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
| 1 | [Thu hiện trạng thực tế](./phase-01-thu-hien-trang-thuc-te.md) | 01–02/10 | M | Completed (02/10: bỏ câu hỏi theo từng sản phẩm, người phụ trách sản phẩm tự rà soát; đối chiếu lại mã nguồn mới nhất) |
| 2 | [Viết mô tả công việc hiện tại thành 23 tài liệu bản 0.9](./phase-02-mo-ta-cong-viec-hien-tai.md) | 02–05/10 | L | Completed (02/10: 0 ô chờ phiếu, tên người thay bằng vai trò, quy định dữ liệu khách chỉ gửi hạ tầng nội bộ + danh mục ngoại lệ) |
| 3 | [Trả lời đủ 122 dòng việc vào bản sao Excel](./phase-03-tra-loi-122-dong.md) | 05–07/10 | M | Completed (02/10: 122/122 dòng, 0 dòng chờ trả lời; 76 Hoàn thành, 46 Chờ xác nhận đều có hạn 31/10/2026) |
| 4 | [Kiểm tra dữ kiện và chốt khoảng trống](./phase-04-kiem-tra-du-kien-chot-khoang-trong.md) | 06–07/10 | S | Completed (02/10: sổ khoảng trống 199 mục, 0 lỗi; khoảng trống giao Người phụ trách sản phẩm) |
| 5 | [Rà soát chéo và đóng băng nội dung](./phase-05-ra-soat-cheo-dong-bang.md) | 08/10, 17:00 | S | In progress (02/10: kiểm tra tự động 0 lỗi; phân công rà chéo đã duyệt; chờ rà chéo và khóa bản 17:00 08/10) |
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
- (02/10) **Quy trình và biểu mẫu áp dụng chung cho mọi sản phẩm; người phụ trách sản phẩm tự chịu trách nhiệm làm đúng.** Không hỏi lần lượt từng người phụ trách về hiện trạng sản phẩm của họ. Khoảng trống phát hiện từ mã nguồn (bằng chứng `EVD-KT-20261002-doi-chieu-ma-nguon-moi-nhat-*.txt`) ghi đúng hiện trạng vào bảng khoảng trống, giao người phụ trách sản phẩm tự rà soát và khắc phục trước hạn chung; không đưa vào câu hỏi của hồ sơ. Ô phiếu hiện trạng còn trống ghi "Người phụ trách sản phẩm tự rà soát và cập nhật theo DEV-QT tương ứng" kèm hạn. Dòng nào bằng chứng cho thấy chưa đạt (vd tách môi trường, ảnh chụp phản hồi OneDash) ghi MỘT PHẦN, không ghi ĐÃ CÓ.
- Môi trường (thực tế đang làm): **dev** chỉ người đang làm xem được; **staging** thử nghiệm nội bộ, không có dữ liệu khách hàng; **production** là nơi duy nhất có dữ liệu khách hàng.

## Trả lời 6 câu cấp hệ thống (chốt 02/10/2026)

1. Danh sách người phụ trách 17 sản phẩm: đồng ý theo đề xuất. **Không ghi tên người trực tiếp vào quy trình, biểu mẫu, quy định**: chỉ dùng vai trò (Người phụ trách sản phẩm, Người phụ trách BP-DEV, Trưởng phòng Nền tảng, CEO). Bảng ánh xạ sản phẩm → người chỉ nằm ở tài liệu nội bộ không nộp. Ngoại lệ: dòng 1 và dòng 2 bảng trả lời Excel (liên hệ Trưởng phòng Nền tảng và Người phụ trách BP-DEV). Dữ liệu khách chỉ gửi hạ tầng nội bộ, trừ danh mục ngoại lệ được duyệt (cổng thanh toán, CDN/DNS, Zalo OA, thông báo đẩy) do CEO duyệt trên my.inet.vn (DEV-QT-10 mục 6.7).
2. Hạn chung để người phụ trách sản phẩm tự rà soát và đưa sản phẩm về đúng quy trình: **31/10/2026**. Quy định chuẩn: **dữ liệu khách hàng chỉ gửi tới dịch vụ trên hạ tầng nội bộ iNET**; tài liệu không nhắc tới việc gửi ra nước ngoài. Sản phẩm chưa tuân thủ: ghi đúng hiện trạng, Người phụ trách sản phẩm xử lý lại trước hạn chung.
3. Báo triển khai production qua **my.inet.vn** (hệ thống quản trị nội bộ: lưu trữ, quản lý ticket, yêu cầu deploy). Luồng thật (xác nhận 11:12 02/10): "Deploy" trên my.inet.vn chỉ tạo yêu cầu và gửi thông báo tới CEO qua Telegram; CEO tự triển khai production thủ công trên hệ thống runner riêng. Chưa có màn hình quản lý triển khai production; bản ghi duyệt và bản ghi triển khai production chưa lưu tập trung (CHƯA CÓ, hạn 31/10/2026).
4. Kênh chung nhận báo cáo lỗ hổng từ bên ngoài: **my.inet.vn**.
5. Ngưỡng phát hiện chung: DET-01 lỗi 5xx > 5% trong 5 phút; DET-02 > 20 lần đăng nhập sai/tài khoản trong 10 phút.
6. Email Trưởng phòng Nền tảng (Excel dòng 1): kienvt@inet.vn.

Còn mở: BP-DEV đã từng nhận báo cáo lỗ hổng từ bên ngoài chưa (chưa trả lời; nếu dòng Excel bắt buộc thì ghi CHƯA XÁC MINH kèm hạn).

Mô hình trách nhiệm (xác nhận 01/10/2026): mỗi sản phẩm có **người phụ trách sản phẩm** tự triển khai, xử lý sự cố và báo thẳng CEO, không qua người phụ trách BP-DEV. Người phụ trách BP-DEV chỉ hỗ trợ, quản lý công việc khi cần, đồng thời phụ trách OneDash và OneMail. Người phụ trách sản phẩm vắng mặt thì thành viên khác của BP-DEV hỗ trợ. **CEO** chịu trách nhiệm cuối cùng về triển khai production (CEO hoặc người được CEO ủy quyền duyệt). Tên người cụ thể không ghi vào tài liệu nộp (quyết định 02/10).

<!-- slug: ho-so-anm-bp-dev -->
