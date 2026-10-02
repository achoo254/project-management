---
title: "Hồ sơ an ninh mạng BP-DEV — nộp trước 17:00 09/10/2026"
description: "Mô tả đúng công việc hiện tại của BP-DEV (phát triển, vận hành, sự cố, bảo mật) thành 10 quy trình + 13 biểu mẫu bản 0.9 và trả lời đủ 122 dòng việc của Ban ATANM & BVDL, kèm bằng chứng, trước hạn."
status: in-progress
priority: P1
effort: "L (6 phase; tier theo ai-collaboration-workflow, không ước giờ)"
tags: [an-ninh-mang, ho-so, tcvn-14423, nd-331, bp-dev]
blockedBy: []
blocks: []
created: 2026-10-01
---

# Hồ sơ an ninh mạng BP-DEV — nộp trước 17:00 thứ Sáu 09/10/2026

## Overview

Ban ATANM & BVDL (QĐ 159/2026/QĐ-iNET) giao BP-DEV 122 dòng việc trong `05-BP-PHAT-TRIEN-SAN-PHAM-NOI_BO.xlsx`
(iCloud, **chỉ đọc**). Trọng tâm đợt này: **mô tả đúng công việc BP-DEV đang làm thật**, gồm phát triển, phát hành,
vận hành, xử lý sự cố và bảo mật sản phẩm. Phần chưa làm hoặc chưa đạt chuẩn ghi "CHƯA CÓ / CHƯA XÁC MINH", luôn kèm
hạn khắc phục và người phụ trách.

Kế thừa (không làm lại):
- Contract và căn cứ pháp lý: [brainstorm](../reports/brainstorm-261001-1108-khung-ho-so-anm-bp-dev.html)
- Cấu trúc 23 tài liệu: [mock](../reports/mock-261001-1121-quy-trinh-bieu-mau-anm-bp-dev.html)
- Đối chiếu TCVN 14423:2026 cấp độ 3: [mapping](../reports/tcvn14423-cap3-doi-chieu-bo-dev-261001.md)
- Quyết định chọn hướng cho từng mục bổ sung và lịch đã chỉnh: brainstorm, mục 5 (bảng "Quyết định theo thời gian còn lại")

## Quy tắc bất biến

1. Không mô tả việc chưa làm như thể đã làm. Mỗi số liệu phải có file bằng chứng `EVD-…` và thời điểm chốt.
2. Không ghi giá trị bí mật (mật khẩu, token, khóa). Sổ khóa chỉ ghi mã định danh.
3. Không nhắc AI, công cụ sinh mã, MCP trong mọi tài liệu nộp. Rủi ro dữ liệu ra ngoài viết theo quy định chung về dịch vụ bên thứ ba.
4. Tên tổ chức: dùng đúng QĐ 169/2026 và QĐ 159/2026; không viết "BP Công Nghệ", "CTO", "Pháp chế"; không nêu tên thành viên outsource.
5. Người phê duyệt để trống cho tới khi được chốt.
6. File Excel gốc không bị sửa. Câu trả lời ghi vào bản sao.
7. Bộ nộp và bằng chứng lưu ở iCloud, cạnh file Excel (`QUY TRINH QUY DINH NOI BO/BP-DEV-ho-so-2026-10/`), **không commit vào git**, vì có thông tin lỗ hổng.

## Phases

