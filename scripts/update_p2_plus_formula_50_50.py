# -*- coding: utf-8 -*-
"""
Sửa công thức P2+ Tổng trong P2_Form_BP_Cong_Nghe.xlsx:
P2+ Tổng = (P2-Core x 50%) + (P2-Delivery x 50%)
và cập nhật nội dung mô tả công thức (70%/30% -> 50%/50%) trong toàn workbook.
"""
from __future__ import annotations

import sys
import re
import openpyxl

PATH = r"c:\CONG VIEC\project-management\P2_Form_BP_Cong_Nghe.xlsx"


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    wb = openpyxl.load_workbook(PATH, data_only=False)

    # 1. Product_Engineer: ô P2+ Tổng (row 31, col B) = 50% Core + 50% Delivery
    if "Product_Engineer" in wb.sheetnames:
        ws = wb["Product_Engineer"]
        val = ws.cell(31, 1).value
        if val and "P2+" in str(val) and "Tổng" in str(val):
            ws.cell(31, 2).value = '=IF(OR(D11="",B30=""),"",D11*0.5+B30*0.5)'

    # 2. Tất cả sheet: thay nội dung chữ "70%" và "30%" trong ngữ cảnh P2+ thành "50%" và "50%"
    for name in wb.sheetnames:
        ws = wb[name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value is None or not isinstance(cell.value, str):
                    continue
                s = cell.value
                # P2+ Tổng = (P2-Core × 70%) + (P2-Delivery × 30%) -> 50%, 50%
                if "P2+" in s and "70%" in s and "30%" in s:
                    new_s = s.replace("70%", "50%").replace("30%", "50%")
                    if new_s != s:
                        cell.value = new_s
                # Các biến thể: 0.7/0.3 trong mô tả
                if "P2" in s and ("× 70%" in s or "x 70%" in s or "70%" in s) and "30%" in s:
                    cell.value = s.replace("70%", "50%").replace("30%", "50%")

    wb.save(PATH)
    wb.close()
    print("Done: P2+ Tổng = (P2-Core x 50%) + (P2-Delivery x 50%) in P2_Form_BP_Cong_Nghe.xlsx")


if __name__ == "__main__":
    main()
