---
phase: 5
title: "Rà soát chéo và đóng băng nội dung"
status: in-progress
priority: P1
effort: "S"
dependencies: [2, 3, 4]
---

# Phase 5: Rà soát chéo và đóng băng nội dung (thứ Năm 08/10, đóng băng lúc 17:00)

## Goal
Bộ hồ sơ qua được kiểm tra tự động và rà chéo của người thứ hai. Sau 17:00 08/10 chỉ được sửa lỗi chính tả hoặc định dạng.

## Tasks & Steps
1. [ ] **Kiểm tra tự động** (script Python chỉ đọc, lưu ở scratchpad), chạy trên `00-nguon/`, `01-quy-trinh/`, `02-bieu-mau/`, `03-bang-tra-loi/`:
   - Độ phủ: kiểm tra 122 dòng như ở Phase 3; 23 tài liệu đều có khối kiểm soát, mục 8, mục 9.
   - Từ cấm, so theo nguyên từ. `AI` so **phân biệt hoa thường**, để không bắt nhầm chữ "ai" (nghĩa là "người nào"); các từ còn lại không phân biệt hoa thường: `AI`, `trí tuệ nhân tạo`, `vibe`, `MCP`, `OpenAI`, `Anthropic`, `Gemini`, `Groq`, `CTO`, `BP Công Nghệ`, `Pháp chế`, `outsource`.
   - Chuỗi giống bí mật: `glpat-`, `sk-…`, `BEGIN … PRIVATE KEY`, `password=`, chuỗi base64 dài ≥ 40 ký tự trong ô bảng.
   - Mọi `CHƯA CÓ` / `CHƯA XÁC MINH` có ngày `dd/mm/yyyy` và tên người phụ trách.
   - Mọi mã `EVD-…` được nhắc đến đều tồn tại trong `04-bang-chung/`.
2. [ ] **Rà chéo** (người rà khác người soạn): hobv rà QT-01, 02, 03; ducnd rà QT-04, 05, 06; chuongdt rà QT-07, 08, 09, 10; dattqh rà toàn bộ BM và bản sao Excel. Câu hỏi duy nhất cho mỗi câu khẳng định: "Có bằng chứng cho câu này không?"
3. [ ] Sửa lỗi, chạy lại script đến khi 0 lỗi.
4. [ ] 17:00: khóa bản. Ghi ngày rà soát vào bảng lịch sử thay đổi của mỗi tài liệu.

## Verification
- [x] Kết quả script (chạy 01/10/2026 19:32) lưu ở `04-bang-chung/EVD-QA-20261001-kiem-tra-tu-dong.txt`: 0 lỗi độ phủ, 0 từ cấm, 0 chuỗi giống bí mật, 0 mã EVD treo. Chạy lại bằng `FREEZE=1` lúc khóa bản 08/10 và lưu thành `EVD-QA-20261008-…`.
- [ ] Mỗi tài liệu có tên người rà chéo trong lịch sử thay đổi (ghi vào `99-cong-cu-noi-bo/phase5/reviewers.json`, bộ chuyển .docx tự thêm dòng "Rà soát chéo"; chế độ `FREEZE=1` báo lỗi nếu thiếu).

## Kết quả 01/10/2026
- Bước 1: script `qa_check.py` (chỉ đọc) kiểm 23 .docx, 23 nguồn HTML, phiếu hiện trạng và 122 dòng Excel; đã thử bộ phát hiện bằng chuỗi giả (bắt đủ 5 dạng bí mật, AI viết hoa, mã EVD treo; không bắt nhầm chữ "ai", đường dẫn, mã băm). Kết quả cuối: 0 lỗi.
- Bước 2 (phần tự động): 4 người rà độc lập, mỗi người một nhóm tài liệu, chỉ đọc, hỏi "Có bằng chứng cho câu này không?" — 126 phát hiện (QT-01…03: 32, QT-04…06: 23, QT-07…10: 30, BM và Excel: 41). Các lỗi nặng: "review theo thói quen" trái bằng chứng (16/17 sản phẩm commit thẳng hoặc tự merge); 3 → 5 project chưa bảo vệ nhánh; "3 project có bước duyệt production" → chỉ OxMail; số liệu "quét 20 repo" không có bằng chứng; ô triển khai production của OneDash mô tả staging; Go 1.25 đã hết hỗ trợ (Go 1.27 phát hành 19/08/2026).
- Bước 3: sửa toàn bộ theo `99-cong-cu-noi-bo/phase5/FIX-BRIEF.md` (câu chuẩn dùng chung), 3 người sửa song song QT theo nhóm tệp, người điều phối sửa bộ sinh BM và Excel. Kê khai thêm: tunnel Imapsync qua máy ngoài hạ tầng iNET, điểm nhận trace của iNET Portal, phạm vi dữ liệu thật của Telegram, ngoại lệ máy dev nối tới dữ liệu production (Webmail, Design System, Công cụ nội bộ), 2 repo tài liệu. Bằng chứng mới: `EVD-QT01-20261001-ket-qua-ra-soat-ma-nguon-17-san-pham.csv`, `EVD-QT02-20261001-1910-readme-security-test-repo-san-pham.csv`. Sau sửa: kiểm tra tự động 0 lỗi, sổ khoảng trống 192 mục 0 lỗi, Excel 0 lỗi.
- Còn lại: rà chéo của người thật (hobv QT-01…03, ducnd QT-04…06, chuongdt QT-07…10, dattqh BM + Excel) và khóa bản 17:00 08/10 sau khi có câu trả lời 05/10.
