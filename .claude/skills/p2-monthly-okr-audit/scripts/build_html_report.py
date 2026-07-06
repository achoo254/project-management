"""Render a self-contained P2-Delivery audit HTML report from a JSON data file.

Usage:
    python build_html_report.py --data audit.json --out report.html

JSON schema (see example below):
{
  "month": "T05/2026", "date": "2026-06-02",
  "members": [
    {
      "name": "Trịnh Quốc Hoàn Đạt", "role": "Fullstack · Trưởng phòng",
      "projects": "OneDash + OneMail", "commits": "667", "kpiCount": 4,
      "p2plus": "1.065", "delivery": "1.13", "verdict": "Chính xác",
      "kqFilled": "1/4", "kyDanhGia": "trống", "nguoiDanhGia": "trống",
      "badges": ["Minh chứng tốt nhất"],
      "criteria": [
        {"name":"Mức độ hoàn thành OKR", "level":"Tốt", "weight":"40%",
         "verdict":"3/3 KPI đã ship ...", "kq":"5/5 Objectives hoàn thành",
         "evidence":[{"sha":"dd7f300","url":"https://gitlabs.inet.vn/server-tools/cloud-panel-application/-/commit/dd7f3009...","desc":"customer-effectiveness OKR dashboard","repo":"OneDash"}],
         "issues":[{"label":"#36 Component Layer","url":"https://.../-/issues/36"}]
        }
      ]
    }
  ],
  "notes": ["<b>Mô hình nén</b>: ..."],   # raw HTML allowed (trusted author)
  "fixes": ["<b>Điền metadata</b>: ..."]
}

Level -> badge: "Tốt"->green, "Đạt"/"Chưa đạt"->blue/amber. Verdict "Chính xác"->green ✓.
"""
import argparse, html, json, sys

def esc(s): return html.escape(str(s if s is not None else ""))

def level_badge(level):
    cls = "b-tot" if level.strip().lower().startswith("tốt") or level.strip().lower().startswith("tot") else "b-dat"
    return f'<span class="badge {cls}">{esc(level)}</span>'

def verdict_badge(v):
    vl = (v or "").lower()
    if "chính xác" in vl or "chinh xac" in vl or v == "✓":
        return '<span class="badge b-ok">✓ Chính xác</span>'
    return f'<span class="badge b-warn">⚠ {esc(v)}</span>'

