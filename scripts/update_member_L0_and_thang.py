# -*- coding: utf-8 -*-
"""
Cập nhật file member (Bui Van Ho) trong worktree grz:
1. Điểm C25,C26,C27: mô tả đổi thành "Điểm (Chưa đạt < 1, Đạt >=1, Tốt=1.2)".
2. THANG ĐÁNH GIÁ CHI TIẾT: thêm L0 "Chưa đạt kết quả hoặc năng lực chưa đạt", đổi title (L0/L1/L2/L3).
3. Mức C7:C10: header "Mức (L0/L1/L2/L3)", data validation L0,L1,L2,L3, công thức D7:D10 với L0=0.8, L1=0.9, L2=1, L3=1.2.
"""
from __future__ import annotations

import os
import sys

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMBER_PATH = os.path.join(BASE_DIR, "members", "P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx")
SHEET_PE = "Product_Engineer"

# P2-Core: L0=0.8 (<1 Chưa đạt), L1=0.9, L2=1 (Đạt), L3=1.2 (Tốt)
CORE_L0, CORE_L1, CORE_L2, CORE_L3 = 0.8, 0.9, 1, 1.2


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    wb = openpyxl.load_workbook(MEMBER_PATH, data_only=False)
    if SHEET_PE not in wb.sheetnames:
        print("Sheet Product_Engineer không tồn tại.")
        wb.close()
        return

    ws = wb[SHEET_PE]

    # 1. Header Mức (row 6 col 3): Mức (L0/L1/L2/L3)
    if ws.cell(6, 3).value:
        ws.cell(6, 3).value = "Mức (L0/L1/L2/L3)"

    # 2. THANG ĐÁNH GIÁ CHI TIẾT: đổi title thành (L0/L1/L2/L3), thêm dòng L0 (chèn trước để không lệch ô mô tả Điểm)
    if ws.cell(13, 1).value and "THANG" in str(ws.cell(13, 1).value):
        ws.cell(13, 1).value = "THANG ĐÁNH GIÁ CHI TIẾT (L0/L1/L2/L3)"
    ws.insert_rows(15)
    ws.cell(15, 1).value = "L0"
    ws.cell(15, 2).value = "Chưa đạt kết quả hoặc năng lực chưa đạt."

    # 3. Mô tả điểm C25:C27: Điểm (Chưa đạt < 1, Đạt >=1, Tốt=1.2) — sau khi chèn dòng, ô thường ở row 25
    for r in range(23, 28):
        val = ws.cell(r, 3).value
        if val and "Điểm" in str(val) and "Chưa đạt" in str(val):
            ws.cell(r, 3).value = "Điểm (Chưa đạt < 1, Đạt >=1, Tốt=1.2)"
            break

    # 4. Data validation C7:C10: L0,L1,L2,L3
    to_remove = []
    for dv in list(ws.data_validations.dataValidation):
        sqref_str = str(dv.sqref) if dv.sqref else ""
        if "C7:C10" in sqref_str or "C7" in sqref_str:
            to_remove.append(dv)
    for dv in to_remove:
        ws.data_validations.dataValidation.remove(dv)
    dv_new = DataValidation(type="list", formula1='"L0,L1,L2,L3"', allow_blank=True)
    dv_new.add("C7:C10")
    ws.add_data_validation(dv_new)

    # 5. D7:D10 – công thức 4 mức L0=0.8, L1=0.9, L2=1, L3=1.2 (P2-Core max 1.2)
    for r in range(7, 11):
        ws.cell(r, 4).value = (
            f'=IF(C{r}="","",B{r}*IF(C{r}="L0",{CORE_L0},IF(C{r}="L1",{CORE_L1},IF(C{r}="L2",{CORE_L2},IF(C{r}="L3",{CORE_L3},0))))/100)'
        )
    ws.cell(11, 4).value = "=SUM(D7:D10)"

    wb.save(MEMBER_PATH)
    wb.close()
    print("Đã cập nhật: Điểm (Chưa đạt < 1, Đạt >=1, Tốt=1.2); THANG thêm L0; Mức (L0/L1/L2/L3), D7:D10 với L0=0.8,L1=0.9,L2=1,L3=1.2.")


if __name__ == "__main__":
    main()
