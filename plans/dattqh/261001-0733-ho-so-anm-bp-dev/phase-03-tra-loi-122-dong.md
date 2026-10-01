---
phase: 3
title: "Trả lời đủ 122 dòng việc vào bản sao Excel"
status: in-progress
priority: P1
effort: "M"
dependencies: [1, 2]
---

# Phase 3: Trả lời đủ 122 dòng việc vào bản sao Excel (05/10 → 07/10)

## Goal
Một bản sao của `05-BP-PHAT-TRIEN-SAN-PHAM-NOI_BO.xlsx`. Trong đó đủ 122 dòng (dòng Excel 5–126) được điền các cột màu
vàng **J–O**, trỏ sang tài liệu DEV và file bằng chứng. File gốc giữ nguyên.

## Files
- Đọc: file gốc ở iCloud `QUY TRINH QUY DINH NOI BO/` (chỉ đọc; kiểm tra lại mtime sau khi chạy).
- Tạo: `BP-DEV-ho-so-2026-10/03-bang-tra-loi/05-BP-PHAT-TRIEN-SAN-PHAM-NOI_BO_tra-loi-BP-DEV.xlsx` (sao file gốc rồi ghi bằng openpyxl, giữ định dạng và data validation).
- Tạo: `BP-DEV-ho-so-2026-10/03-bang-tra-loi/ma-tran-122-dong.csv`, gồm STT → tài liệu DEV → mã EVD → trạng thái. Đây là đầu vào của script kiểm tra ở Phase 5.

## Quy ước điền
| Cột | Nội dung |
|---|---|
| J · Nội dung đơn vị cung cấp | Giá trị cụ thể kèm thời điểm chốt. Nếu chưa có: `CHƯA CÓ — <hiện trạng thật> · Hạn khắc phục: dd/mm/yyyy · Biện pháp tạm thời: …`. Nếu BP-DEV không tự xác minh được: `CHƯA XÁC MINH — <lý do> · Hạn xác minh: 31/10/2026`. |
| K · Nguồn bằng chứng | Mã file EVD và/hoặc tên tài liệu DEV. **Bắt buộc** với 29 dòng có mẫu "Cung cấp tệp hoàn chỉnh hoặc dự thảo…". |
| L · Người được giao | Họ tên người phụ trách (không ghi thành viên outsource; luồng bộ phận khác ghi tên người phụ trách bộ phận đó). |
| M · Hạn hoàn thành | Hạn **điền dòng** ≤ 09/10/2026. Hạn khắc phục ghi trong cột J. |
| N · Trạng thái | Theo danh sách có sẵn. `Hoàn thành`: đã trả lời đủ và có bằng chứng, kể cả khi nội dung là CHƯA CÓ kèm hạn. `Chờ xác nhận`: CHƯA XÁC MINH hoặc chờ đơn vị khác. `Không áp dụng`: kèm lý do ở cột O. Không để `Chưa bắt đầu`. |
| O · Ghi chú | Lý do không áp dụng; ghi chú "chờ đối chiếu tài liệu gốc" khi chưa có bản GOV/CMP/OPS; ghi chú gửi Ban về sai tên đơn vị (dòng ghi "Bộ phận Pháp chế thuộc Phòng Tổng hợp"). |

## Ma trận nhóm dòng (dòng theo STT trong file)
| STT | Mục trong tài liệu gốc | Trả lời bằng | Nguồn |
|---|---|---|---|
| 1–2 | GOV-01 Điều 2: thành phần Ban | Dòng 1 (Trưởng phòng): Ông Vũ Trọng Kiên, Trưởng phòng Nền tảng (đã xác nhận 01/10/2026). Dòng 2 (người phụ trách): Ông Trịnh Quốc Hoàn Đạt, người phụ trách BP-DEV do CEO chỉ định, thành viên Ban (QĐ 159/2026), dattqh@inet.vn; số điện thoại công việc: tổng đài công ty 1900 9250 (theo inet.vn, tra ngày 01/10/2026) | QĐ 159, QĐ 169 |
| 3–7 | GOV-03 5.5, 5.6, Phụ lục A | Runtime theo repo, lộ trình EOL; tài khoản quản trị GitLab; kho bí mật; file khóa trong repo (chỉ số lượng) | BM-02, BM-06, BM-03, QT-05 |
| 8, 14–28 | CMP-04 5.1, 9.2, 11 Sổ HTTT | Số repo chính xác; đối chiếu repo ↔ subdomain; 14 dòng sổ HTTT | BM-01 (đối chiếu subdomain: CHƯA XÁC MINH nếu BP-DEV không có danh sách) |
| 9–11 | CMP-04 HT-07, HT-12, HT-14 | eKYC; xác nhận không lưu dữ liệu thẻ; chatbot có gửi dữ liệu ra ngoài không | BM-09, QT-10, phiếu hiện trạng Portal |
| 12–13 | CMP-04 HT-16 GitLab | Kho bí mật, lịch sử Git; SSO/2FA | EVD-BM06, QT-04, QT-05 |
| 29–34 | CMP-05 15.4, CMP-06 13.c | Kế hoạch nâng cấp, thay thế; kho bí mật; thu hồi khóa; EOL liên quan HT-08 | BM-02, QT-05, QT-06 |
| 35–55 | CMP-06 15 (Đ30 k3), 16 (Đ30 k4) | Từng yêu cầu quản lý và kỹ thuật → quy trình DEV tương ứng, theo ma trận tuân thủ của brainstorm mục 8 | QT-01…QT-10 |
| 56–65 | CMP-06 18, 19 (HT-03) | WHOIS legacy; phương án ANM cho HT-03 | Xác định chủ sở hữu HT-03 trước; không thuộc BP-DEV thì ghi rõ và trỏ sang đơn vị sở hữu |
| 66–75 | CMP-07 11, 23, 25, 28.2 | EOL theo mã HT; sổ rủi ro; ngưỡng phát hiện DET (dòng 73–74 cần quyết định giá trị); dự phòng theo lớp | BM-02, BM-10, QT-07 |
| 76–87 | CMP-08 7.2, 8, 9.1, 12.3 | Danh mục dữ liệu; luồng dữ liệu; dịch vụ bên thứ ba và nơi đặt hạ tầng; dòng 87 trả lời trung tính qua danh mục dịch vụ bên thứ ba | BM-01 Phần C, BM-09, QT-10 |
| 88–96 | OPS-09 | Lộ trình SSO; ngoại lệ xác thực; bảng quyền theo vai trò; kho bí mật | QT-04, BM-06 Phần D, QT-05 |
| 97–105 | OPS-10 12.2 Sổ EOL | Phiên bản chính xác; danh sách giao diện còn dùng thư viện cũ (ghi "không có trong sản phẩm BP-DEV" kèm danh sách repo đã rà) | BM-02 (+ Hạ tầng cho dòng 105) |
| 106–109 | OPS-12 7.1 CSIRT | Vai trò BP-DEV trong đội ứng phó: người chính, người dự phòng | QT-08 |
| 110–114 | OPS-13 | Kho bí mật; kịch bản nghiệm thu sau khôi phục; vai trò khi khôi phục | QT-05, QT-09, BM-08 |
| 115–117 | OPS-15 6.2.4 | Cấu hình bảo mật; kết quả rà file khóa trong repo | QT-07, BM-03 |
| 118–122 | OPS-16 Sổ 7, 12, 13 | Hạn hoàn thành cho rủi ro và EOL; sổ khóa | BM-10, BM-02, BM-03 |

