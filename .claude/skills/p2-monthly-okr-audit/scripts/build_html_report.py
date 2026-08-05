"""Render a self-contained OKR + P2 audit HTML report (iNET Design System, light) from JSON.

Usage:
    python3 build_html_report.py --data audit.json --out okr-kpi/MM-YYYY/review-okr-p2-team-YYMMDD.html

Schema v2. Mọi field đều optional trừ `meta` và `members` — thiếu block nào thì block đó
không render. Field `html` cho phép HTML thô (tác giả là agent, nội dung tin cậy); mọi field
khác được escape.

{
  "meta": {
    "title":  "Audit P2-Delivery — Đối chiếu tự đánh giá với bằng chứng thật",
    "period": "07/2026",            // KỲ ĐƯỢC REVIEW (không phải tháng chạy audit)
    "auditDate": "05/08/2026",
    "subtitle": "BP Công Nghệ · iNET · 4 thành viên (...)",
    "chips": ["Audit 05/08/2026", "Chỉ-đọc — không sửa, không khoá điểm", "..."],
    "sourceNote": "ghi chú về nguồn dữ liệu của kỳ (nếu có gì bất thường cần nêu ngay đầu report)"
  },

  "banners": [ {"tone":"err|warn|ok|info", "title":"...", "html":"..."} ],

  "summary": [ {                    // bảng chốt — 1 dòng / người
    "name":"chuongdt", "role":"Frontend", "roleNote":"đã sửa từ Backend 04/08",
    "self":"1.025", "selfGrade":"Tốt", "selfNote":"submit 04/08 17:53",
    "official":"1.025", "officialGrade":"Tốt", "officialNote":"khoá 05/08 10:38",
    "status":"locked",              // empty | draft | locked  (xem STATUS_MAP)
    "statusNote":"__permission: self",
    "delivery":"Đạt / Đạt / Tốt",
    "proposal":"Hạ Cam kết → Đạt", "proposalTone":"err", "proposalNote":"tổng về 1.0",
    "flag": true                    // tô nền cảnh báo cho dòng này
  } ],

  "refMetrics": {                   // cảnh báo "Số liệu tham chiếu" + bảng chấm công
    "title":"...", "items":[{"tone":"y|n|q|i","html":"..."}], "source":"POST .../metrics",
    "timekeeping": {"title":"...", "rows":[
        {"who":"chuongdt","approved":19,"late":4,"onTimeRate":79,"tone":"err","flag":true} ]}
  },

  "members": [ {
    "name":"ducnd · Nguyễn Đăng Đức", "flag": false,
    "pills":[{"tone":"info","text":"6 entry · 2×XL + 4×L"}],
    "score":"1.1 · Tốt",
    "formula": {                    // BẮT BUỘC theo runbook §5: kiểm chứng lại total/grade
      "lines":["core = 1.0×0.30 + ... = 1.00   // trọng số role Frontend", "..."],
      "server":"khớp computed server trả về (1.1 / Tốt)"
    },
    "criteria":[ {"name":"OKR","weight":"40%","level":"Tốt","levelTone":"ok",
                  "evidence":[{"tone":"y","html":"..."}] } ],
    "entries":[ {"effort":"XL","status":"approved","target":"...",
                 "novelty":"mới|mở rộng|thường kỳ",   // runbook §2 điều kiện 3 — chỉ `mới` tính cho "Tốt"
                 "evidence":"#204 closed 06/07 ...","tone":"y"} ],
    "unverified":[ "claim ... — repo ngoài scope token, KHÔNG kiểm chứng được" ]
  } ],

  "traps":[ {"tag":"Bẫy 1","title":"...","steps":[{"d":"Cách đọc sai","html":"...","bad":true}]} ],
  "todos":[ {"task":"...","level":"blocker","levelTone":"err","owner":"dattqh"} ],
  "sourcesHtml":"...",
  "footerHtml":"..."
}

Quy tắc render (khớp docs/monthly-okr-p2-review-guide.md §5):
- Self-contained: CSS inline, KHÔNG CDN / font ngoài / file ngoài.
- Token iNET DS (viui) light: primary #0582D4 · gradient #0582D4→#619ee9 · accent-red #E8353C
  · success #0E9F6E/#ECFDF5 · warning #D47B0A/#FFFBEB · error #B91C1C/#FEF2F2
  · info #1E40AF/#EFF6FF · nền #F4F7FA · chữ #0F1E2D · viền #D0DAE6 · radius 4/8/12/16.
- Dữ liệu nhân sự → để local, KHÔNG publish.
"""
import argparse
import html
import json
import sys

