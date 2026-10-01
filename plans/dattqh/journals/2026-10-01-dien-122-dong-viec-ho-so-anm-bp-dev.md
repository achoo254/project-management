---
title: Điền 122 dòng việc hồ sơ ANM BP-DEV
date: 2026-10-01
summary: "Phase 3: bản sao Excel 122/122 dòng, 0 lỗi kiểm tra; phát hiện và sửa 2 sai lệch trong tài liệu bản 0.9"
---

# Điền 122 dòng việc hồ sơ ANM BP-DEV

## Kết quả
- Bản sao `05-BP-PHAT-TRIEN-SAN-PHAM-NOI_BO_tra-loi-BP-DEV.xlsx` (iCloud, `03-bang-tra-loi/`): 122/122 dòng có J–O; 56 Hoàn thành, 66 Chờ xác nhận (22 chờ người phụ trách BP-DEV trả lời, 44 chờ đơn vị khác hoặc Ban đối chiếu). Script kiểm tra 0 lỗi; file gốc không đổi.
- 60 dòng gốc chỉ ghi tên bộ phận, không có tài liệu gốc GOV/CMP/OPS: trả lời theo tiêu đề mục, ghi đề nghị Ban đối chiếu ở cột O.

## Phát hiện khi đối chiếu bằng chứng
- Tài liệu bản 0.9 ghi "không có AngularJS" là chưa đúng đủ: iNET Editor có gói tích hợp AngularJS 1.x để nhúng vào my.inet.vn, helpdesk.inet.vn, ierp (ba hệ thống dùng AngularJS, ngoài BP-DEV). Đã thêm EOL-08 vào DEV-BM-02 và sửa DEV-QT-06.
- DEV-QT-01 ghi iNET Portal tự động lên staging; thực tế staging thủ công, production do người ngoài BP-DEV phát hành. Đã sửa.
- iNET Portal không lưu dữ liệu thẻ (chỉ gọi API backend, cổng VNPay); chatbot Portal gửi tin của khách tới dịch vụ trả lời tự động chưa rõ nơi đặt.

## Sự cố trong quá trình làm
- Hai tệp bằng chứng `.txt` bị rỗng do một lệnh chuẩn hóa ở phiên trước mở tệp ở chế độ ghi trước khi đọc (`open(p,'w').write(f(open(p).read()))`). Đã dựng lại từ nội dung gốc. Bài học: đọc vào biến trước, rồi mới mở để ghi.

> Historical work record — not durable authority. Prefer docs/specs/ADRs for current decisions.