CSS = """
:root{--bg:#0f1117;--panel:#161a23;--panel2:#1d2230;--line:#2a3142;--txt:#e6e9ef;--muted:#9aa4b6;--muted2:#6b7488;--green:#34d399;--green-bg:rgba(52,211,153,.12);--amber:#fbbf24;--amber-bg:rgba(251,191,36,.12);--blue:#60a5fa;--blue-bg:rgba(96,165,250,.12);--accent:#49c98d}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.55;font-size:15px}
.wrap{max-width:1080px;margin:0 auto;padding:32px 20px 80px}
header.hero{background:linear-gradient(135deg,#13241d 0%,#161a23 60%);border:1px solid var(--line);border-radius:16px;padding:28px 30px;margin-bottom:26px}
header.hero h1{margin:0 0 6px;font-size:25px}.sub{color:var(--muted);font-size:14px}
.pill{display:inline-block;background:var(--accent);color:#06130d;font-weight:700;font-size:11px;padding:3px 10px;border-radius:999px;margin-left:8px}
.meta-row{margin-top:14px;display:flex;flex-wrap:wrap;gap:8px}.meta-row span{font-size:12px;color:var(--muted);background:var(--panel2);border:1px solid var(--line);padding:4px 10px;border-radius:8px}
.note{background:var(--amber-bg);border:1px solid rgba(251,191,36,.35);border-radius:10px;padding:12px 16px;margin:20px 0;font-size:13.5px;color:#f4e2b6}.note b{color:var(--amber)}
h2.sec{font-size:18px;margin:34px 0 14px;padding-bottom:8px;border-bottom:1px solid var(--line)}h2.sec .em{color:var(--accent)}
table{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--panel2);color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase}
tr:last-child td{border-bottom:none}td.center,th.center{text-align:center}
.badge{display:inline-block;font-weight:700;font-size:11.5px;padding:2px 9px;border-radius:6px;white-space:nowrap}
.b-tot{background:var(--green-bg);color:var(--green);border:1px solid rgba(52,211,153,.4)}
.b-dat{background:var(--blue-bg);color:var(--blue);border:1px solid rgba(96,165,250,.4)}
.b-ok{background:var(--green-bg);color:var(--green);border:1px solid rgba(52,211,153,.4)}
.b-warn{background:var(--amber-bg);color:var(--amber);border:1px solid rgba(251,191,36,.4)}
.score{font-weight:800;font-variant-numeric:tabular-nums}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px 24px;margin:16px 0}
.card h3{margin:0 0 2px;font-size:17px}.card .role{color:var(--muted);font-size:12.5px;margin-bottom:14px}
.crit{border-left:3px solid var(--line);padding:4px 0 4px 14px;margin:14px 0}.crit.tot{border-color:var(--green)}.crit.dat{border-color:var(--blue)}
.crit .ch{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px}.crit .ch .name{font-weight:700;font-size:14px}.crit .ch .w{color:var(--muted2);font-size:11.5px}
.crit .verdict{font-size:13px;color:var(--muted);margin-bottom:8px}
.ev{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
a.commit{display:inline-flex;align-items:center;gap:6px;text-decoration:none;background:var(--panel2);border:1px solid var(--line);border-radius:7px;padding:3px 8px;font-size:12px;color:var(--txt)}
a.commit:hover{border-color:var(--accent);background:#10231a}
a.commit .sha{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--accent);font-size:11px}a.commit .repo{color:var(--muted2);font-size:10.5px}
a.issue{color:var(--blue);text-decoration:none;border-bottom:1px dotted var(--blue);font-size:12px;margin-right:8px}
.kq{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:12.5px;color:#cdd5e3;margin-top:8px}.kq b{color:var(--green)}
.trans{display:flex;flex-wrap:wrap;gap:14px;margin-top:14px;font-size:12.5px}.trans div{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:8px 12px}.trans .lbl{color:var(--muted2);font-size:11px;display:block}
footer{margin-top:30px;color:var(--muted2);font-size:12px;text-align:center;border-top:1px solid var(--line);padding-top:18px}
ul.fix{font-size:13.5px;color:var(--muted);padding-left:20px}ul.fix li{margin:5px 0}ul.fix b{color:var(--txt)}
"""