| # | Phase | Ngày | Tier | Status |
|---|-------|------|------|--------|
| 1 | [Thu hiện trạng thực tế](./phase-01-thu-hien-trang-thuc-te.md) | 01–02/10 | M | In progress (chỉ còn chờ câu trả lời phiếu, 05/10) |
| 2 | [Viết mô tả công việc hiện tại thành 23 tài liệu bản 0.9](./phase-02-mo-ta-cong-viec-hien-tai.md) | 02–05/10 | L | In progress (23 tài liệu bản 0.9 đã xuất; còn 35 ô chờ phiếu và mã EVD ở mục 6 của 4 QT) |
| 3 | [Trả lời đủ 122 dòng việc vào bản sao Excel](./phase-03-tra-loi-122-dong.md) | 05–07/10 | M | In progress (01/10: 122/122 dòng đã điền, 22 dòng chờ trả lời) |
| 4 | [Kiểm tra dữ kiện và chốt khoảng trống](./phase-04-kiem-tra-du-kien-chot-khoang-trong.md) | 06–07/10 | S | In progress (01/10: khoảng trống đã chốt hạn; chờ xác nhận sản phẩm và chatbot Portal) |
| 5 | [Rà soát chéo và đóng băng nội dung](./phase-05-ra-soat-cheo-dong-bang.md) | 08/10, 17:00 | S | In progress (01/10: kiểm tra tự động và rà độc lập xong, 0 lỗi; chờ rà chéo người thật và khóa bản) |
| 6 | [Ký và nộp](./phase-06-ky-va-nop.md) | 09/10, trước 17:00 | S | In progress (01/10: gói nộp, thư gửi, sổ theo dõi đã chuẩn bị, chạy thử 0 lỗi; chưa gửi) |

Phụ thuộc: 1 → 2 → 3. Phase 4 chạy song song phần cuối của 2 và 3. Sau đó 5 → 6.

## Success Criteria

- [ ] 122/122 dòng của bản sao Excel có nội dung ở các cột màu vàng (J–N). Mọi dòng CHƯA CÓ / CHƯA XÁC MINH có hạn dạng dd/mm/yyyy và tên người phụ trách.
- [ ] 10 DEV-QT và 13 DEV-BM bản 0.9: có khối kiểm soát, căn cứ ghi tới điều khoản TCVN 14423, mục "Hiện trạng áp dụng" và mục "Rà soát và cập nhật".
- [ ] Mục 6 (nội dung quy trình) của mỗi DEV-QT mô tả cách BP-DEV đang làm thật, được người phụ trách BP-DEV xác nhận (người trả lời phiếu cho toàn bộ sản phẩm).
- [ ] Mọi số liệu (số repo, tài khoản quản trị, phiên bản runtime, số pipeline có quét) có file EVD và ngày chốt.
- [ ] Script kiểm tra ở Phase 5 trả về 0 lỗi: thiếu ô, thiếu hạn, từ cấm, chuỗi giống bí mật.
- [ ] Nộp cho Ban ATANM & BVDL trước 17:00 09/10/2026 và có xác nhận đã nhận.

## Rủi ro chính

| Rủi ro | Cách xử lý |
|---|---|
| Khối lượng soạn tài liệu (đánh giá khả thi: rủi ro số 1) | Soạn trước từ mock và dữ kiện GitLab; người phụ trách BP-DEV chỉ kiểm tra dữ kiện. Phase 2 bắt đầu ngay ngày 02/10, song song với Phase 1. |
| Khai sai về dữ liệu ra dịch vụ nước ngoài | Phase 1 xác minh trạng thái thật trên production. Phase 4 quyết: tắt trước khi nộp, hoặc khai đúng. |
| Thiếu tài liệu gốc GOV/CMP/OPS nên khoảng 60 dòng chỉ ghi chung "BP-DEV" | Không gửi yêu cầu ra ngoài (quyết định 01/10): trả lời theo tiêu đề mục và tài liệu DEV tương ứng, ghi chú "chờ đối chiếu tài liệu gốc". |

## Quyết định đã chốt (01/10/2026)

- Định dạng nộp: **.docx** cho quy trình và biểu mẫu dạng văn bản; các sổ dạng bảng có thể dùng .xlsx; bảng trả lời là bản sao .xlsx.
- Tên đơn vị: **Phòng Nền tảng**, gồm Bộ phận Kỹ thuật và Bộ phận Phát triển sản phẩm (BP-DEV). Trưởng phòng Nền tảng chịu trách nhiệm cao nhất về quản trị GitLab; CEO chịu trách nhiệm quy trình triển khai production.

