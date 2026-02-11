# -*- coding: utf-8 -*-
"""Inspect P2 Core, P2 Delivery, P2+ formulas in a member form."""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import openpyxl

path = r"c:\CONG VIEC\project-management\members\P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx"
# Only Product_Engineer and key cells
wb = openpyxl.load_workbook(path, data_only=False)
print("Sheets:", wb.sheetnames)

for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    print("\n=== Sheet:", sheet_name, "===")
    # Find cells with formulas or values that might be P2 Core, Delivery, P2+
    for r in range(1, min(ws.max_row, 35) + 1):
        for c in range(1, min(ws.max_column, 8) + 1):
            cell = ws.cell(r, c)
            if hasattr(cell, 'data_type') and cell.data_type == 'f':
                print("  %s%d: %s" % (openpyxl.utils.get_column_letter(c), r, cell.value))
            val = cell.value
            if val is None:
                continue
            s = str(val).strip().upper()
            if "P2" in s and ("CORE" in s or "DELIVERY" in s or "TỔNG" in s or "TONG" in s) or "TỔNG P2" in s:
                print("  [%s%d] label: %s" % (openpyxl.utils.get_column_letter(c), r, str(val)[:60]))

wb.close()