def render(d):
    month, date_ = esc(d.get("month", "")), esc(d.get("date", ""))
    members = d.get("members", [])
    # summary rows
    rows = []
    for mb in members:
        crit = {c["name"]: c for c in mb.get("criteria", [])}
        def lvl(key):
            for c in mb.get("criteria", []):
                if key in c["name"]:
                    return level_badge(c["level"])
            return "—"
        rows.append(f"""<tr>
          <td><b>{esc(mb.get('name'))}</b><br><span style="color:var(--muted2);font-size:11px">{esc(mb.get('role'))}</span></td>
          <td>{esc(mb.get('projects'))}</td>
          <td class="center">{lvl('hoàn thành OKR')}</td>
          <td class="center">{lvl('Chất lượng')}</td>
          <td class="center">{lvl('Cam kết')}</td>
          <td class="center score">{esc(mb.get('delivery'))}</td>
          <td class="center score">{esc(mb.get('p2plus'))}</td>
          <td class="center">{verdict_badge(mb.get('verdict'))}</td></tr>""")

    # detail cards
    cards = []
    for mb in members:
        extra = "".join(f'<span class="badge b-ok" style="font-size:10px">{esc(b)}</span> ' for b in mb.get("badges", []))
        crit_html = []
        for c in mb.get("criteria", []):
            tot = c["level"].strip().lower().startswith(("tốt", "tot"))
            ev = "".join(
                f'<a class="commit" href="{esc(e.get("url"))}" target="_blank"><span class="sha">{esc(e.get("sha"))}</span> {esc(e.get("desc"))} <span class="repo">{esc(e.get("repo"))}</span></a>'
                for e in c.get("evidence", []) if e.get("sha"))
            kq = f'<div class="kq">Kết quả: <b>{esc(c["kq"])}</b></div>' if c.get("kq") else ""
            iss = ""
            if c.get("issues"):
                iss = '<div class="verdict" style="margin-top:8px">Issue: ' + " · ".join(
                    f'<a class="issue" href="{esc(i.get("url"))}" target="_blank">{esc(i.get("label"))}</a>' for i in c["issues"]) + "</div>"
            crit_html.append(f"""<div class="crit {'tot' if tot else 'dat'}">
              <div class="ch"><span class="name">{esc(c['name'])}</span> {level_badge(c['level'])} <span class="w">{esc(c.get('weight'))}</span></div>
              <div class="verdict">{esc(c.get('verdict'))}</div>{kq}
              <div class="ev">{ev}</div>{iss}</div>""")
        cards.append(f"""<div class="card">
          <h3>{esc(mb.get('name'))} <span class="badge b-tot" style="font-size:10px">P2+ {esc(mb.get('p2plus'))}</span> {extra}</h3>
          <div class="role">{esc(mb.get('role'))} · {esc(mb.get('projects'))} · {esc(mb.get('commits'))} commit · {esc(mb.get('kpiCount'))} KPI</div>
          {''.join(crit_html)}
          <div class="trans">
            <div><span class="lbl">Kết quả KPI điền</span> {esc(mb.get('kqFilled'))}</div>
            <div><span class="lbl">Kỳ đánh giá</span> {esc(mb.get('kyDanhGia'))}</div>
            <div><span class="lbl">Người đánh giá</span> {esc(mb.get('nguoiDanhGia'))}</div>
          </div></div>""")

    notes = "".join(f"<p>{n}</p>" for n in d.get("notes", []))  # raw HTML (trusted)
    fixes = "".join(f"<li>{f}</li>" for f in d.get("fixes", []))
    notes_block = f'<h2 class="sec"><span class="em">3.</span> Quan sát &amp; minh bạch</h2><div class="card">{notes}</div>' if notes else ""
    fixes_block = f'<h2 class="sec"><span class="em">4.</span> Cần xử lý trước khi gửi</h2><ul class="fix">{fixes}</ul>' if fixes else ""

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Audit P2-Delivery — BP Công Nghệ {month}</title><style>{CSS}</style></head><body><div class="wrap">
<header class="hero"><h1>Audit "KẾT QUẢ CÔNG VIỆC" (P2-Delivery)<span class="pill">{month}</span></h1>
<div class="sub">BP Công Nghệ iNET · Kiểm chứng <b style="color:var(--green)">chính xác</b> · <b style="color:var(--blue)">minh bạch</b> · <b style="color:var(--accent)">có bằng chứng</b></div>
<div class="meta-row"><span>📅 {date_}</span><span>🔍 git log + my.inet.vn KPI</span><span>👥 {len(members)} thành viên</span><span>📊 Delivery: Chưa đạt 0.8 · Đạt 1.0 · Tốt 1.2</span></div></header>
<div class="note"><b>⚠ Phương pháp:</b> KHÔNG xét trạng thái "Đã duyệt/Duyệt" (việc của quản lý). Chỉ xét công việc thực (git + KPI shipped). Mọi link commit là SHA thật trên gitlabs.inet.vn.</div>
<h2 class="sec"><span class="em">1.</span> Bảng tổng — verdict 3 tiêu chí Delivery</h2>
<table><thead><tr><th>Thành viên</th><th>Dự án</th><th class="center">Hoàn thành OKR<br>(40%)</th><th class="center">Chất lượng<br>(35%)</th><th class="center">Cam kết<br>(25%)</th><th class="center">Delivery</th><th class="center">P2+</th><th class="center">Audit</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
<h2 class="sec"><span class="em">2.</span> Chi tiết &amp; bằng chứng từng người</h2>{''.join(cards)}
{notes_block}{fixes_block}
<footer>Audit dựa trên git log {month} + KPI my.inet.vn · BP Công Nghệ iNET · {date_}</footer>
</div></body></html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    with open(a.data, encoding="utf-8") as f:
        d = json.load(f)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(render(d))
    print(f"OK -> {a.out}")

if __name__ == "__main__":
    main()