- Không gửi yêu cầu ra ngoài BP-DEV: BP-DEV tự mô tả đúng việc đang làm; việc không tự xác minh được ghi CHƯA XÁC MINH kèm hạn.
- Môi trường (thực tế đang làm): **dev** chỉ người đang làm xem được; **staging** thử nghiệm nội bộ, không có dữ liệu khách hàng; **production** là nơi duy nhất có dữ liệu khách hàng.

## Câu hỏi còn mở

Còn 16 câu chỉ người phụ trách BP-DEV trả lời được, hạn 17:00 05/10/2026 (tự điền từ bằng chứng 01/10 đã giảm ô chờ phiếu từ 218 xuống 35):

1. Người hỗ trợ khi vắng cho 8 sản phẩm (Super Admin Dashboard, công cụ nội bộ, Developers, OneOffice, Design System, Assets, Sàn tên miền, iNET Editor), hoặc chấp nhận ghi chung "thành viên BP-DEV khác do người phụ trách BP-DEV phân công".
2. WebPanel/Central và OnePanel: tên miền production, người phụ trách, người hỗ trợ.
3. OxMail, Imapsync, công cụ Bộ phận Kỹ thuật: người phụ trách, người hỗ trợ.
4. Hình thức báo CEO và CEO duyệt production, nơi lưu bản ghi duyệt.
5. Sản phẩm có API quản trị: ai giữ token, phạm vi, hạn dùng, nơi lưu.
6. Ma trận quyền: người phụ trách sản phẩm và thành viên BP-DEV với trang quản trị, CSDL production, dữ liệu khách hàng.
7. Thu hồi quyền quản trị sản phẩm (ngoài GitLab) có được ghi lại không.
8. Đã từng nhận báo cáo lỗ hổng từ bên ngoài chưa, qua kênh nào.
9. Ai triển khai production cho Assets và iNET Portal (tài liệu repo ghi người ngoài BP-DEV phát hành).
10. Tính năng gửi nội dung ra dịch vụ đặt ở nước ngoài (WebPanel/Central, OxMail, goclaw) đã chạy trên production chưa.
11. Email công vụ của Trưởng phòng Nền tảng (Excel dòng 1).
12. Chatbot iNET Portal gửi tin nhắn, ảnh của khách tới dịch vụ trả lời tự động đặt ở đâu (nội bộ iNET hay bên ngoài, trong hay ngoài nước).
13. Chốt ngưỡng phát hiện đề xuất: DET-01 lỗi 5xx > 5% trong 5 phút; DET-02 > 20 lần đăng nhập sai/tài khoản trong 10 phút.
14. Đồng ý hạn khắc phục mirror mã nguồn ra GitHub (Assets kho cá nhân, Design System) 31/10/2026 và bản sao lưu Design System ở kho nước ngoài 31/12/2026?
15. Dòng "Tách môi trường dev / staging / production": giữ ĐÃ CÓ theo xác nhận (kèm ngoại lệ máy dev nối dữ liệu production của Webmail, Design System, Công cụ nội bộ, hạn 31/10/2026) hay đổi MỘT PHẦN?
16. Ảnh chụp màn hình phản hồi OneDash đang tự chụp, người dùng bỏ chọn được, trong khi nguyên tắc DEV-QT-10 §6.4 là "chỉ đính kèm khi người dùng chủ động chọn": đổi trạng thái dòng này sang MỘT PHẦN (kèm hạn) hay nới nguyên tắc?

Mô hình trách nhiệm (xác nhận 01/10/2026): mỗi sản phẩm có **người phụ trách sản phẩm** tự triển khai, xử lý sự cố và báo thẳng CEO, không qua người phụ trách BP-DEV. Người phụ trách BP-DEV chỉ hỗ trợ, quản lý công việc khi cần, đồng thời phụ trách OneDash và OneMail. Người phụ trách sản phẩm vắng mặt thì thành viên khác của BP-DEV hỗ trợ. **CEO** chịu trách nhiệm cuối cùng về triển khai production (CEO hoặc người được CEO ủy quyền duyệt). Phiếu hiện trạng thu thêm tên người phụ trách và người hỗ trợ cho từng sản phẩm.

<!-- slug: ho-so-anm-bp-dev -->
