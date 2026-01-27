from __future__ import annotations

from typing import Dict, List, Tuple

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo


def _safe_str(v: object) -> str:
    return "" if v is None else str(v).strip()


def _read_wide_format(ws) -> Dict[Tuple[str, str, int], str]:
    """
    Read current wide format (Role x Category x Level -> Description).
    Returns dict mapping (role, category, level) -> description.
    """
    data: Dict[Tuple[str, str, int], str] = {}
    current_role = None
    current_category = None
    
    for row in ws.iter_rows(min_row=1, values_only=True):
        if not row:
            continue
        
        first_cell = _safe_str(row[0])
        
        # Role header (e.g., "Backend")
        if first_cell and first_cell not in ["CẤP ĐỘ NĂNG LỰC (THEO VAI TRÒ)", "Gợi ý:", "Nhóm năng lực"]:
            if first_cell in ["Backend", "FrontEnd", "Designer", "FullStack"]:
                current_role = first_cell
                continue
        
        # Header row (skip)
        if first_cell == "Nhóm năng lực":
            continue
        
        # Category row (e.g., "A. Năng lực kỹ thuật")
        if first_cell.startswith(("A. ", "B. ", "C. ", "D. ")):
            current_category = first_cell
            # Read level columns (columns B=index1, C=index2, D=index3, E=index4 are Level 1, 2, 3, 4)
            for col_idx in range(1, 5):  # row[1], row[2], row[3], row[4] (0-indexed)
                level = col_idx  # Level 1, 2, 3, 4
                if col_idx < len(row):
                    desc = _safe_str(row[col_idx])
                    if desc and current_role and current_category:
                        data[(current_role, current_category, level)] = desc
    
    return data


def _map_level_4_to_3(old_level: int) -> int:
    """
    Map old 4-level system to new 3-level system:
    - Old Level 1-2 -> New Level 1 (Làm tốt phần việc kỹ thuật)
    - Old Level 3 -> New Level 2 (Giải quyết bài toán xuyên hệ thống)
    - Old Level 4 -> New Level 3 (Định hướng, tạo chuẩn, scale)
    """
    if old_level <= 2:
        return 1
    elif old_level == 3:
        return 2
    else:  # old_level == 4
        return 3


def _merge_descriptions(desc1: str, desc2: str) -> str:
    """Merge two descriptions, preferring the more detailed one (desc2)."""
    if not desc1:
        return desc2
    if not desc2:
        return desc1
    # Prefer desc2 (Level 2) as it's more detailed, but combine if both exist
    if desc1 in desc2:
        return desc2
    return desc2  # Prefer Level 2 description


def _apply_border(ws, cell_range: str, border: Border) -> None:
    for row in ws[cell_range]:
        for c in row:
            c.border = border


def _set_col_widths(ws, widths: Dict[int, float]) -> None:
    for col_idx, w in widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = w


def _read_from_template() -> Dict[Tuple[str, str, int], str]:
    """Read original 4-level data from template."""
    template_path = r"c:\CONG VIEC\project-management\P2_Template_BP_Cong_Nghe_v2.xlsx"
    wb = openpyxl.load_workbook(template_path)
    ws = wb["Tiêu chí"] if "Tiêu chí" in wb.sheetnames else wb[wb.sheetnames[2]]
    
    role_map = {"BE": "Backend", "FE": "FrontEnd", "DE": "Designer", "FS": "FullStack"}
    category_map = {
        "Core_Skill": "A. Năng lực kỹ thuật",
        "Delivery": "B. Ownership & trách nhiệm",
        "DevOps": "C. DevOps & vận hành",
        "AI_Agent": "D. AI Agent & cải tiến",
    }
    
    data: Dict[Tuple[str, str, int], str] = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if not r or not any(r[:4]):
            continue
        role_code = _safe_str(r[0])
        category_code = _safe_str(r[1])
        try:
            lvl = int(r[2])
        except Exception:
            continue
        desc = _safe_str(r[3])
        
        # Map template levels 2..5 -> 1..4 for JuniorPlus table
        if lvl < 2 or lvl > 5:
            continue
        lvl = lvl - 1  # 2->1, 3->2, 4->3, 5->4
        
        role = role_map.get(role_code, role_code)
        category = category_map.get(category_code, category_code)
        if role and category and desc:
            data[(role, category, lvl)] = desc
    
    wb.close()
    return data


