# -*- coding: utf-8 -*-
"""
Sheet Product_Engineer: ô C25–C27 dùng thang Text → Điểm (giống P2-Core):
  Chưa đạt = 1.5, Đạt = 3.5, Tốt = 5
- Data validation C25:C27 = list "Chưa đạt", "Đạt", "Tốt"
- Công thức B30 (P2-Delivery) = trung bình điểm quy đổi (1.5, 3.5, 5)
- Chuyển giá trị hiện tại (L1/L2/L3 hoặc 1–5) sang Chưa đạt/Đạt/Tốt
"""
from __future__ import annotations

import sys
import os
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = r"c:\CONG VIEC\project-management"
PATH_MAIN = os.path.join(ROOT, "P2_Form_BP_Cong_Nghe.xlsx")
MEMBERS_DIR = os.path.join(ROOT, "members")
MEMBER_FILES = [
    "P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx",
    "P2_Form_BP_Cong_Nghe - Dinh Tien Chuong.xlsx",
    "P2_Form_BP_Cong_Nghe - Nguyen Dang Duc.xlsx",
    "P2_Form_BP_Cong_Nghe - Nguyen Huy Hoang.xlsx",
]
SHEET = "Product_Engineer"

# Mapping: Text -> Điểm (giống P2-Core, thang 1–5)
# Chưa đạt=1.5, Đạt=3.5, Tốt=5


def old_value_to_new(val) -> str | None:
    """Chuyển giá trị hiện tại (L1/L2/L3 hoặc số 1–5) sang Chưa đạt / Đạt / Tốt."""
    if val is None or (isinstance(val, str) and val.strip() == ""):
        return None
    s = str(val).strip()
    # Đã đúng format mới -> giữ nguyên
    if s in ("Chưa đạt", "Đạt", "Tốt"):
        return s
    # L1/L2/L3
    if s.upper() == "L1":
        return "Chưa đạt"
    if s.upper() == "L2":
        return "Đạt"
    if s.upper() == "L3":
        return "Tốt"
    # Số 1–5
    try:
        n = int(float(val))
        if n in (1, 2):
            return "Chưa đạt"
        if n in (3, 4):
            return "Đạt"
        if n == 5:
            return "Tốt"
    except (TypeError, ValueError):
        pass
    return None


def _excel_conv(cell_ref: str) -> str:
    """Công thức Excel: ô cell_ref (text) -> số 1/2/3, ô trống -> rỗng."""
    return (
        f'IF({cell_ref}="","",'
        f'IF({cell_ref}="Chưa đạt",1,IF({cell_ref}="Đạt",2,IF({cell_ref}="Tốt",3,""))))'
    )


def apply_to_file(path: str) -> bool:
    """Áp dụng mapping C25:C27 (Chưa đạt/Đạt/Tốt) cho một file. Trả về True nếu thành công."""
    wb = openpyxl.load_workbook(path, data_only=False)
    if SHEET not in wb.sheetnames:
        print(f"  Skip (no sheet '{SHEET}'): {path}")
        wb.close()
        return False

    ws = wb[SHEET]

    # 0. Chuyển giá trị hiện tại C25:C27 sang Chưa đạt/Đạt/Tốt (trước khi đổi DV)
    for r in (25, 26, 27):
        cell = ws.cell(r, 3)
        if cell.data_type != "f" and cell.value is not None:
            new_val = old_value_to_new(cell.value)
            if new_val is not None:
                cell.value = new_val

    # 1. Bỏ C25:C27 khỏi data validation L1/L2/L3 (nếu có), giữ L1/L2/L3 chỉ cho C7:C10
    if ws.data_validations:
        for dv in ws.data_validations.dataValidation:
            sqref = getattr(dv, "sqref", None) or getattr(dv, "ranges", "")
            if sqref and "C25" in str(sqref):
                f1 = getattr(dv, "formula1", "") or ""
                if "L1" in f1 or "L2" in f1:
                    dv.sqref = "C7:C10"

    # 2. Thêm data validation cho C25:C27: list Chưa đạt, Đạt, Tốt
    dv_new = DataValidation(
        type="list",
        formula1='"Chưa đạt,Đạt,Tốt"',
        allow_blank=True,
    )
    dv_new.add("C25:C27")
    ws.add_data_validation(dv_new)

    # 3. Cập nhật tiêu đề cột C (row 24): Điểm quy đổi 1.5 / 3.5 / 5 (giống P2-Core)
    c24 = ws.cell(24, 3).value
    if c24:
        s = str(c24).strip()
        if "1" in s and "5" in s or "L1" in s or "L2" in s or "Chưa đạt=1" in s:
            ws.cell(24, 3).value = "Điểm (Chưa đạt=1.5, Đạt=3.5, Tốt=5)"

    # 4. Công thức B30: P2-Delivery = trung bình điểm C25,C26,C27 (quy đổi text -> 1.5, 3.5, 5)
    sum_part = (
        f'IF(C25="",0,IF(C25="Chưa đạt",1.5,IF(C25="Đạt",3.5,IF(C25="Tốt",5,0))))+'
        f'IF(C26="",0,IF(C26="Chưa đạt",1.5,IF(C26="Đạt",3.5,IF(C26="Tốt",5,0))))+'
        f'IF(C27="",0,IF(C27="Chưa đạt",1.5,IF(C27="Đạt",3.5,IF(C27="Tốt",5,0))))'
    )
    count_part = '(C25<>"")+(C26<>"")+(C27<>"")'
    ws.cell(30, 2).value = (
        f'=IF({count_part}=0,"",MIN(({sum_part})/{count_part},5))'
    )

    wb.save(path)
    wb.close()
    return True


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    paths = [PATH_MAIN]
    for f in MEMBER_FILES:
        p = os.path.join(MEMBERS_DIR, f)
        if os.path.isfile(p):
            paths.append(p)

    for path in paths:
        name = os.path.basename(path)
        if apply_to_file(path):
            print(f"OK: {name}")
    print("Done: C25:C27 mapping Chưa đạt=1.5, Đạt=3.5, Tốt=5 (giống P2-Core); giá trị cũ đã quy đổi.")


if __name__ == "__main__":
    main()
