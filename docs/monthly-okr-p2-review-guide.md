# Hướng dẫn review OKR + P2 hằng tháng — BP Công Nghệ

Runbook lặp lại mỗi tháng: đối chiếu **tự đánh giá (OKR + P2)** với **công việc thực tế** rồi xuất báo cáo. Chạy đầu tháng kế tiếp (review tháng N vào đầu tháng N+1).

**Phạm vi:** dattqh, hobv, ducnd, chuongdt. ⛔ KHÔNG làm cho `anhtct` (quản lý khác phụ trách).
**Công cụ:** skill `/gitlab-okr-kpi` (chứa credential discovery + API contract chi tiết). Audit **chỉ-đọc** — KHÔNG submit/khóa P2 (chỉ `draft`).

## 1. Nguồn dữ liệu (đọc chi tiết curl trong skill references)

| Nguồn | Cách lấy | Ghi chú |
|-------|----------|---------|
| **OKR tháng** | `POST my.inet.vn/api/client/v1/accountkpi/search` body `{account,monthStr:"MMYYYY",size:50}` | KHÁC `kpi/search` (=KPI sales). Field: `target`/`result`(tự báo)/`description`/`note`/`status` |
| **P2 tự đánh giá** | `POST .../p2evaluation/get` body `{account,period:"YYYY-MM"}` → `selfScores`/`selfComputed`/`selfStatus` **và** `scores`/`computed`/`status` + `roles` + `history[]` | Tính lại điểm: `.../p2evaluation/compute`. Never submit |
| **Tiêu chí + trọng số** | `POST .../p2config/list` body `{department}` → mỗi tiêu chí có `label`/`desc`/`weight`/`levels`/`rubric` | Nguồn chuẩn cho text tiêu chí. `rubric: []` = không có rubric chi tiết → chấm theo đúng `desc` |
| **Số liệu tham chiếu** | `POST .../p2evaluation/metrics` body `{account,period}` → `tasks`/`ticketConversations`/`calendar`/`timekeeping` | Chính là cột "Số liệu tham chiếu" trên form. ⚠️ Xem bẫy `tasks.total=0` ở §3 |
| **Bằng chứng GitLab** | `gitlabs.inet.vn/api/v4` — `issues`, `merge_requests`, `milestones`, `pipelines`, `jobs/:id/trace`, **`releases`**, `repository/tags`, `users/:id/events` (phân trang!) | Token `GITLABS_ACCESS_TOKEN` nạp qua `source scripts/load-env.sh`. User IDs: dattqh=5, ducnd=27, chuongdt=26, hobv=17. Project IDs ở §4 |
| **OKR kỳ N-1 (bắt buộc)** | Cùng endpoint, `monthStr` tháng trước | Baseline để gán nhãn `mới`/`mở rộng`/`thường kỳ` ở §2. KHÔNG bỏ bước này |
| **Code thực tế (local)** | Scout repo local qua git log + đọc source | Bản đồ repo ở mục 4 |

Cookie `sid`/`ssid` + token nạp bằng `source scripts/load-env.sh` — helper lấy `sid`/`ssid` từ `access-tokens.json` (sổ token chung trên iCloud Drive, entry `service: "inet.vn"`, `type: "session-cookie"`), token GitLab từ file env trên iCloud Drive; repo không chứa file secret nào.

## 2. Phương pháp đánh giá 3 lớp

1. **Hoàn thành** — đọc OKR `result` tự báo + P2 self-scores.
2. **Code thật** — scout repo local + GitLab (issue closed / MR merged) để xác minh KHÔNG chỉ tin status "done". Ghi bằng chứng: path/symbol + ngày landed.
3. **Effort-weighted** — gán **S/M/L/XL cho từng OKR**, ước lượng **KHÁCH QUAN từ code footprint** (số tầng/hệ thống/độ phức tạp), **KHÔNG tin effort tự khai** (tránh liệt kê toàn task S/M để luôn "Tốt").

