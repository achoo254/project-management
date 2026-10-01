---
phase: 2
title: "Viết mô tả công việc hiện tại thành 23 tài liệu bản 0.9"
status: in-progress
priority: P1
effort: "L"
dependencies: [1]
---

# Phase 2: Viết mô tả công việc hiện tại thành 23 tài liệu bản 0.9 (02/10 → 17:00 05/10)

## Goal
Mỗi DEV-QT trả lời trước hết câu hỏi **"BP-DEV đang làm việc này thế nào"**, bằng cách làm thật, viết theo phiếu hiện trạng
và bằng chứng của Phase 1. Sau đó mới ghi yêu cầu chuẩn (TCVN 14423 cấp độ 3, NĐ 331) và khoảng cách còn thiếu. Mỗi DEV-BM
được điền dữ liệu thật từ EVD.

## Nguyên tắc viết (bắt buộc cho từng tài liệu)
- **Mục 6 "Nội dung quy trình" = cách làm hiện tại.** Không có thì ghi thẳng "Hiện chưa thực hiện", không viết bước giả.
- Yêu cầu chuẩn mà hiện chưa làm thì chỉ đưa vào **mục 8 "Hiện trạng áp dụng và kế hoạch khắc phục"**: CHƯA CÓ / CHƯA XÁC MINH + hạn + người phụ trách + biện pháp tạm thời.
- Căn cứ ghi tới điều khoản: `TCVN 14423:2026 5.x.2.y` → Luật → NĐ → (TT nếu có) → ISO 27001 A.x.
- Khối kiểm soát: mã, lần 0.9, ngày hiệu lực, rà soát kế tiếp, bảng ký (người phê duyệt để trống).
- Không dùng từ cấm (quy tắc 3 trong plan.md); mã nguồn của mọi luồng đều "phải được review".

## Files to Create (iCloud `BP-DEV-ho-so-2026-10/`)
- `00-nguon/DEV-QT-01..10.html`, `00-nguon/DEV-BM-01..13.html`: bản nguồn, dựng từ cấu trúc của mock.
- `01-quy-trinh/DEV-QT-xx_<ten>_v0.9_20261009.docx` (10 file) và `02-bieu-mau/DEV-BM-xx_<ten>_v0.9_20261009.docx` hoặc `.xlsx` cho các sổ dạng bảng (13 file). Chuyển đổi bằng skill `anthropic-skills:docx` / `anthropic-skills:xlsx` sau khi chốt định dạng.

## Thứ tự soạn và nguồn dữ kiện
| Thứ tự | Tài liệu | Mô tả hiện tại lấy từ | Bổ sung theo TCVN (theo bảng quyết định trong brainstorm) | Người xác nhận |
|---|---|---|---|---|
| 1 | QT-03 Thay đổi, phát hành, CI/CD | EVD-QT03 (CI, nhánh bảo vệ, duyệt MR), phiếu mục Phát hành | Vá thư viện có đánh giá tác động | dattqh |
| 2 | QT-08 Xử lý sự cố | Phiếu mục Sự cố, sự cố thật gần nhất | Người chính và người dự phòng, danh bạ hằng năm, diễn tập | dattqh |
| 3 | QT-01 Phát triển an toàn + Phụ lục 3 luồng | Phiếu mục Phát triển; danh sách project ngoài BP-DEV | Điều khoản chung cho phần mềm do đơn vị ngoài công ty phát triển (5.17.2.1c); luồng dữ liệu ở giai đoạn thiết kế | dattqh |
| 4 | QT-04 Mã nguồn, GitLab, API quản trị | EVD-BM06, EVD-QT03 | Mật khẩu 8/14 ký tự, MFA quản trị, vô hiệu sau 45 ngày, rà 6 tháng | dattqh |
| 5 | QT-05 Bí mật, khóa, chứng thư | EVD-BM03 (chỉ đếm) | Mã hóa khi lưu và khi truyền, nguyên vẹn, chữ ký số | dattqh |
| 6 | QT-06 Lỗ hổng, phụ thuộc, EOL + Phụ lục kiểm thử xâm nhập | EVD-BM02, kết quả quét 01/10 | Rà 6 tháng/lần, kênh nhận báo cáo lỗ hổng từ bên ngoài | dattqh |
| 7 | QT-07 Vận hành, giám sát | Phiếu mục Vận hành | Log ≥ 3 tháng, rà 6 tháng, cấu hình chuẩn, tách cổng quản trị | dattqh |
| 8 | QT-09 Sao lưu, khôi phục | Phiếu mục Sao lưu | 3-2-1, tự động, khôi phục thử | dattqh |
| 9 | QT-10 Dữ liệu cá nhân, bên thứ ba | EVD-BM09; trạng thái production đã xác minh | Không đưa dữ liệu lấy qua API sang dịch vụ ngoài; thời hạn lưu; tự thu thập màn hình chỉ khi người dùng chọn | dattqh |
| 10 | QT-02 Lập trình an toàn | Phiếu mục Bảo mật | Khóa phiên 5/15 phút, khóa sau nhiều lần đăng nhập sai, SECURITY.md | dattqh |
| 11 | BM-01…BM-13 | EVD tương ứng | BM-02 mở rộng thành sổ thành phần phần mềm; BM-06 thêm ma trận quyền theo chức danh; BM-10 thêm cột rủi ro; **BM-13 mới** (kiểm thử xâm nhập) | dattqh |

