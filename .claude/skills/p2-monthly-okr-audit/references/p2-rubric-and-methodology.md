# P2+ Rubric & Scoring — chi tiết

> Nguồn chuẩn: sheet `CẤU TRÚC & TRỌNG SỐ` + `ĐÁNH GIÁ HIỆU SUẤT P2` trong mỗi file P2 Excel. **Verify lại mỗi kỳ** (trọng số có thể đổi theo giai đoạn).

## Cấu trúc P2+
- **P2-Core** (Năng lực, thang 0.8–1.0): A. Năng lực kỹ thuật · B. Ownership & trách nhiệm · C. DevOps & vận hành · D. AI Agent & cải tiến.
- **P2-Delivery** (Kết quả, thang 0.8–1.2): `Mức độ hoàn thành OKR` · `Chất lượng kết quả` · `Cam kết & tiến độ`.
- **P2+ Tổng = (P2-Core × A) + (P2-Delivery × B)**, mặc định A=B=**0.5**.

## Thang mức (Level 2)
| Mức | Core (D) | Delivery |
|---|---|---|
| Chưa Đạt | 0.8 | 0.8 |
| Đạt | 1.0 | 1.0 |
| Tốt | — (Core max = Đạt 1.0) | **1.2 (trần)** |

## Trọng số P2-Core theo vai trò (sheet CẤU TRÚC, A39:E42)
| Vai trò | A. Kỹ thuật | B. Ownership | C. DevOps | D. AI Agent |
|---|---|---|---|---|
| Design System | 30 | 25 | 15 | 30 |
| Backend | 35 | 25 | 15 | 25 |
| Frontend | 30 | 25 | 10 | 35 |
| Fullstack | 30 | 30 | 15 | 25 |

## Trọng số P2-Delivery (sheet CẤU TRÚC, B64:B66)
- OKR/KPI: **0.40** · Chất lượng: **0.35** · Cam kết: **0.25**

## Công thức Excel (verify)
- Delivery `C20` = VLOOKUP(C17)×0.4 + VLOOKUP(C18)×0.35 + VLOOKUP(C19)×0.25
- Core `D12` = Σ(weight_i × level_i/100)
- Tổng `C23` = D12×0.5 + C20×0.5
- Xếp loại `C24`: `ROUND(C23,2)<1`→Chưa đạt · `=1`→Đạt · `>1`→**Tốt**

## Ô Excel cần đọc (sheet `ĐÁNH GIÁ HIỆU SUẤT P2`)
| Ô | Nội dung |
|---|---|
| B3 | Họ tên · B4 Vai trò |
| C3 | label "Kỳ đánh giá" → **giá trị ở D3** (hay trống) |
| C4 | label "Người đánh giá" → giá trị ở D4 (hay trống) |
| C8–C11 | mức P2-Core 4 nhóm |
| C17 / C18 / C19 | **mức Delivery: OKR / Chất lượng / Cam kết** |
| C20 | tổng Delivery · C23 tổng P2+ · C24 xếp loại |

## Mô tả tiêu chí Delivery (đối chiếu khi verdict)
- **Mức độ hoàn thành OKR:** "Tỷ lệ hoàn thành các mục tiêu đã cam kết". → đối chiếu: các KPI/OKR đã ship chưa (git + Kết quả my.inet.vn).
- **Chất lượng kết quả:** "Ít lỗi nghiêm trọng; hạn chế làm lại; không gây rủi ro hệ thống". → đối chiếu: số sự cố prod, revert, rework, security findings. Có sự cố/rework → "Đạt" (không max) là trung thực.
- **Cam kết & tiến độ:** "Hoàn thành đúng hạn; chủ động báo sớm rủi ro; phối hợp tốt". → đối chiếu: commit/ngày đều không, có dựng giám sát/cảnh báo, plan/handoff không.

## Nguyên tắc đánh giá (sheet CẤU TRÚC, mục III)
1. Không chấm trùng nội dung (Core = cách làm; Delivery = kết quả đầu ra).
2. OKR cao nhưng vi phạm chuẩn kỹ thuật/gây rủi ro → không xếp P2+ cao.
3. Đánh giá theo **mặt bằng chung**, không theo 1–2 tình huống nổi bật.

## Audit rules bổ sung (xem SKILL.md → Methodology Rules)
- Bỏ qua trạng thái duyệt my.inet.vn · không dùng weekly meetings · lọc release-bot khi đếm commit · không thổi phồng · tôn trọng quyết định đã chốt của user.
