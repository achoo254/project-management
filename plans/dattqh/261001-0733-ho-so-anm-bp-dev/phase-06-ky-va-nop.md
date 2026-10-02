---
phase: 6
title: "Ký và nộp"
status: in-progress
priority: P1
effort: "S"
dependencies: [5]
---

# Phase 6: Ký và nộp (thứ Sáu 09/10, trước 17:00)

## Goal
Ban ATANM & BVDL nhận đủ bộ hồ sơ trước 17:00 09/10/2026 và xác nhận đã nhận.

## Tasks & Steps
- [ ] Bước 1: Sáng 09/10: người phụ trách BP-DEV ký ô "Người lập" trên 23 tài liệu. Ô "Người phê duyệt" giữ trống nếu chưa được chốt; nếu đã chốt thì trình ký.
- [ ] Bước 2 (script đóng gói sẵn sàng, chạy thử 01/10 đạt; đóng gói chính thức sáng 09/10): Đóng gói `BP-DEV-ho-so-2026-10.zip` gồm:
   - `01-quy-trinh/` (10 tài liệu)
   - `02-bieu-mau/` (13 tài liệu)
   - `03-bang-tra-loi/` (bản sao Excel đã điền, ma trận 122 dòng)
   - `04-bang-chung-nop/`: **bản tóm tắt đã lọc** của bằng chứng (số lượng, kết luận, ngày chốt). Không có đường dẫn file nhạy cảm, không có tên tài khoản cá nhân ngoài danh sách được phép, không có bằng chứng thô. Thư mục `04-bang-chung/` thô giữ nội bộ.
   - `00-thu-gui.txt`: danh sách tài liệu, các mục CHƯA XÁC MINH đang chờ đơn vị nào, các điểm cần Ban sửa trong file Excel (tên đơn vị không tồn tại, các dòng chỉ ghi chung "BP-DEV")
- [ ] Bước 3: Gửi cho Ban ATANM & BVDL trước 15:00 (chừa 2 giờ cho việc bổ sung). Nhận xác nhận bằng văn bản.
- [ ] Bước 4: Sau khi nộp: chép bảng hạn khắc phục (mọi CHƯA CÓ / CHƯA XÁC MINH) sang danh sách theo dõi của BP-DEV, mốc gần nhất là 31/10/2026. Xóa các repo đã clone tạm vào scratchpad ở Phase 1; giữ `99-cong-cu-noi-bo/` đến khi Ban duyệt bản 1.0.

## Verification
- [ ] Có email hoặc tin nhắn xác nhận đã nhận của Ban, thời điểm trước 17:00 09/10/2026.
- [ ] File zip mở được; số file khớp danh sách trong `00-thu-gui.txt` (chạy thử 01/10: 27 tệp, khớp, 0 lỗi; kiểm lại với bản khóa ngày 09/10).
- [x] Danh sách theo dõi hạn khắc phục có đủ mọi mục khoảng trống, mỗi mục có người phụ trách (`06-theo-doi-khac-phuc/so-theo-doi-han-khac-phuc.xlsx`, 192 mục; sinh lại khi nộp).

## Chuẩn bị sẵn (01/10/2026)
- Script đóng gói `99-cong-cu-noi-bo/phase6/build_package.py`: sinh `05-ban-nop/04-bang-chung-nop/EVD-TT-<ngày>-tom-tat-bang-chung.docx` (bản tóm tắt đã lọc, 11 nhóm bằng chứng, chỉ số lượng và kết luận), `05-ban-nop/00-thu-gui.txt`, `05-ban-nop/BP-DEV-ho-so-2026-10.zip`; tự kiểm: không có bằng chứng thô, số tệp khớp thư gửi, không từ cấm, không chuỗi giống bí mật. Chạy thử 01/10: 27 tệp, 990 KB, 0 lỗi. **Chưa gửi.**
- Sổ theo dõi `06-theo-doi-khac-phuc/so-theo-doi-han-khac-phuc.xlsx`: 192 mục từ sổ khoảng trống, sắp theo hạn sớm nhất (10/2026: 132, 11/2026: 3, 12/2026: 55, 03/2027: 1, 06/2027: 1), có cột tình trạng xử lý.
- Tài liệu nộp chỉ còn tên đăng nhập trong đường dẫn repo sản phẩm (cần cho danh mục) và email công vụ của người phụ trách BP-DEV.

## Trình tự chạy 08/10 (khóa bản) và 09/10 (nộp)
Công cụ ở iCloud `BP-DEV-ho-so-2026-10/99-cong-cu-noi-bo/` (đọc `00-doc-truoc.txt`; không nộp, không commit).
1. Áp câu trả lời 05/10 (Excel `answers.py`, nguồn HTML), chạy `fill_122.py`.
2. Ghi người rà chéo vào `99-cong-cu-noi-bo/phase5/reviewers.json`, xuất lại 23 .docx bằng `html2docx.py`.
3. `FREEZE=1 python qa_check.py <HS> <HS>/04-bang-chung/EVD-QA-20261008-kiem-tra-tu-dong.txt` → 0 lỗi. 17:00 08/10 khóa bản.
4. 09/10 sáng: sinh lại sổ khoảng trống và sổ theo dõi, chạy `build_package.py` → 0 lỗi; người phụ trách BP-DEV ký ô "Người lập"; gửi Ban trước 15:00 và lưu xác nhận đã nhận.
