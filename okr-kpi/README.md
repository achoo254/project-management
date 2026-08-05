# okr-kpi/ — Báo cáo audit OKR + P2 theo tháng

Nơi lưu **bản tổng hợp HTML** của mỗi kỳ review OKR/KPI + P2 (đối chiếu tự đánh giá với bằng chứng thật).

Quy trình và phương pháp: [`../docs/monthly-okr-p2-review-guide.md`](../docs/monthly-okr-p2-review-guide.md). Quy tắc viết nội dung OKR: [`../docs/quy-tac-viet-noi-dung-okr.html`](../docs/quy-tac-viet-noi-dung-okr.html).

## Cấu trúc

```
okr-kpi/MM-YYYY/
├── review-okr-p2-<scope>-<YYMMDD>.json    # dữ liệu nguồn (bắt buộc) — render lại được
├── review-okr-p2-<scope>-<YYMMDD>.html    # bản tổng hợp (bắt buộc)
└── review-okr-p2-<scope>-<YYMMDD>.md      # bản chi tiết đi kèm (tuỳ chọn)
```

- **`MM-YYYY` = kỳ được review**, không phải tháng chạy audit. Review tháng 07/2026 chạy ngày 04/08 vẫn nằm ở `okr-kpi/07-2026/`.
- **`<scope>`** = `team` khi tổng hợp cả nhóm, hoặc username khi tách riêng (`dattqh`, `hobv`, `ducnd`, `chuongdt`).
- **`<YYMMDD>`** = ngày chạy audit, cho phép audit lại cùng một kỳ mà không ghi đè bản trước.
- Tên file mô tả nội dung — không đưa số phase hay mã plan vào tên.

## Quy tắc

- **Render bằng script, KHÔNG viết HTML tay** — `.claude/skills/p2-monthly-okr-audit/scripts/build_html_report.py` (schema v2 ở docstring đầu file):

  ```bash
  python3 .claude/skills/p2-monthly-okr-audit/scripts/build_html_report.py \
    --data okr-kpi/MM-YYYY/review-okr-p2-team-YYMMDD.json \
    --out  okr-kpi/MM-YYYY/review-okr-p2-team-YYMMDD.html
  ```

  Cần khối nội dung schema chưa có → mở rộng script + docstring, đừng viết tay một bản riêng.
- **HTML self-contained**: inline hết CSS/JS, không CDN, không font ngoài, không dẫn file ngoài. Mở được offline (`open <path>` trên macOS).
- **Style theo iNET Design System (viui)** — token trong runbook mục 5; script đã cài sẵn bộ token light.
- **Nội dung tối thiểu** (runbook §5): self ↔ official + `status` (rỗng / `draft` / `locked`) · công thức kiểm chứng `total`/`grade` · **đủ từng entry OKR** kèm effort S/M/L/XL + bằng chứng + ngày landed · điều chỉnh đề xuất · claim không kiểm chứng được phải ghi rõ.
- **Nguồn mức đánh giá = my.inet.vn (`p2evaluation/get`), KHÔNG phải Excel.** File `.xlsx` trong repo chỉ giữ mẫu công thức tính P2, không chứa mức nào → không đọc, không đối chiếu.
- **Dữ liệu nhân sự — để local.** Không publish, không deploy, không gửi ra ngoài công ty.
- **Chỉ-đọc với điểm P2**: report chỉ nêu điều chỉnh đề xuất. Điểm cuối do quản lý khoá trên my.inet.vn; agent chỉ lưu `draft`.
- **Phạm vi**: dattqh, hobv, ducnd, chuongdt. Không bao gồm `anhtct` (quản lý khác phụ trách).

## Lịch sử trước quy tắc này

Report các kỳ T5–T7/2026 làm trước khi có `okr-kpi/`, vẫn nằm ở vị trí cũ và giữ nguyên tại chỗ:

| Kỳ | Vị trí |
|---|---|
| T5/2026 | `plans/dattqh/reports/`, `members/2026/T5/p2-delivery-evidence-audit-*.html` |
| T6/2026 | `plans/reports/audit-okr-p2-260701-*` |
| T7/2026 | `plans/reports/review-p2-*-260804-thang-07-2026.html` |

Quy tắc `okr-kpi/MM-YYYY/` áp dụng từ kỳ **T8/2026**.