## Tasks & Steps
1. [x] 01/10: tạo bản sao, điền nhóm dữ kiện có sẵn (1–34, 76–87, 97–105, 118–122) từ EVD.
2. [x] 01/10: điền nhóm tham chiếu quy trình (35–75, 88–96, 106–117) từ tài liệu bản 0.9.
3. [x] 01/10: dòng BP-DEV không tự xác minh được ghi `CHƯA XÁC MINH`, trạng thái `Chờ xác nhận`.
4. [x] Sinh `ma-tran-122-dong.csv` từ bản sao để Phase 5 kiểm tra.
- [ ] Điền nốt 22 dòng chờ câu trả lời của người phụ trách BP-DEV (STT 1, 6, 7, 11, 16, 18, 20–24, 26, 55, 62, 65, 73, 74, 87, 90, 106, 107, 122), chạy lại script và kiểm tra.

## Verification
- [x] Script: mở bản sao, với mỗi dòng 5–126 kiểm tra J, K, L, M, N không trống; N thuộc danh sách hợp lệ và ≠ "Chưa bắt đầu"; J chứa "CHƯA" thì phải có mẫu ngày `\d{2}/\d{2}/\d{4}`; 29 dòng "Cung cấp tệp…" có K trỏ tới file tồn tại trong `01-quy-trinh/`, `02-bieu-mau/` hoặc `04-bang-chung/`. Kết quả mong đợi: 0 lỗi.
- [x] `stat` file gốc: mtime vẫn là `Oct 1 11:02` (không bị ghi đè).

## Kết quả 01/10/2026
- Bản sao: `03-bang-tra-loi/05-BP-PHAT-TRIEN-SAN-PHAM-NOI_BO_tra-loi-BP-DEV.xlsx`; ma trận: `03-bang-tra-loi/ma-tran-122-dong.csv`. Danh sách chọn ở cột N còn nguyên.
- Kiểm tra: 0 lỗi trên 122 dòng (J–N không trống, trạng thái hợp lệ, mọi dòng CHƯA có hạn, 29 dòng "Cung cấp tệp…" trỏ tới tệp có thật, không từ cấm, không chuỗi giống bí mật). File gốc giữ nguyên 11:02, 17.676 byte.
- Trạng thái: 56 Hoàn thành, 66 Chờ xác nhận (22 chờ câu trả lời của người phụ trách BP-DEV, hạn 05/10; 44 chờ đơn vị khác hoặc Ban đối chiếu, hạn xác minh 31/10).
- 60 dòng gốc chỉ ghi tên bộ phận: trả lời theo tiêu đề mục, cột O ghi đề nghị Ban đối chiếu với bản gốc GOV/CMP/OPS (BP-DEV chưa có).
- Sửa ngược Phase 2 khi đối chiếu bằng chứng: DEV-BM-02 thêm EOL-08 AngularJS (my.inet.vn, helpdesk.inet.vn, ierp dùng AngularJS; iNET Editor có gói tích hợp) và cập nhật số repo theo 46 project lúc 18:08; DEV-QT-06 sửa dòng AngularJS; DEV-QT-01 sửa câu "iNET Portal tự động lên staging" (thực tế staging thủ công, production do người ngoài BP-DEV phát hành).
- Bằng chứng mới: `EVD-BM01-20261001-1808-danh-sach-project-dang-hoat-dong.csv`, `EVD-BM02-20261001-ra-soat-angularjs.txt`, `EVD-QT10-20261001-ra-soat-ma-nguon-portal-thanh-toan-chatbot.txt`. Dựng lại 2 tệp bằng chứng bị rỗng do lệnh chuẩn hóa ở phiên trước (`EVD-00`, `EVD-BM01-…-thay-doi-kho-gitlab.txt`).