TONE = {"y": "ok", "n": "err", "q": "warn", "i": "gray",
        "ok": "ok", "err": "err", "warn": "warn", "info": "info", "gray": "gray"}

NOVELTY_TONE = {"mới": "ok", "mở rộng": "warn", "thường kỳ": "gray"}

STATUS_MAP = {
    "empty":  ("gray", "trống · chưa ai chấm"),
    "draft":  ("warn", "draft"),
    "locked": ("info", "locked · phải reopen mới sửa được"),
}


def esc(s):
    return html.escape(str(s if s is not None else ""))


def pill(text, tone="gray"):
    return f'<span class="pill p-{TONE.get(tone, "gray")}">{esc(text)}</span>'


def ev_list(items):
    """items: [{"tone":"y|n|q|i","html":"..."}] → <ul class="ev">"""
    if not items:
        return ""
    lis = "".join(f'<li class="{esc(it.get("tone", "i"))}">{it.get("html", "")}</li>' for it in items)
    return f'<ul class="ev">{lis}</ul>'


CSS = """
:root{
  --pri:#0582D4; --pri-2:#619ee9; --red:#E8353C; --cyan:#22D3EE;
  --ok:#0E9F6E; --ok-bg:#ECFDF5; --warn:#D47B0A; --warn-bg:#FFFBEB;
  --err:#B91C1C; --err-bg:#FEF2F2; --info:#1E40AF; --info-bg:#EFF6FF;
  --bg:#F4F7FA; --card:#fff; --ink:#0F1E2D; --muted:#5B6B7C; --line:#D0DAE6;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:"Be Vietnam Pro","Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  font-size:14.5px;line-height:1.55}
code,.mono{font-family:"JetBrains Mono","SF Mono",Menlo,Consolas,monospace;font-size:.86em}
code{background:#EEF3F8;border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px 56px}
header{background:linear-gradient(115deg,#0582D4,#619ee9);color:#fff;padding:26px 0 22px;margin-bottom:22px}
header .wrap{padding-bottom:0}
h1{font-size:22px;margin:0 0 6px;font-weight:700;letter-spacing:-.2px}
.sub{opacity:.92;font-size:13px}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.meta span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);
  border-radius:999px;padding:3px 11px;font-size:11.5px}
h2{font-size:16px;margin:30px 0 12px;padding-left:10px;border-left:4px solid var(--pri)}
h3{font-size:14px;margin:0 0 8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;
  box-shadow:0 1px 2px rgba(15,30,45,.05)}
.banner{border-radius:12px;padding:14px 18px;margin-bottom:8px;border:1px solid}
.banner.err{background:var(--err-bg);border-color:#F3C4C4}
.banner.ok{background:var(--ok-bg);border-color:#BFE7D5}
.banner.warn{background:var(--warn-bg);border-color:#F0DCA8}
.banner.info{background:var(--info-bg);border-color:#C7D7F5}
.banner .bt{font-weight:700;font-size:15px;margin-bottom:4px}
.grid{display:grid;gap:12px}
.g2{grid-template-columns:repeat(auto-fit,minmax(330px,1fr))}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:13px;min-width:640px}
th{background:#EDF2F7;text-align:left;font-weight:600;font-size:11.5px;text-transform:uppercase;
  letter-spacing:.3px;color:#41536A;padding:9px 12px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid #E8EEF4;vertical-align:top}
tr:last-child td{border-bottom:none}
tr.flag{background:#FFF9F9}
.pill{display:inline-block;border-radius:999px;padding:1px 9px;font-size:11px;font-weight:600;white-space:nowrap}
.p-ok{background:var(--ok-bg);color:var(--ok);border:1px solid #BFE7D5}
.p-err{background:var(--err-bg);color:var(--err);border:1px solid #F3C4C4}
.p-warn{background:var(--warn-bg);color:var(--warn);border:1px solid #F0DCA8}
.p-info{background:var(--info-bg);color:var(--info);border:1px solid #C7D7F5}
.p-gray{background:#EEF3F8;color:#41536A;border:1px solid var(--line)}
.member{border-left:4px solid var(--pri);margin-bottom:12px}
.member.flag{border-left-color:var(--red)}
.mhead{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;margin-bottom:12px;
  padding-bottom:10px;border-bottom:1px dashed var(--line)}
.mhead .nm{font-size:16px;font-weight:700}
.mhead .sc{font-size:20px;font-weight:700;color:var(--pri);margin-left:auto}
.fx{background:#F8FAFC;border:1px dashed var(--line);border-radius:8px;padding:9px 12px;margin-bottom:12px;
  font-family:"JetBrains Mono","SF Mono",Menlo,Consolas,monospace;font-size:11.8px;color:#33475E;
  overflow-x:auto;white-space:pre;line-height:1.7}
.fx .srv{color:var(--ok);font-weight:700}
.crit{display:grid;grid-template-columns:118px 74px 1fr;font-size:13px}
.crit>div{padding:8px 10px;border-bottom:1px solid #E8EEF4}
.crit>div:nth-child(3n+1){font-weight:600;background:#F8FAFC}
.ev{margin:0;padding-left:0;list-style:none}
.ev li{position:relative;padding-left:20px;margin-bottom:5px}
.ev li:before{position:absolute;left:0;top:0;font-weight:700}
.ev li.y:before{content:"\\2713";color:var(--ok)}
.ev li.n:before{content:"\\2717";color:var(--err)}
.ev li.q:before{content:"!";color:var(--warn)}
.ev li.i:before{content:"\\00B7";color:var(--muted);font-size:18px;line-height:1}
.tl{list-style:none;margin:0;padding:0;border-left:2px solid var(--line);margin-left:6px}
.tl li{position:relative;padding:0 0 12px 16px}
.tl li:before{content:"";position:absolute;left:-6px;top:5px;width:10px;height:10px;border-radius:50%;
  background:var(--pri);border:2px solid #fff;box-shadow:0 0 0 1px var(--line)}
.tl li.bad:before{background:var(--red)}
.tl .d{font-size:11.5px;color:var(--muted);font-weight:600}
.small{font-size:12px;color:var(--muted)}
.unv{background:var(--warn-bg);border:1px solid #F0DCA8;border-radius:8px;padding:8px 12px;
  font-size:12.5px;margin-top:10px}
.unv b{color:var(--warn)}
footer{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);font-size:11.5px;color:var(--muted)}
.src{background:#F8FAFC;border:1px dashed var(--line);border-radius:8px;padding:10px 12px;
  font-size:11.5px;color:var(--muted)}
"""