**Ngưỡng "Tốt" (okr) đã chốt — 3 điều kiện ĐỒNG THỜI:**

1. **Hoàn thành cao** — hạng mục đã khai landed trong kỳ, có bằng chứng.
2. **≥1 deliverable stretch (L–XL)** — nhiều task S/M mà không có stretch → tối đa "Đạt".
3. **Có khác biệt so với kỳ trước** — xem mục dưới. **Mở rộng trên nền có sẵn KHÔNG được đánh giá cao, dù khối lượng rất lớn.**

### Điều kiện 3 — phân loại tính chất từng hạng mục

Gán cho **mỗi entry OKR** một nhãn, so với **OKR kỳ N-1** (không phải cảm nhận):

| Nhãn | Dấu hiệu | Được tính cho "Tốt"? |
|---|---|---|
| **mới** | Dựng từ 0 (repo/module/dịch vụ chưa tồn tại kỳ trước) · đổi kiến trúc hoặc cutover · mở năng lực chưa từng có · giải một lớp vấn đề mới | ✅ có |
| **mở rộng** | Phase tiếp theo của epic đã mở · thêm instance theo khuôn đã có (thêm tool/trang/endpoint/loại OS) · parity cho nền tảng khác · dashboard mới trên dữ liệu đã có · fix/QA cho bề mặt vừa ship | ❌ không |
| **thường kỳ** | Việc lặp lại hằng tháng (cập nhật nội dung, nâng version, xử lý ticket, bảo trì) · cùng tên/cùng phạm vi với entry kỳ trước | ❌ không |

**Cách áp:** "Tốt" cần **≥1 hạng mục nhãn `mới`, và hạng mục đó chiếm phần đáng kể của kỳ**. Một entry `mới` cỡ S/M nằm giữa 5 entry `mở rộng` thì chưa đủ — cân theo tỉ trọng effort, không đếm số dòng. Nếu phần `mới` là **hạ tầng/tooling nội bộ chưa thành năng lực dùng được trong kỳ** thì tính nhẹ hơn năng lực đã tới người dùng.

⚠️ **BẮT BUỘC đọc OKR kỳ N-1** (`accountkpi/search` với `monthStr` tháng trước) trước khi gán nhãn — và **kiểm bằng git, đừng suy từ tên hạng mục**. Bài học 05/08/2026: audit ghi "MCP Phase 2–4 lặp lại khuôn Phase 1 đã dựng từ T6" chỉ vì thấy chữ "Phase 1"; kiểm lại thì commit đầu tiên của `onedash-mcp` là `fd195621c` **09/07/2026** và OKR T6 của ducnd **không có hạng mục MCP nào** → Phase 1 dựng ngay trong T7. Sai một fact ở đây là sai luôn căn cứ chấm điểm.

**Ví dụ T7/2026 (đã kiểm chứng bằng git + OKR T6):**

| Người | Nhãn từng entry | OKR |
|---|---|---|
| dattqh | 5 `mới` (Web-scanner→VictoriaLogs, cutover VictoriaMetrics, Command Capture, CEPH/S3 Inc.1, APM đa tenant) + 2 `mở rộng` | **Tốt** — phần `mới` chiếm gần hết kỳ |
| hobv | 1 `mới` (DAM assets.inet.vn dựng từ 0, XL) + 1 `mới` một phần (DS-R5 O1 landing qua MCP) + 1 `thường kỳ` | Đạt vì lý do khác (`#49` quá hạn milestone) |
| ducnd | 1 `mới` (MCP Phase 1 — nền + transport + device-code CLI) + 5 `mở rộng` (116 tool wrapper quanh endpoint có sẵn, Admin Analytics trên dữ liệu có sẵn, parity systemd, RDP diagnostics, QA 11 lỗi) | **Đạt** — phần `mới` là nền tooling nội bộ, phần lớn khối lượng là lặp khuôn |
| chuongdt | 2 `mới` (khu CTV, ViUI base kit) + 1 `mở rộng` (Telegram ops report tiếp nối notification đa kênh T6) | Đạt vì lý do khác (deploy prod ngoài kỳ) |

