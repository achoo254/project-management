# Hướng dẫn review OKR + P2 hằng tháng — BP Công Nghệ

Runbook lặp lại mỗi tháng: đối chiếu **tự đánh giá (OKR + P2)** với **công việc thực tế** rồi xuất báo cáo. Chạy đầu tháng kế tiếp (review tháng N vào đầu tháng N+1).

**Phạm vi:** dattqh, hobv, ducnd, chuongdt. ⛔ KHÔNG làm cho `anhtct` (quản lý khác phụ trách).
**Công cụ:** skill `/gitlab-okr-kpi` (chứa credential discovery + API contract chi tiết). Audit **chỉ-đọc** — KHÔNG submit/khóa P2 (chỉ `draft`).

## 1. Nguồn dữ liệu (đọc chi tiết curl trong skill references)

| Nguồn | Cách lấy | Ghi chú |
|-------|----------|---------|
| **OKR tháng** | `POST my.inet.vn/api/client/v1/accountkpi/search` body `{account,monthStr:"MMYYYY",size:50}` | KHÁC `kpi/search` (=KPI sales). Field: `target`/`result`(tự báo)/`description`/`note`/`status` |
| **P2 tự đánh giá** | `POST .../p2evaluation/get` body `{account,period:"YYYY-MM"}` → `selfScores`/`selfComputed`/`selfStatus` | Tính lại điểm: `.../p2evaluation/compute`. Never submit |
| **Bằng chứng GitLab** | `gitlabs.inet.vn/api/v4` — `users/:id/events` (phân trang!), `merge_requests`, `issues` theo tháng | Token `GITLABS_ACCESS_TOKEN` trong `.env`. User IDs: dattqh=5, ducnd=27, chuongdt=26, hobv=17 |
| **Code thực tế (local)** | Scout repo local qua git log + đọc source | Bản đồ repo ở mục 4 |

Cookie `sid`/`ssid` + token đọc từ `.env` (privacy-guarded → xin duyệt; nguồn qua Bash `. .env` không bị chặn).

## 2. Phương pháp đánh giá 3 lớp

1. **Hoàn thành** — đọc OKR `result` tự báo + P2 self-scores.
2. **Code thật** — scout repo local + GitLab (issue closed / MR merged) để xác minh KHÔNG chỉ tin status "done". Ghi bằng chứng: path/symbol + ngày landed.
3. **Effort-weighted** — gán **S/M/L/XL cho từng OKR**, ước lượng **KHÁCH QUAN từ code footprint** (số tầng/hệ thống/độ phức tạp), **KHÔNG tin effort tự khai** (tránh liệt kê toàn task S/M để luôn "Tốt").

**Ngưỡng "Tốt" (okr) đã chốt:** hoàn thành cao **VÀ** ≥1 deliverable **stretch (L–XL)**. Hoàn thành nhiều task S/M mà không có stretch → tối đa "Đạt".

**Verdict = đối chiếu self-score vs (hoàn thành × code thật × effort).** Chỉ đề xuất điều chỉnh; **điểm cuối do quản lý khóa** trên my.inet.vn.

## 3. Quy tắc quan trọng (dễ sai)