def r_header(meta):
    chips = "".join(f"<span>{esc(c)}</span>" for c in meta.get("chips", []))
    return f"""<header><div class="wrap">
  <h1>{esc(meta.get('title', 'Audit OKR + P2'))}</h1>
  <div class="sub">{esc(meta.get('subtitle', ''))} · Kỳ <b>tháng {esc(meta.get('period', ''))}</b></div>
  <div class="meta">{chips}</div>
</div></header>"""


def r_banners(banners):
    out = []
    for b in banners:
        out.append(f'<div class="banner {esc(TONE.get(b.get("tone", "info"), "info"))}">'
                   f'<div class="bt">{esc(b.get("title", ""))}</div>{b.get("html", "")}</div>')
    return "".join(out)


def r_summary(rows):
    if not rows:
        return ""
    trs = []
    for r in rows:
        st_tone, st_txt = STATUS_MAP.get(r.get("status", "empty"), ("gray", r.get("status", "")))
        official = (f'<b>{esc(r["official"])}</b> {pill(r.get("officialGrade", ""), "ok")}'
                    if r.get("official") else pill("trống · 0", "gray"))
        onote = f'<br><span class="small">{esc(r.get("officialNote", ""))}</span>' if r.get("officialNote") else ""
        pnote = f'<br><span class="small">{esc(r.get("proposalNote", ""))}</span>' if r.get("proposalNote") else ""
        rnote = f'<br><span class="small">{esc(r.get("roleNote", ""))}</span>' if r.get("roleNote") else ""
        snote = f' · <code>{esc(r.get("statusNote", ""))}</code>' if r.get("statusNote") else ""
        trs.append(f"""<tr class="{'flag' if r.get('flag') else ''}">
  <td><b>{esc(r.get('name'))}</b></td>
  <td>{esc(r.get('role'))}{rnote}</td>
  <td><b>{esc(r.get('self'))}</b> {pill(r.get('selfGrade', ''), 'ok')}<br>
      <span class="small">{esc(r.get('selfNote', ''))}</span></td>
  <td>{official}{onote}</td>
  <td>{pill(st_txt, st_tone)}{snote}</td>
  <td>{esc(r.get('delivery'))}</td>
  <td>{pill(r.get('proposal', ''), r.get('proposalTone', 'ok'))}{pnote}</td>
</tr>""")
    return f"""<h2>Bảng chốt — trạng thái &amp; đề xuất</h2>
<div class="tw"><table>
<thead><tr><th>Người</th><th>Role P2</th><th>Tự đánh giá</th><th>Chính thức</th>
<th>Trạng thái</th><th>OKR / Chất lượng / Cam kết</th><th>Đề xuất</th></tr></thead>
<tbody>{"".join(trs)}</tbody></table></div>"""