⚠️ Điều kiện 3 là **đánh giá tính chất công việc, không phải khối lượng** — nêu nhãn của từng entry trong report kèm lý do, để tháng sau cùng một profile không bị chấm khác.

**Verdict = đối chiếu self-score vs (hoàn thành × code thật × effort).** Chỉ đề xuất điều chỉnh; **điểm cuối do quản lý khóa** trên my.inet.vn.

## 3. Quy tắc quan trọng (dễ sai)

- **`accountkpi/search` phân trang cứng ở 30 entry/trang, BỎ QUA tham số `size`.** Luôn gửi kèm `monthStr` để BE lọc; KHÔNG lấy 1 trang rồi lọc client-side — người có nhiều entry lịch sử (vd dattqh `totalElements=58`) sẽ mất sạch entry của tháng cần review và bị kết luận sai là "không khai OKR". Đối chiếu `totalElements` trả về với số dòng thực nhận trước khi tin kết quả.
- **Deadline:** OKR tháng N phải landed (merge main / issue close) **≤ ngày cuối tháng N**. Việc landed sang tháng sau = trễ.
- **`issue closed` ≠ dùng được.** Mốc tính cho tiêu chí *Cam kết & tiến độ* là ngày deliverable **đạt trạng thái dùng được**, không phải ngày đóng issue. T7/2026: ducnd đóng `#192`/`#193` ngày 22/07 tuyên bố 116 tool MCP xong, nhưng `#236` (31/07) cho thấy đến 31/07 mới rà soát bằng lượt gọi thật và ra 11 lỗi — 1 lỗi làm hỏng cả 26 tool đọc → deliverable chỉ thật sự dùng được vào **đúng ngày cuối kỳ** ⇒ Cam kết "Đạt", không "Tốt".
  - ⚠️ **Đừng đổi căn cứ này thành "làm dồn cuối tháng"** nếu chưa đo: cùng ca đó, commit của ducnd rải đủ 22/22 ngày làm việc, tuần cao nhất là tuần 2 (76 · 166 · 122 · 95 · 137). Lập luận "dồn cuối tháng" sẽ bị chính dữ liệu commit bác lại — phải nói đúng lý do là *thời điểm dùng được*, không phải *nhịp làm việc*.
  - Nếu cùng sự việc đó dùng để hạ Cam kết thì phải nói rõ vì sao **Chất lượng** vẫn giữ (vd: tự phát hiện, tự sửa, đóng trong kỳ, không lọt ra người dùng) — nếu không, tháng sau hai tiêu chí sẽ chấm lệch nhau.
