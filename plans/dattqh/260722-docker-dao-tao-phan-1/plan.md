# Plan — Tài liệu đào tạo Docker (Phần 1) + Labs & Bài tập

**Trạng thái:** ✅ hoàn thành
**Ngày:** 2026-07-22
**Người thực hiện:** dattqh (AI-driven)
**Deliverable:** `dao-tao/22-07-2026/docker-phan-1-nen-tang.html` (1521 dòng, ~131KB, self-contained) — đã verify render trực quan qua Chrome (hero, Labs, Bài tập, Prism highlight bash/docker).

## Bối cảnh

- Có transcript buổi dạy Docker: `dao-tao/22-07-2026/inet_2026-07-18_105914.srt` (~10k dòng, speech-to-text tiếng Việt, nhiều lỗi nhận dạng).
- Yêu cầu: tóm tắt + bóc tách nội dung Docker phù hợp → tạo tài liệu đào tạo có **Labs mới** và **Bài tập mới**.
- **Quan trọng:** Docker chia nhiều buổi, đây là **Phần 1**. Labs & Bài tập phải thiết kế theo **nhóm/group mở rộng được** để các buổi sau bổ sung tiếp.

## Nguồn tham chiếu / convention

- Format chuẩn tài liệu đào tạo = 1 file HTML self-contained (theo `dao-tao/10-07-2026/kien-truc-phan-mem.html`).
- Tái sử dụng nguyên design system CSS ("Engineering Blueprint") + Prism core + smooth-scroll script từ file trên.
- Bổ sung Prism grammar: `bash`, `yaml`, `docker/dockerfile` (đã tải, nhúng inline — giữ self-contained).

## Deliverable

- File: `dao-tao/22-07-2026/docker-phan-1-nen-tang.html` (self-contained, tiếng Việt).
- Cấu trúc:
  1. Hero — nêu rõ "Phần 1 / series nhiều buổi".
  2. Tóm tắt buổi học (từ transcript).
  3. Nội dung cốt lõi (concepts, ví von của giảng viên, lệnh Docker).
  4. **Labs** — dạng nhóm mở rộng: Nhóm "Phần 1 — Nền tảng" (đầy đủ), + roadmap Phần 2/3… ("sắp ra mắt").
  5. **Bài tập** — nhóm theo phần, có đáp án ẩn (accordion).
  6. Cheat-sheet lệnh + tài liệu tham khảo.

## Các bước

1. [x] Đọc template + trích design system CSS/JS.
2. [x] Tải Prism bash/yaml/docker.
3. [x] Bóc tách transcript → giáo trình có cấu trúc (subagent) → `_extract-docker-curriculum.md`.
4. [x] Dựng HTML: summary + content + Labs (group) + Bài tập (group).
5. [x] Verify HTML: self-contained (0 external load), thẻ cân bằng, Prism đủ, render Chrome OK.
6. [x] Đối chiếu chính xác kỹ thuật Docker + đánh dấu các điểm suy luận từ transcript.

## Kết quả

- `docker-phan-1-nen-tang.html` — tài liệu Phần 1 đầy đủ: hero (nêu series), tóm tắt, lý thuyết
  (lịch sử hạ tầng, container vs VM, kiến trúc Docker, image/layer, namespace/cgroups, bất biến & volume),
  bảng lệnh, **6 Labs** (nhóm mở rộng + roadmap Phần 2-4), **10 Bài tập** (có đáp án ẩn), takeaways, nguồn.
- `_extract-docker-curriculum.md` — bản bóc tách transcript có cấu trúc (giữ lại để làm Phần 2-4 & đối chiếu).
- Labs/Bài tập thiết kế theo **nhóm/lab-group**: buổi sau chèn thêm `<article class="lab">` / `.ex` vào group mới,
  cập nhật roadmap track từ "Sắp ra mắt" → "Đang học". Không phá cấu trúc hiện có.

## Tiêu chí hoàn thành

- Nội dung khớp những gì giảng viên dạy trong transcript (không bịa), kiến thức Docker chính xác.
- Labs & Bài tập thực hành được, có nhóm mở rộng cho các buổi sau.
- File self-contained (không tham chiếu tài nguyên ngoài), responsive, dark-mode OK.

## Rủi ro

- Transcript nhiễu → phải chuẩn hóa lệnh/khái niệm cho đúng.
- Nếu giảng viên nói sai kiến thức → giữ ý giảng nhưng đính chính nhẹ trong callout.