def r_ref_metrics(rm):
    if not rm:
        return ""
    tk = rm.get("timekeeping") or {}
    tk_rows = "".join(
        f'<tr class="{"flag" if x.get("flag") else ""}"><td>{esc(x.get("who"))}</td>'
        f'<td>{esc(x.get("approved"))}</td><td>{esc(x.get("late"))}</td>'
        f'<td>{pill(str(x.get("onTimeRate")) + "%", x.get("tone", "ok"))}</td></tr>'
        for x in tk.get("rows", []))
    tk_html = f"""<div class="card"><h3>{esc(tk.get('title', 'Chấm công'))}</h3>
  <div class="tw" style="border:none"><table style="min-width:0">
  <thead><tr><th>Người</th><th>Ngày duyệt</th><th>Trễ</th><th>Đúng giờ</th></tr></thead>
  <tbody>{tk_rows}</tbody></table></div></div>""" if tk_rows else ""
    src = f'<p class="small" style="margin-bottom:0">Nguồn: {rm.get("source", "")}</p>' if rm.get("source") else ""
    return f"""<h2>Cảnh báo phương pháp — số liệu tham chiếu trên form</h2>
<div class="grid g2">
  <div class="card"><h3>{esc(rm.get('title', ''))}</h3>{ev_list(rm.get('items', []))}{src}</div>
  {tk_html}
</div>"""


def r_formula(f):
    if not f:
        return ""
    lines = "\n".join(esc(l) for l in f.get("lines", []))
    srv = f'\n<span class="srv">// {esc(f["server"])}</span>' if f.get("server") else ""
    return f'<div class="fx">{lines}{srv}</div>'


def r_entries(entries):
    if not entries:
        return ""
    trs = "".join(
        f'<tr><td>{pill(e.get("effort", "-"), "info")}</td>'
        f'<td>{pill(e["novelty"], NOVELTY_TONE.get(e["novelty"], "gray")) if e.get("novelty") else "—"}</td>'
        f'<td><code>{esc(e.get("status", ""))}</code></td>'
        f'<td>{esc(e.get("target", ""))}</td>'
        f'<td>{e.get("evidence", "")}</td></tr>'
        for e in entries)
    return f"""<div class="tw" style="margin-top:12px"><table>
<thead><tr><th>Effort</th><th>Tính chất</th><th>Duyệt</th><th>Hạng mục OKR</th><th>Bằng chứng · ngày landed</th></tr></thead>
<tbody>{trs}</tbody></table></div>"""


