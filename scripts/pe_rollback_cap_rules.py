# -*- coding: utf-8 -*-
"""
Rollback: bỏ 3 luật cap P2-Delivery.
- Xóa nội dung hàng 28 (A28:B28, C28), bỏ data validation C28.
- B30 trở lại công thức cũ: chỉ trung bình C25:C27 (Chưa đạt=1, Đạt=2, Tốt=3), không cap.
"""
from __future__ import annotations

import sys
import os
import openpyxl

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


def rollback_cap(path: str) -> bool:
    """Bỏ cap: xóa hàng 28, B30 = trung bình không cap."""
    wb = openpyxl.load_workbook(path, data_only=False)
    if SHEET not in wb.sheetnames:
        print(f"  Skip (no sheet '{SHEET}'): {path}")
        wb.close()
        return False

    ws = wb[SHEET]

    # 1. Bỏ merge A28:B28 (nếu có), xóa nội dung A28, B28, C28
    merged = [m for m in list(ws.merged_cells.ranges) if m.min_row == 28 and m.max_row == 28]
    for m in merged:
        ws.unmerge_cells(str(m))
    ws.cell(28, 1).value = None
    ws.cell(28, 2).value = None
    ws.cell(28, 3).value = None

    # 2. Bỏ data validation áp dụng cho C28
    if ws.data_validations:
        kept = [
            dv for dv in ws.data_validations.dataValidation
            if "C28" not in str(getattr(dv, "sqref", ""))
        ]
        ws.data_validations.dataValidation = kept

    # 3. B30 = công thức cũ (chỉ trung bình, MIN 5); thang 1.5/3.5/5 giống P2-Core
    sum_part = (
        'IF(C25="",0,IF(C25="Chưa đạt",1.5,IF(C25="Đạt",3.5,IF(C25="Tốt",5,0))))+'
        'IF(C26="",0,IF(C26="Chưa đạt",1.5,IF(C26="Đạt",3.5,IF(C26="Tốt",5,0))))+'
        'IF(C27="",0,IF(C27="Chưa đạt",1.5,IF(C27="Đạt",3.5,IF(C27="Tốt",5,0))))'
    )
    count_part = '(C25<>"")+(C26<>"")+(C27<>"")'
    ws.cell(30, 2).value = f'=IF({count_part}=0,"",MIN(({sum_part})/{count_part},5))'

    try:
        wb.save(path)
    except PermissionError:
        print(f"  Permission denied (file open?): {os.path.basename(path)}")
        wb.close()
        return False
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
        if rollback_cap(path):
            print(f"OK: {name}")
    print("Done: Đã bỏ cap, B30 = trung bình C25:C27 (1.5/3.5/5).")


if __name__ == "__main__":
    main()