- **"Đã build lên production" không phải bằng chứng.** Phải đối chiếu mốc deploy thật: release object, `last-modified` của bundle prod, hoặc pipeline `deploy` thành công. Có trường hợp merge main đúng hạn nhưng deploy prod sang tháng sau, và trường hợp CI `deploy` bị `skipped` cả tháng vì job `build` fail. Repo deploy thủ công (0 pipeline trong kỳ, CI chỉ deploy `staging`) thì **không có dấu vết audit** — ghi rõ là không kiểm chứng được, đừng suy ra "đã lên prod".
- **Lightweight tag KHÔNG chứng minh được ngày phát hành.** `git for-each-ref '%(creatordate)'` trên tag lightweight (`git cat-file -t` trả `commit`, `taggerdate` rỗng) cho ra **ngày commit** — tag có thể tạo muộn hơn rồi trỏ về commit cũ. Mốc release phải lấy từ `GET /projects/:id/releases` → `created_at`. T7/2026 có 2 tag rơi vào diện này: `assets v1.0.0` (release created 31/07 17:37 +07) và `cloud-panel v1.7.0` (27/07 21:34 +07) — cả hai vẫn in-period, nhưng bằng chứng cũ (creatordate) thì không đứng vững.
- **`tasks.total = 0` ⇒ "Task đúng hạn 0%" là KHÔNG CÓ DỮ LIỆU**, không phải 0% thật. Cột "Số liệu tham chiếu" trên form lấy từ `p2evaluation/metrics`; T7/2026 cả 4 người đều `tasks.total=0` + `ticketConversations.count=0` → **không được dùng để hạ điểm**. Số dùng được duy nhất là `timekeeping` (ngày duyệt · trễ · đúng giờ) — và nó phân hoá thật (T7/2026: 79% ↔ 96–100%).
- **`status` có 3 mức:** `scores` rỗng = **chưa ai chấm** (portal hiện 0/"Chưa đạt", KHÔNG phải điểm xấu) · `draft` = đã chấm chưa chốt · `locked` = **đã khoá, muốn sửa phải `reopen`**. Đề xuất hạ điểm cho bản `locked` là việc khác hẳn điền vào bản trống — report phải nói rõ đang ở mức nào.
- **Đọc `history[]` trước khi tin mức hiện tại.** Mỗi bản ghi có `action` (`self_save`/`self_submit`/`self_reopen`/`setstatus`/`update`), `modifiedBy`, `oldTotal→newTotal`, `reason`. T7/2026: một lần `reopen` với lý do "sai role" nhưng bản resubmit nâng luôn Cam kết từ Đạt → Tốt — không đọc history thì không thấy.
- **Role P2 phải khớp công việc thực tế**, vì trọng số A/B/C/D khác nhau theo role. Kiểm bằng tỉ lệ commit theo repo/tầng, không tin title.
- **"Chờ duyệt" ≠ chưa làm:** entry OKR `status="waiting"` chỉ là chờ quản lý duyệt — công việc **đã làm**. Chỉ coi là dở khi **code/result** cho thấy chưa xong.
- **Liệt kê ĐỦ entry** — không gộp/bỏ sót (đối chiếu số entry `monthStr` khớp số dòng report).
- **Role P2** lấy từ baseline `/get` (có người chọn role khác title, vd hobv title Design System nhưng P2 = Fullstack — hợp lệ nếu công việc đúng vậy).
- Trọng số A/B/C/D khác theo role; điểm do server tính (`selfComputed`) — không hardcode.
- **my.inet.vn là nguồn DUY NHẤT của mức đánh giá — KHÔNG đọc Excel.** File `.xlsx` trong repo chỉ giữ **mẫu công thức tính P2** (trọng số + VLOOKUP), không chứa mức nào → không phải nguồn dữ liệu, không đối chiếu, không nhắc trong report. Mức có hiệu lực = `p2evaluation/get`; tiêu chí + trọng số = `p2config/list`.
- **Phân biệt `scores` với `selfScores`.** `selfScores`/`selfComputed`/`selfStatus` = tự đánh giá; `scores`/`computed`/`status` = điểm quản lý chấm. `scores` rỗng + `status="draft"` nghĩa là **chưa ai chấm** — hiển thị 0/"Chưa đạt" trên portal KHÔNG phải kết quả xấu. Report phải nói rõ, vì để nguyên thì kỳ đó nằm mãi ở 0.
- **Không kết luận từ ảnh chụp màn hình.** Ảnh dùng để đối chiếu, con số phải lấy từ API. Đã có lần khối vàng "ĐÁNH GIÁ CHÍNH THỨC = 0" bị đọc thành điểm thật.

## 4. Bản đồ repo local ↔ thành viên

⚠️ Repo mỗi người **thay đổi theo tháng** — phát hiện lại từ OKR + git mỗi kỳ, đừng bê nguyên bảng này. Cột ID để gọi API trực tiếp, khỏi `?search=` lại.

| Thành viên | Repo local (`~/inet-gitlab/`) | GitLab | ID |
|---|---|---|---|
| dattqh, ducnd | `cloud-panel-application` (OneDash: onedash-backend/client/agent/victoria/mcp) | server-tools/cloud-panel-application | 300 |
| hobv | `design-sys-fe` (packages `@hobui/*`) | design-system/design-sys-fe | 256 |
| hobv | `assets.inet.vn` (DAM — Nuxt web + NestJS api, từ T7/2026) | donv/assets.inet.vn | 338 |
| chuongdt | `portal-client` (khối lượng chính) | donv/portal-client | 238 |
| chuongdt | `portal-server` | donv/portal-server | — |
| chuongdt | `developers.inet.vn` | donv/developers.inet.vn | 303 |

