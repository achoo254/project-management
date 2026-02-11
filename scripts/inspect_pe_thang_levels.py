# -*- coding: utf-8 -*-
"""Inspect THANG ĐÁNH GIÁ CHI TIẾT and Mức header in Product_Engineer."""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import openpyxl
import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(base, "members", "P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx")
wb = openpyxl.load_workbook(path, data_only=True)
ws = wb["Product_Engineer"]
for r in range(1, 30):
    row = [ws.cell(r, c).value for c in range(1, 5)]
    if any(x is not None and str(x).strip() for x in row):
        print(r, row)
wb.close()
