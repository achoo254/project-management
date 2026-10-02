---
phase: 4
title: "Kiểm tra dữ kiện và chốt khoảng trống"
status: in-progress
priority: P1
effort: "S"
dependencies: [1]
---

# Phase 4: Kiểm tra dữ kiện và chốt khoảng trống (06/10 → 07/10)

## Goal
Mỗi câu khẳng định trong bộ hồ sơ hoặc được người phụ trách xác nhận đúng thực tế, hoặc được chuyển thành khoảng trống
có hạn. Không còn câu nào đứng một mình không có bằng chứng.

## Tasks & Steps
- [ ] Bước 1: **06/10, người phụ trách BP-DEV kiểm toàn bộ sản phẩm trong phiếu.** Đọc mục 6 và 8 của các DEV-QT liên quan cùng dòng của sản phẩm trong BM-01, BM-02, BM-06, BM-09. Đánh dấu Đúng / Sai / Không chắc. Sai thì sửa kèm bằng chứng. Không chắc thì chuyển thành CHƯA XÁC MINH.
- [x] Bước 2: **07/10 sáng, chốt khoảng trống.** Mục nào BP-DEV không tự xác minh được (sao lưu CSDL, log tập trung, EOL hạ tầng, 2FA toàn GitLab, tài liệu gốc GOV/CMP/OPS): ghi `CHƯA XÁC MINH — <lý do> · Hạn xác minh: 31/10/2026 · Người phụ trách: <tên>` ở cả tài liệu DEV và cột J của bản sao Excel.
- [ ] Bước 4 (01/10: đã có kết luận cho 4 sản phẩm; chatbot iNET Portal chờ câu 12): **07/10, quyết định về dữ liệu ra dịch vụ nước ngoài.** Dựa vào trạng thái production đã xác minh ở Phase 1:
   - Nếu không còn gửi dữ liệu khách hàng hoặc dữ liệu cá nhân: ghi "Không có tính năng sản phẩm nào gửi dữ liệu khách hàng ra dịch vụ đặt máy chủ ở nước ngoài", kèm bằng chứng cấu hình.
   - Nếu vẫn còn gửi: hoặc người có thẩm quyền tắt trước 08/10 (kèm bằng chứng tắt), hoặc kê khai đúng vào BM-09 với trạng thái và hạn xử lý. **Không ghi "không có" khi thực tế vẫn có.**
- [ ] Bước 5 (mô hình người chính/dự phòng đã chốt; tên theo sản phẩm và ngưỡng DET chờ câu 1–3, 13): **07/10, ba quyết định của người phụ trách BP-DEV** (nếu đã có trả lời thì áp ngay):
   - Người chính và người dự phòng ứng phó sự cố: **đã chốt 01/10** — người chính là người phụ trách từng sản phẩm, người dự phòng là thành viên khác của BP-DEV; CEO chịu trách nhiệm cuối cùng. Tên theo từng sản phẩm lấy từ phiếu, ghi vào BM-01 trước 09/10.
   - Ngưỡng cho DET dòng 73–74: mặc định đề xuất là tỷ lệ lỗi 5xx > 5% trong 5 phút; > 20 lần đăng nhập sai trong 10 phút trên một tài khoản.
- [ ] Bước 6: Chiều 07/10 để dự phòng.

## Verification
- [ ] Bảng xác nhận của người phụ trách BP-DEV cho từng sản phẩm: `04-bang-chung/EVD-XN-20261001-bang-xac-nhan-san-pham.xlsx` (đã soạn sẵn 01/10, chờ đánh dấu); sau khi đánh dấu, xuất `EVD-XN-…-xac-nhan.csv` gồm sản phẩm, người xác nhận, số câu Đúng/Sai/Không chắc, rồi áp phần Sai vào tài liệu.
- [x] Không còn câu trả lời "chờ" mà không có hạn: sổ khoảng trống 192 mục (sinh lại sau Phase 5) đều có hạn và người phụ trách; Excel 0 lỗi (mỗi CHƯA CÓ / CHƯA XÁC MINH có hạn ngay sau).
- [ ] Có bằng chứng cho kết luận về dữ liệu ra nước ngoài: đã có cho WebPanel / Central, OxMail, công cụ của Bộ phận Kỹ thuật, Design System; còn chatbot iNET Portal chờ câu trả lời 05/10.

## Kết quả 01/10/2026
- Bước 1: soạn sẵn bảng xác nhận 425 câu khẳng định của 17 sản phẩm (215 câu "Cần xem" vì độ tin cậy chưa cao), có danh sách chọn Đúng / Sai / Không chắc, sheet Tổng hợp tự đếm, sheet Câu hỏi gom 14 câu. Công thức kiểm tĩnh (máy không có LibreOffice để tính lại).
- Bước 2: sổ khoảng trống `04-bang-chung/EVD-KT-20261001-so-khoang-trong.csv` sinh từ 23 tài liệu: 183 mục (76 CHƯA XÁC MINH, 82 CHƯA CÓ, 25 MỘT PHẦN), 0 mục thiếu hạn hoặc người phụ trách. Đã thêm cột hạn và người phụ trách cho DEV-BM-09, BM-06 Phần A, QT-09 Phụ lục 10.1. Excel: mỗi dòng CHƯA XÁC MINH ghi người phụ trách xác minh.
- Bước 4: bằng chứng ở `04-bang-chung/EVD-QT10-20261001-du-lieu-ra-dich-vu-nuoc-ngoai.txt`. WebPanel / Central (bản production build từ nhánh không có tính năng), OxMail (worker tắt trong cấu hình production 28/09/2026), công cụ của Bộ phận Kỹ thuật (chưa production), Design System (đã gỡ 01/10) theo nhánh "không gửi"; chatbot iNET Portal chờ trả lời, đã soạn sẵn hai nhánh.
- Phát hiện thêm, đã kê khai: Design System lưu bản sao lưu CSDL ở kho nước ngoài, mirror GitHub, image trên GitHub Container Registry, gói npm công khai; Assets mirror sang kho GitHub cá nhân; Webmail kết nối Google Drive/OneDrive/Dropbox; OxMail kiểm tra URL độc hại; công cụ Bộ phận Kỹ thuật dùng webhook thanh toán SePay. DEV-BM-09 từ 12 lên 19 nhóm dịch vụ; DEV-BM-10 thêm R-DEV-11 (mã nguồn ra kho ngoài GitLab công ty, hạn 31/10/2026) và R-DEV-12 (bản sao lưu ở nước ngoài, hạn 31/12/2026); DEV-QT-04 thêm quy định mirror; DEV-QT-10 thêm dòng bản sao lưu.
- Bước 5: mô hình người chính / dự phòng đã chốt; tên theo sản phẩm và ngưỡng DET chờ trả lời 05/10.