- **`accountkpi/search` phân trang cứng ở 30 entry/trang, BỎ QUA tham số `size`.** Luôn gửi kèm `monthStr` để BE lọc; KHÔNG lấy 1 trang rồi lọc client-side — người có nhiều entry lịch sử (vd dattqh `totalElements=58`) sẽ mất sạch entry của tháng cần review và bị kết luận sai là "không khai OKR". Đối chiếu `totalElements` trả về với số dòng thực nhận trước khi tin kết quả.
- **Deadline:** OKR tháng N phải landed (merge main / issue close) **≤ ngày cuối tháng N**. Việc landed sang tháng sau = trễ.
- **"Đã build lên production" không phải bằng chứng.** Phải đối chiếu mốc deploy thật: tag release, `last-modified` của bundle prod, hoặc pipeline `deploy` thành công. Có trường hợp merge main đúng hạn nhưng deploy prod sang tháng sau, và trường hợp CI `deploy` bị `skipped` cả tháng vì job `build` fail.
- **Role P2 phải khớp công việc thực tế**, vì trọng số A/B/C/D khác nhau theo role. Kiểm bằng tỉ lệ commit theo repo/tầng, không tin title.
- **"Chờ duyệt" ≠ chưa làm:** entry OKR `status="waiting"` chỉ là chờ quản lý duyệt — công việc **đã làm**. Chỉ coi là dở khi **code/result** cho thấy chưa xong.
- **Liệt kê ĐỦ entry** — không gộp/bỏ sót (đối chiếu số entry `monthStr` khớp số dòng report).
- **Role P2** lấy từ baseline `/get` (có người chọn role khác title, vd hobv title Design System nhưng P2 = Fullstack — hợp lệ nếu công việc đúng vậy).
- Trọng số A/B/C/D khác theo role; điểm do server tính (`selfComputed`) — không hardcode.

## 4. Bản đồ repo local ↔ thành viên

| Thành viên | Repo local (`~/inet-gitlab/`) | GitLab |
|---|---|---|
| dattqh, ducnd | `cloud-panel-application` (OneDash: onedash-backend/client/agent/victoria) | server-tools/cloud-panel-application |
| hobv | `design-sys-fe` (packages `@hobui/*`) | design-system/design-sys-fe |
| chuongdt | `developers.inet.vn` (+ portal-client/server) | donv/developers.inet.vn |

## 5. Đầu ra: BÁO CÁO HTML (không dùng .md cho bản tổng hợp)

Bản tổng hợp cho người xem = **file HTML** self-contained (CSS inline), **để local** trong `plans/reports/` — KHÔNG publish ra ngoài (dữ liệu nhân sự). File `.md` chỉ dùng làm bản chi tiết/record đi kèm.

**Style theo iNET Design System (viui) — primary.** Lấy token từ `~/inet-gitlab/design-sys-fe/docs/ai-prompt-tokens.json` (đúng thứ viui MCP phục vụ):
- Primary `#0582D4`, gradient `#0582D4→#619ee9`, accent-red `#E8353C`, tech-cyan `#22D3EE`
- Semantic (light): success `#0E9F6E/#ECFDF5` · warning `#D47B0A/#FFFBEB` · error `#B91C1C/#FEF2F2` · info `#1E40AF/#EFF6FF` · nền `#F4F7FA` chữ `#0F1E2D` viền `#D0DAE6`
- Font **Be Vietnam Pro** + mono JetBrains Mono · radius 4/8/12/16 · spacing 8pt · elevation/glow · triết lý *Simple · Secure · Stable*

Bố cục gợi ý: TL;DR (số người khớp / thổi phồng / điều chỉnh) → mỗi thành viên 1 card (điểm self + pill verdict + danh sách OKR kèm badge effort S/M/L/XL + bằng chứng code + **cột "Điều chỉnh đề xuất"** Core/Delivery) → banner deadline + phương pháp.

## 6. Checklist mỗi tháng

- [ ] Xác thực cookie my.inet.vn (200) + token GitLab
- [ ] Lấy đủ OKR (`accountkpi/search`) + P2 (`p2evaluation/get`) cho 4 người — đếm đủ entry
- [ ] GitLab: commits/MR/issue trong tháng (phân trang đủ, không cap 100)
- [ ] Scout code local từng repo: xác minh code thật + ngày landed vs deadline
- [ ] Gán effort S/M/L/XL từ code footprint; áp ngưỡng "Tốt = + stretch"
- [ ] Xuất HTML (style iNET DS) vào `plans/reports/`; `.md` record đi kèm
- [ ] Nêu điều chỉnh đề xuất; nhắc quản lý khóa điểm cuối

> Xem ví dụ: `plans/reports/audit-okr-p2-260701-1115-thang-06-2026.html` (+ `...-1038-...report.md`) — review tháng 6/2026.