Prod URL để đo `last-modified` của bundle: `portal.inet.vn` · `onedash.inet.vn` · `assets.inet.vn` · `developers.inet.vn` (site này không trả `last-modified`). Repo `donv/inet.vn` (nội dung website, hobv) **ngoài scope token dattqh** — API trả 404, mọi claim liên quan phải ghi là không kiểm chứng được.

## 5. Đầu ra: BÁO CÁO HTML trong `okr-kpi/MM-YYYY/`

Bản tổng hợp cho người xem = **file HTML** self-contained (CSS inline), **để local** — KHÔNG publish ra ngoài (dữ liệu nhân sự). File `.md` chỉ dùng làm bản chi tiết/record đi kèm.

**Vị trí bắt buộc:** mỗi kỳ review có một thư mục riêng.

```
okr-kpi/MM-YYYY/          # kỳ được review, KHÔNG phải tháng chạy audit
├── review-okr-p2-<scope>-<YYMMDD>.json    # dữ liệu nguồn (bắt buộc) — render lại được
├── review-okr-p2-<scope>-<YYMMDD>.html    # bản tổng hợp (bắt buộc)
└── review-okr-p2-<scope>-<YYMMDD>.md      # bản chi tiết đi kèm (tuỳ chọn)
```

**Render bằng script, KHÔNG viết HTML tay:**

```bash
python3 .claude/skills/p2-monthly-okr-audit/scripts/build_html_report.py \
  --data okr-kpi/MM-YYYY/review-okr-p2-team-YYMMDD.json \
  --out  okr-kpi/MM-YYYY/review-okr-p2-team-YYMMDD.html
```

Schema v2 nằm ở docstring đầu script, có sẵn block cho những thứ kỳ nào cũng cần: `summary` (self ↔ official ↔ `status` 3 mức) · `refMetrics` (cảnh báo `tasks.total=0` + bảng chấm công) · `members[].formula` · `members[].entries` (từng entry + effort + bằng chứng) · `members[].unverified` · `traps` · `todos`. Cần khối mới → **mở rộng script + docstring**, đừng quay lại viết tay.

- `MM-YYYY` = **kỳ được review**, KHÔNG phải tháng chạy audit. Review tháng 07/2026 chạy ngày 04/08 vẫn nằm ở `okr-kpi/07-2026/`.
- `<scope>` = `team` khi tổng hợp cả nhóm, hoặc username khi tách riêng (`hobv`, `dattqh`…).
- `<YYMMDD>` = ngày chạy audit — cho phép nhiều lần audit cùng một kỳ mà không ghi đè.
- Tên file mô tả nội dung, **không** chứa số phase hay mã plan.
- Report cũ (T5–T7/2026) nằm rải ở `plans/reports/`, `plans/dattqh/reports/` và `members/2026/T5/`; giữ nguyên tại chỗ, quy tắc này áp dụng từ kỳ T8/2026.

**Nội dung tối thiểu phải có:** cả `selfScores` và `scores` (nêu rõ nếu quản lý chưa chấm) · điểm `total`/`grade` kiểm chứng lại bằng công thức · từng OKR kèm badge effort S/M/L/XL và bằng chứng (path/SHA + ngày landed) · cột "Điều chỉnh đề xuất" · claim nào **không kiểm chứng được** (vd repo ngoài scope token) phải ghi rõ là không kiểm chứng, không đoán theo hướng nào.

