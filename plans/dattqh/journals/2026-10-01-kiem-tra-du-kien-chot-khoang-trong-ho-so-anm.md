---
title: Kiem tra du kien va chot khoang trong ho so ANM BP-DEV
date: 2026-10-01
summary: "Phase 4: sổ khoảng trống 183 mục đủ hạn; bảng xác nhận 425 câu; kết luận dữ liệu ra nước ngoài cho 4 sản phẩm; kê khai thêm 7 dịch vụ bên ngoài"
---

# Kiem tra du kien va chot khoang trong ho so ANM BP-DEV

## Kết quả
- Sổ khoảng trống tự sinh từ 23 tài liệu: 183 mục, mục nào cũng có hạn và người phụ trách. Muốn đạt được phải thêm cột hạn và người phụ trách cho DEV-BM-09, BM-06 và QT-09 Phụ lục 10.1, vì trước đó 18 mục CHƯA XÁC MINH trong DEV-BM-09 không có hạn.
- Bảng xác nhận 425 câu khẳng định theo 17 sản phẩm, có danh sách chọn và sheet tự đếm, để người phụ trách BP-DEV kiểm.
- Dữ liệu ra nước ngoài: cấu hình triển khai và nhánh phát hành trong repo cho thấy 4 sản phẩm không chạy tính năng xử lý nội dung trên production. Bằng chứng mạnh nhất là inventory production của OxMail ghi tính năng tắt có chủ ý, và lệnh build production của WebPanel / Central checkout nhánh không chứa tính năng. Còn chatbot iNET Portal chưa rõ nơi đặt dịch vụ.

## Phát hiện
- Design System lưu bản sao lưu CSDL ở kho nước ngoài và mirror mã nguồn sang GitHub; Assets mirror sang kho GitHub cá nhân của người phát triển để triển khai staging. Cả hai trước đó không có trong danh mục dịch vụ bên thứ ba. Đã kê khai và thêm rủi ro R-DEV-11, R-DEV-12.

## Giới hạn
- Máy không có LibreOffice nên chưa tính lại công thức của bảng xác nhận; chỉ kiểm tĩnh vùng tham chiếu.

> Historical work record — not durable authority. Prefer docs/specs/ADRs for current decisions.
