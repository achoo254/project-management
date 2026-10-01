---
title: Ra soat doc lap va sua ho so ANM BP-DEV
date: 2026-10-01
summary: "Phase 5: 4 người rà độc lập ra 126 phát hiện; sửa hết theo câu chuẩn dùng chung; kiểm tra tự động 0 lỗi"
---

# Ra soat doc lap va sua ho so ANM BP-DEV

## Kết quả
- Kiểm tra tự động (chỉ đọc) cho 23 tài liệu, nguồn HTML, phiếu và 122 dòng Excel: 0 lỗi sau sửa. Bộ phát hiện đã thử bằng chuỗi giả.
- Rà độc lập "có bằng chứng cho câu này không" bằng 4 người rà tách theo nhóm tài liệu: 126 phát hiện.

## Bài học
- Khối chữ chèn sẵn dùng chung (log, đăng nhập, sao lưu, review) nhân một lỗi ra nhiều tài liệu. Sửa bằng một bộ câu chuẩn dùng chung cho mọi người sửa thì các tài liệu nói giống nhau.
- Mô tả "cách đang làm" dễ trượt sang mô tả quy trình mong muốn (ví dụ "review theo thói quen", "rà tay khi review MR" khi thực tế gần như không có MR). Biện pháp tạm thời chưa có bằng chứng phải viết thành việc sẽ làm.
- Cột đếm trong kết xuất phải hiểu đúng nghĩa: `manual_gate_count` đếm mọi job thủ công, không phải bước duyệt production.
- Số liệu không truy được về tệp bằng chứng (đợt "quét 20 repo") phải thay bằng phép đo lặp lại được và lưu thành EVD.
- Hạn hỗ trợ phiên bản (Go) phải tra nguồn chính thức: Go 1.27 ra 19/08/2026 nên 1.25 đã hết hỗ trợ.

> Historical work record — not durable authority. Prefer docs/specs/ADRs for current decisions.
