# -*- coding: utf-8 -*-
"""Sửa B31: P2-Delivery lấy từ C26, C27, C28 (không phải C25,C26,C27)."""
from __future__ import annotations

import os
import sys

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "members", "P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx")

DELIVERY_CHUA_DAT = 0.8
DELIVERY_DAT = 1
DELIVERY_TOT = 1.2

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    wb = openpyxl.load_workbook(PATH, data_only=False)
    ws = wb["Product_Engineer"]

    # Tìm ô chứa công thức P2-Delivery (có C25 hoặc C26 trong formula) — thường B31
    for row in (30, 31, 32):
        cell = ws.cell(row, 2)
        if cell.value and isinstance(cell.value, str) and "C25" in cell.value and "Chưa đạt" in cell.value:
            part26 = f'IF(C26="Chưa đạt",{DELIVERY_CHUA_DAT},IF(C26="Đạt",{DELIVERY_DAT},IF(C26="Tốt",{DELIVERY_TOT},0)))'
            part27 = f'IF(C27="Chưa đạt",{DELIVERY_CHUA_DAT},IF(C27="Đạt",{DELIVERY_DAT},IF(C27="Tốt",{DELIVERY_TOT},0)))'
            part28 = f'IF(C28="Chưa đạt",{DELIVERY_CHUA_DAT},IF(C28="Đạt",{DELIVERY_DAT},IF(C28="Tốt",{DELIVERY_TOT},0)))'
            count_part = '(C26<>"")+(C27<>"")+(C28<>"")'
            ws.cell(row, 2).value = (
                f'=IF({count_part}=0,"",(({part26})+({part27})+({part28}))/({count_part}))'
            )
            print(f"Đã sửa ô B{row}: P2-Delivery tính từ C26, C27, C28.")
            break
    else:
        print("Không tìm thấy ô công thức P2-Delivery (C25/C26/C27).")

    # Data validation: chuyển C25:C27 sang C26:C28 (dropdown Chưa đạt/Đạt/Tốt)
    to_remove = [dv for dv in list(ws.data_validations.dataValidation) if dv.sqref and "C25:C27" in str(dv.sqref)]
    for dv in to_remove:
        ws.data_validations.dataValidation.remove(dv)
    dv_new = DataValidation(type="list", formula1='"Chưa đạt,Đạt,Tốt"', allow_blank=True)
    dv_new.add("C26:C28")
    ws.add_data_validation(dv_new)
    print("Đã đặt data validation Chưa đạt/Đạt/Tốt cho C26:C28.")

    wb.save(PATH)
    wb.close()

if __name__ == "__main__":
    main()
