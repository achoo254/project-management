# -*- coding: utf-8 -*-
"""
Sau khi copy file Dinh Tien Chuong -> Bui Van Ho, đặt lại tên và chạy công thức.
"""
from __future__ import annotations

import os
import sys

import openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "members", "P2_Form_BP_Cong_Nghe - Bui Van Ho.xlsx")

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    wb = openpyxl.load_workbook(PATH, data_only=False)
    ws = wb["Product_Engineer"]
    # Họ và tên thường ở B3
    if ws.cell(3, 1).value and "Họ" in str(ws.cell(3, 1).value):
        ws.cell(3, 2).value = "Bùi Văn Hổ"
    wb.save(PATH)
    wb.close()
    print("Đã đặt tên Bùi Văn Hổ.")

if __name__ == "__main__":
    main()