def r_member(mb):
    pills = "".join(pill(p.get("text", ""), p.get("tone", "gray")) + " " for p in mb.get("pills", []))
    crit = []
    for c in mb.get("criteria", []):
        head = f'{esc(c.get("name"))}<br><span class="small">{esc(c.get("weight", ""))}</span>'
        crit.append(f'<div>{head}</div><div>{pill(c.get("level", ""), c.get("levelTone", "gray"))}</div>'
                    f'<div>{ev_list(c.get("evidence", []))}</div>')
    unv = ""
    if mb.get("unverified"):
        lis = "".join(f"<li>{u}</li>" for u in mb["unverified"])
        unv = f'<div class="unv"><b>Không kiểm chứng được</b> (không đoán theo hướng nào)<ul style="margin:4px 0 0;padding-left:18px">{lis}</ul></div>'
    return f"""<div class="card member {'flag' if mb.get('flag') else ''}">
  <div class="mhead"><span class="nm">{esc(mb.get('name'))}</span>{pills}
    <span class="sc">{esc(mb.get('score', ''))}</span></div>
  {r_formula(mb.get('formula'))}
  <div class="crit">{"".join(crit)}</div>
  {r_entries(mb.get('entries', []))}
  {unv}
</div>"""


def r_traps(traps):
    if not traps:
        return ""
    cards = []
    for t in traps:
        steps = "".join(
            f'<li class="{"bad" if s.get("bad") else ""}"><span class="d">{esc(s.get("d", ""))}</span><br>{s.get("html", "")}</li>'
            for s in t.get("steps", []))
        cards.append(f'<div class="card"><h3>{pill(t.get("tag", "Bẫy"), "err")} &nbsp;{esc(t.get("title"))}</h3>'
                     f'<ul class="tl">{steps}</ul></div>')
    return f'<h2>Bẫy kỹ thuật đã vá trong lượt audit này</h2><div class="grid g2">{"".join(cards)}</div>'


def r_todos(todos):
    if not todos:
        return ""
    trs = "".join(
        f"<tr><td>{i + 1}</td><td>{t.get('task', '')}</td>"
        f"<td>{pill(t.get('level', ''), t.get('levelTone', 'info'))}</td>"
        f"<td>{esc(t.get('owner', ''))}</td></tr>"
        for i, t in enumerate(todos))
    return f"""<h2>Việc cần làm</h2><div class="tw"><table>
<thead><tr><th>#</th><th>Việc</th><th>Mức</th><th>Người</th></tr></thead>
<tbody>{trs}</tbody></table></div>"""


def render(d):
    meta = d.get("meta", {})
    note = (f'<div class="banner info"><div class="bt">Ghi chú nguồn dữ liệu</div>{meta["sourceNote"]}</div>'
            if meta.get("sourceNote") else "")
    src = f'<h2>Nguồn &amp; phương pháp</h2><div class="src">{d["sourcesHtml"]}</div>' if d.get("sourcesHtml") else ""
    foot = f'<footer>{d["footerHtml"]}</footer>' if d.get("footerHtml") else ""
    members = "".join(r_member(m) for m in d.get("members", []))
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(meta.get('title', 'Audit OKR + P2'))} — {esc(meta.get('period', ''))}</title>
<style>{CSS}</style>
</head>
<body>
{r_header(meta)}
<div class="wrap">
{r_banners(d.get('banners', []))}
{note}
{r_summary(d.get('summary', []))}
{r_ref_metrics(d.get('refMetrics'))}
<h2>Từng thành viên — điểm, công thức, bằng chứng từng entry</h2>
{members}
{r_traps(d.get('traps', []))}
{r_todos(d.get('todos', []))}
{src}
{foot}
</div>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Render OKR+P2 audit HTML (schema v2, iNET DS light)")
    ap.add_argument("--data", required=True, help="JSON data file (UTF-8)")
    ap.add_argument("--out", required=True, help="output .html path under okr-kpi/MM-YYYY/")
    a = ap.parse_args()
    with open(a.data, encoding="utf-8") as f:
        data = json.load(f)
    if "meta" not in data or "members" not in data:
        sys.exit("ERROR: JSON thiếu `meta` hoặc `members` — xem schema ở docstring đầu file.")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(render(data))
    print(f"OK → {a.out}")


if __name__ == "__main__":
    main()