def main() -> None:
    path = r"c:\CONG VIEC\project-management\P2_Form_Professional_Report_JuniorPlus_Table.xlsx"
    wb = openpyxl.load_workbook(path)
    
    # Find sheet by name (handle encoding)
    sheet_name = None
    for s in wb.sheetnames:
        if "cấp" in s.lower() or "năng lực" in s.lower():
            sheet_name = s
            break
    
    if not sheet_name:
        print("Sheet 'Cấp độ năng lực theo vai trò' not found!")
        wb.close()
        return
    
    old_ws = wb[sheet_name]
    old_idx = wb.sheetnames.index(sheet_name)
    
    # Read original 4-level data from template (more reliable)
    old_data = _read_from_template()
    
    # Debug: print what we read
    # print(f"Read {len(old_data)} entries from old sheet")
    # for (r, c, l), d in sorted(old_data.items()):
    #     print(f"  {r} | {c} | Level {l}: {d[:50]}...")
    
    # Build new data structure: (role, category) -> {new_level: description}
    new_data: Dict[Tuple[str, str], Dict[int, str]] = {}
    roles = set()
    categories = set()
    
    # First pass: collect all data by new level
    temp_data: Dict[Tuple[str, str, int], str] = {}
    for (role, category, old_level), desc in old_data.items():
        roles.add(role)
        categories.add(category)
        new_level = _map_level_4_to_3(old_level)
        temp_data[(role, category, new_level, old_level)] = desc
    
    # Second pass: merge Level 1-2 old into Level 1 new
    for (role, category, new_level, old_level), desc in temp_data.items():
        key = (role, category)
        if key not in new_data:
            new_data[key] = {}
        
        if new_level == 1:
            # Merge old Level 1 and Level 2 into new Level 1
            if 1 not in new_data[key]:
                new_data[key][1] = desc
            else:
                # Prefer Level 2 (old_level==2) over Level 1 (old_level==1)
                if old_level == 2:
                    new_data[key][1] = desc  # Level 2 is more detailed
                # else keep existing (which is Level 1)
        else:
            new_data[key][new_level] = desc
    
    roles = sorted(roles)
    categories = sorted(categories)
    
    # Recreate sheet
    wb.remove(old_ws)
    ws = wb.create_sheet(sheet_name, old_idx)
    
    # Styles
    fill_title = PatternFill("solid", fgColor="1F4E79")
    fill_role = PatternFill("solid", fgColor="2F5597")
    fill_header = PatternFill("solid", fgColor="D9E1F2")
    fill_category = PatternFill("solid", fgColor="F2F2F2")
    
    font_title = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
    font_role = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
    font_header = Font(name="Calibri", size=11, bold=True, color="1F1F1F")
    font_body = Font(name="Calibri", size=11, color="1F1F1F")
    font_category = Font(name="Calibri", size=11, bold=True, color="1F1F1F")
    font_hint = Font(name="Calibri", size=10, italic=True, color="404040")
    
    thin = Side(style="thin", color="BFBFBF")
    border_thin = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left_top = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_left_center = Alignment(horizontal="left", vertical="center", wrap_text=True)
    
    # New level labels with descriptions
    level_labels = [
        ("Level 1", "Làm tốt phần việc kỹ thuật của mình"),
        ("Level 2", "Giải quyết bài toán xuyên hệ thống"),
        ("Level 3", "Định hướng, tạo chuẩn, scale đội/nghệ"),
    ]
    
    cols = ["Nhóm năng lực"] + [label[0] for label in level_labels]
    last_col = len(cols)
    
    # Title
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    t = ws.cell(1, 1, "CẤP ĐỘ NĂNG LỰC (THEO VAI TRÒ)")
    t.fill = fill_title
    t.font = font_title
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30
    
    # Hint with level descriptions
    hint_text = "Gợi ý: dùng nút +/- (Outline) để thu gọn/mở rộng theo từng Vai trò. "
    hint_text += " | ".join([f"{label[0]}: {label[1]}" for label in level_labels])
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=last_col)
    h = ws.cell(2, 1, hint_text)
    h.font = font_hint
    h.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[2].height = 24
    
    r = 4
    ws.sheet_properties.outlinePr.summaryBelow = False
    ws.sheet_properties.outlinePr.applyStyles = True
    
    # Column widths
    widths = {1: 22}
    for i in range(2, last_col + 1):
        widths[i] = 50
    _set_col_widths(ws, widths)
    
    # Build per-role tables
    table_idx = 1
    for role in roles:
        # Role header row
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=last_col)
        c = ws.cell(r, 1, role)
        c.fill = fill_role
        c.font = font_role
        c.alignment = align_left_center
        ws.row_dimensions[r].height = 22
        
        role_header_row = r
        r += 1
        
        # Table header row
        for col_idx, label in enumerate(cols, start=1):
            cell_ = ws.cell(r, col_idx, label)
            cell_.fill = fill_header
            cell_.font = font_header
            cell_.alignment = align_center
        ws.row_dimensions[r].height = 20
        
        table_header_row = r
        r += 1
        
        # Category rows
        for category in categories:
            cat_cell = ws.cell(r, 1, category)
            cat_cell.fill = fill_category
            cat_cell.font = font_category
            cat_cell.alignment = align_left_center
            
            for i, (level_label, _) in enumerate(level_labels, start=2):
                new_level = i - 1  # 1, 2, 3
                desc = new_data.get((role, category), {}).get(new_level, "")
                d = ws.cell(r, i, desc)
                d.font = font_body
                d.alignment = align_left_top
            ws.row_dimensions[r].height = 80
            r += 1
        
        table_first_row = table_header_row
        table_last_row = r - 1
        table_ref = f"A{table_first_row}:{get_column_letter(last_col)}{table_last_row}"
        
        # Add Excel table
        tab = Table(displayName=f"Levels_{role}_{table_idx}", ref=table_ref)
        tab.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium9",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=False,
        )
        ws.add_table(tab)
        table_idx += 1
        
        _apply_border(ws, f"A{table_header_row}:{get_column_letter(last_col)}{table_last_row}", border_thin)
        
        # Group rows
        detail_start = table_header_row
        detail_end = table_last_row
        for rr in range(detail_start, detail_end + 1):
            ws.row_dimensions[rr].outlineLevel = 1
            ws.row_dimensions[rr].hidden = True
        ws.row_dimensions[detail_end].collapsed = True
        ws.row_dimensions[role_header_row].outlineLevel = 0
        
        r += 1  # spacer
    
    # Freeze panes
    ws.freeze_panes = "A4"
    
    wb.save(path)
    wb.close()
    try:
        import sys
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(f"Successfully refactored sheet from 4 levels to 3 levels!")
    except Exception:
        print("Successfully refactored sheet from 4 levels to 3 levels!")


if __name__ == "__main__":
    main()
