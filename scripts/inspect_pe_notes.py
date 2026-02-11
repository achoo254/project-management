# -*- coding: utf-8 -*-
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import openpyxl
path = r"c:\CONG VIEC\project-management\members\P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx"
wb = openpyxl.load_workbook(path, data_only=True)
ws = wb["Product_Engineer"]
for r in range(20, 35):
    for c in range(1, 6):
        v = ws.cell(r, c).value
        if v and ("1.5" in str(v) or "3.5" in str(v) or "Chưa đạt" in str(v) or "Đạt" in str(v) or "Tốt" in str(v) or "điểm" in str(v).lower()):
            print(r, c, repr(str(v)[:80]))
wb.close()
