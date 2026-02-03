# -*- coding: utf-8 -*-
"""
Convert Product_Engineer sheet in P2_Form_BP_Cong_Nghe.xlsx:
- THANG ĐÁNH GIÁ CHI TIẾT (1–5) -> 3 levels: L1 (1–2), L2 (3–4), L3 (5)
- Ô nhập Điểm (1–5) -> dropdown L1/L2/L3
- Công thức quy đổi: L1=1.5, L2=3.5, L3=5 (trên thang 1–5)
"""
from __future__ import annotations

import sys
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

PATH = r"c:\CONG VIEC\project-management\P2_Form_BP_Cong_Nghe.xlsx"
SHEET = "Product_Engineer"

# Quy đổi L1/L2/L3 sang số (thang 1-5): 1-2 -> 1.5, 3-4 -> 3.5, 5 -> 5
FORMULA_CONVERT_C = (
    'IF({cell}="L1",1.5,IF({cell}="L2",3.5,IF({cell}="L3",5,0)))'
)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    wb = openpyxl.load_workbook(PATH, data_only=False)
    if SHEET not in wb.sheetnames:
        print(f"Sheet '{SHEET}' not found")
        wb.close()
        return

    ws = wb[SHEET]

    # 1. Đổi header cột Điểm (1–5) -> Mức (L1/L2/L3)
    if ws.cell(6, 3).value:
        ws.cell(6, 3).value = "Mức (L1/L2/L3)"
    if ws.cell(24, 3).value and "1" in str(ws.cell(24, 3).value) and "5" in str(ws.cell(24, 3).value):
        ws.cell(24, 3).value = "Mức (L1/L2/L3)"

    # 2. Thay THANG ĐÁNH GIÁ CHI TIẾT (1–5) thành 3 level
    # Bỏ merge cũ trong vùng 13-19 trước
    to_unmerge = [m for m in list(ws.merged_cells.ranges) if m.min_row >= 13 and m.max_row <= 19]
    for m in to_unmerge:
        ws.unmerge_cells(str(m))
    ws.cell(13, 1).value = "THANG ĐÁNH GIÁ CHI TIẾT (L1/L2/L3)"
    ws.merge_cells(start_row=13, start_column=1, end_row=13, end_column=5)

    # Row 14: header Mức | Mô tả
    ws.cell(14, 1).value = "Mức"
    ws.cell(14, 2).value = "Mô tả"

    # Rows 15-17: L1, L2, L3
    level_rows = [
        ("L1", "1–2: Phải được hướng dẫn; làm được phần việc cơ bản, cần review."),
        ("L2", "3–4: Chủ động hoàn thành; chất lượng ổn; ít rework; chủ đạo hoàn thành."),
        ("L3", "5: Làm vượt kỳ vọng; tối ưu / chuẩn hóa."),
    ]
    for i, (level, desc) in enumerate(level_rows):
        r = 15 + i
        ws.cell(r, 1).value = level
        ws.cell(r, 2).value = desc
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    # Xóa nội dung cũ hàng 18, 19 (mức 4, 5 cũ) - chỉ ghi ô A,B vì C-E có thể merge
    for r in range(18, 20):
        ws.cell(r, 1).value = None
        ws.cell(r, 2).value = None

    # 3. Dropdown L1/L2/L3 cho các ô điểm
    dv = DataValidation(type="list", formula1='"L1,L2,L3"', allow_blank=True)
    dv.add("C7:C10")
    dv.add("C25:C27")
    ws.add_data_validation(dv)

    # 4. Công thức D7:D10: quy đổi L1/L2/L3 -> số rồi B*val/100
    for r in range(7, 11):
        cell_c = f"C{r}"
        conv = FORMULA_CONVERT_C.format(cell=cell_c)
        ws.cell(r, 4).value = f'=IF(C{r}="","",B{r}*{conv}/100)'

    # 5. Công thức B30 (P2-Delivery): AVERAGE của C25,C26,C27 quy đổi L1/L2/L3 -> số
    # B30 hiện tại = IF(COUNT(C25:C27)=0,"",AVERAGE(C25:C27))
    conv25 = FORMULA_CONVERT_C.format(cell="C25")
    conv26 = FORMULA_CONVERT_C.format(cell="C26")
    conv27 = FORMULA_CONVERT_C.format(cell="C27")
    ws.cell(30, 2).value = (
        f'=IF(COUNT(C25:C27)=0,"",({conv25}+{conv26}+{conv27})/3)'
    )

    # 5b. P2+ Tổng = (P2-Core × 50%) + (P2-Delivery × 50%)
    ws.cell(31, 2).value = '=IF(OR(D11="",B30=""),"",D11*0.5+B30*0.5)'

    # 6. Chuyển giá trị số cũ (1,2,3,4,5) trong C7:C10 và C25:C27 sang L1/L2/L3 nếu có
    def num_to_level(val):
        if val is None:
            return None
        try:
            n = int(float(val))
            if 1 <= n <= 2:
                return "L1"
            if 3 <= n <= 4:
                return "L2"
            if n == 5:
                return "L3"
        except (TypeError, ValueError):
            pass
        return None

    for r in [7, 8, 9, 10, 25, 26, 27]:
        cell = ws.cell(r, 3)
        if cell.data_type != "f" and cell.value is not None:  # not formula
            converted = num_to_level(cell.value)
            if converted:
                cell.value = converted

    wb.save(PATH)
    wb.close()
    print("Done: Product_Engineer converted to L1/L2/L3 with dropdowns.")


if __name__ == "__main__":
    main()