## Tasks & Steps
1. [ ] 02/10 chiều: dựng 23 file nguồn từ mock, thay "[Họ tên]" bằng người phụ trách (mặc định người phụ trách BP-DEV cho mọi sản phẩm trong phiếu). Người phê duyệt để trống.
2. [ ] 03–04/10 (cuối tuần, dự phòng): điền mục 6 và mục 8 từ EVD đã có. Mục nào chờ phiếu hiện trạng thì đánh dấu `[CHỜ PHIẾU]`.
3. [ ] 05/10: ghép phiếu hiện trạng vào mục 6; xóa hết `[CHỜ PHIẾU]`. Sản phẩm nào phiếu chưa trả lời thì mô tả theo EVD và ghi "CHƯA XÁC MINH với người phụ trách" ở mục 8.
4. [ ] 05/10 17:00: xuất bản 0.9 sang định dạng nộp.

## Verification
- [x] 23/23 tài liệu tồn tại ở định dạng nộp (.docx).
- [ ] `grep -c "\[CHỜ PHIẾU\]\|\[Họ tên\]"` trên toàn bộ `00-nguon/` bằng 0. Riêng ô người phê duyệt được để trống.
- [ ] Mục 6 của mỗi DEV-QT có ít nhất một ví dụ thật (MR, pipeline, sự cố, lần deploy) kèm mã EVD.
- [ ] Mỗi dòng ở mục 8 có đủ 4 trường: hiện trạng, bằng chứng, hạn, người phụ trách.

## Rủi ro
- Phiếu hiện trạng về muộn: chặn bởi bước 3; không để mục 6 trống.
- Viết theo "nên làm" thay vì "đang làm": rà lại ở Phase 5 bằng câu hỏi "có bằng chứng cho câu này không?".

## Kết quả thực hiện (01/10/2026)
- [x] Bộ chuyển `html2docx.py` (khối tiêu đề, bảng ký — ô người phê duyệt để trống, lịch sử thay đổi, chân trang) và bản ghi quy tắc dùng chung.
- [x] 23 nguồn HTML ở `00-nguon/`, 23 file .docx ở `01-quy-trinh/` (10) và `02-bieu-mau/` (13). Sổ bảng rộng (BM-01, 02, 03, 04, 05, 06, 09, 10) dùng khổ ngang.
- [x] Kiểm tra tự động trên 23 file: 0 từ cấm, 0 chuỗi giống bí mật, 0 dòng mục 8 thiếu hạn, 23/23 ô người phê duyệt trống.
- [x] Biểu mẫu điền dữ liệu thật từ GitLab: BM-01 (17 sản phẩm + GitLab; repo cần phân loại; thay đổi sau chụp), BM-02 (EOL: Node 20 ở 5 repo, Node 18 ở 2, engines ≥16 ở 5, Go cũ ở 2), BM-03 (theo loại, không giá trị/đường dẫn), BM-06 (số tài khoản quyền cao), BM-09 (9 nhóm dịch vụ bên thứ ba), BM-10 (10 rủi ro).
- [x] Thống nhất hạn: quét bí mật 31/10/2026; quét thư viện và SAST 31/12/2026 (đã tách trong QT-03 cho khớp QT-05, BM-10).
- [x] Tự điền từ bằng chứng (01/10, chỉ đọc mã nguồn, CI, tài liệu repo, issue/MR của 17 sản phẩm): ô `[CHỜ PHIẾU]` giảm từ 218 xuống 40; phiếu hiện trạng điền sẵn kèm độ tin cậy và nguồn. Việc BP-DEV không tự biết (hợp đồng, hạ tầng Bộ phận Kỹ thuật) ghi CHƯA XÁC MINH theo quy tắc.
- [ ] 40 ô còn lại thuộc 10 nhóm câu hỏi chỉ người phụ trách BP-DEV trả lời được (tên người phụ trách/hỗ trợ, kênh duyệt với CEO, token API quản trị, ma trận quyền…) — điền rồi xuất lại .docx.
- Giới hạn kiểm tra: máy không có LibreOffice nên chưa dựng ảnh trang để xem bố cục; đã kiểm tra bằng đọc lại cấu trúc file.