**Style theo iNET Design System (viui) — primary.** Lấy token từ `~/inet-gitlab/design-sys-fe/docs/ai-prompt-tokens.json` (đúng thứ viui MCP phục vụ):
- Primary `#0582D4`, gradient `#0582D4→#619ee9`, accent-red `#E8353C`, tech-cyan `#22D3EE`
- Semantic (light): success `#0E9F6E/#ECFDF5` · warning `#D47B0A/#FFFBEB` · error `#B91C1C/#FEF2F2` · info `#1E40AF/#EFF6FF` · nền `#F4F7FA` chữ `#0F1E2D` viền `#D0DAE6`
- Font **Be Vietnam Pro** + mono JetBrains Mono · radius 4/8/12/16 · spacing 8pt · elevation/glow · triết lý *Simple · Secure · Stable*

Bố cục gợi ý: TL;DR (số người khớp / thổi phồng / điều chỉnh) → mỗi thành viên 1 card (điểm self + pill verdict + danh sách OKR kèm badge effort S/M/L/XL + bằng chứng code + **cột "Điều chỉnh đề xuất"** Core/Delivery) → banner deadline + phương pháp.

## 6. Checklist mỗi tháng

- [ ] Xác thực cookie my.inet.vn (200) + token GitLab
- [ ] Lấy đủ OKR (`accountkpi/search` + `monthStr`) + P2 (`p2evaluation/get`) cho 4 người — đếm đủ entry
- [ ] Đọc cả `selfScores` và `scores`; xác định `status` đang ở mức nào (rỗng / `draft` / `locked`)
- [ ] Đọc `history[]` — có lần `reopen`/`update` nào đổi mức không, lý do gì
- [ ] Lấy `p2evaluation/metrics`: kiểm `tasks.total` — nếu 0 thì nói rõ cột tham chiếu không dùng được; ghi bảng `timekeeping`
- [ ] Lấy tiêu chí + trọng số từ `p2config/list` (đừng gõ lại từ nhớ)
- [ ] GitLab: commits/MR/issue/milestone trong tháng (phân trang đủ, không cap 100)
- [ ] Mốc release: `GET /projects/:id/releases` → `created_at` (KHÔNG dùng creatordate của tag lightweight)
- [ ] Mốc production: `last-modified` bundle prod + pipeline `deploy` thành công; repo deploy thủ công → ghi là không kiểm chứng được
- [ ] Scout code local từng repo: xác minh code thật + ngày landed vs deadline
- [ ] **Lấy OKR kỳ N-1** (`accountkpi/search` + `monthStr` tháng trước) làm baseline so sánh
- [ ] Gán nhãn `mới` / `mở rộng` / `thường kỳ` cho **từng entry**, kiểm bằng git (ngày commit đầu của module) — KHÔNG suy từ tên hạng mục
- [ ] Gán effort S/M/L/XL từ code footprint; áp ngưỡng "Tốt" đủ **3 điều kiện** (hoàn thành cao + stretch L–XL + ≥1 hạng mục `mới` chiếm phần đáng kể của kỳ)
- [ ] Kiểm lại `total`/`grade` bằng công thức, so với `selfComputed`/`computed` server trả về — **đưa công thức vào report**
- [ ] Viết JSON theo schema v2 → render HTML bằng `build_html_report.py` vào **`okr-kpi/MM-YYYY/`**; lưu cả `.json`
- [ ] Liệt kê **đủ từng entry OKR** (số dòng khớp `totalElements` của tháng), mỗi entry có effort + bằng chứng + ngày landed
- [ ] Ghi rõ claim nào không kiểm chứng được (không đoán)
- [ ] Nêu điều chỉnh đề xuất; nhắc quản lý khóa điểm cuối nếu `scores` còn rỗng, hoặc `reopen` nếu đã `locked` mà cần sửa

> Xem ví dụ (nằm ở vị trí cũ, trước khi có quy tắc `okr-kpi/`): `plans/reports/audit-okr-p2-260701-1115-thang-06-2026.html` — review tháng 6/2026; `plans/reports/review-p2-hobv-260804-thang-07-2026.html` — review tháng 7/2026 với ma trận 18 claim đối chiếu bằng chứng độc lập.
