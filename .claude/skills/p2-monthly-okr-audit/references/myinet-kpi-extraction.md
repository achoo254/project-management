# Trích KPI chính thức từ my.inet.vn

Trang KPI detail là **AngularJS SPA** — data nạp qua API gateway `POST /api/helpdesk/v1/accountkpi/search` (headers `token`+`sid` đọc từ cookie). Cách ổn định nhất: **dùng browser đã đăng nhập** (claude-in-chrome) đọc DOM đã render. **Bỏ qua cột trạng thái "Đã duyệt/Duyệt".**

## Cách A (khuyến nghị) — browser đã đăng nhập

1. `tabs_context_mcp` (createIfEmpty) → lấy tabId.
2. `navigate` tới `https://my.inet.vn/account/kpi/detail/<email>` (vd `chuongdt@inet.vn`).
3. Trang SPA polling liên tục → `get_page_text` thường lỗi `document_idle`. Dùng `javascript_tool` đọc DOM trực tiếp.
4. ⚠️ `document.body.innerText` có thể bị privacy-hook chặn ("Cookie/query string data"). → CHỈ trích phần tử bảng KPI, **strip ký tự đặc biệt/URL**, KHÔNG dump cả innerText. Cột "Hành động" chứa link query-string → loại bỏ.
5. Promise/await timeout 45s → dùng pattern **fire-and-store** (`window.__kpi = ...; 'kicked'`) rồi poll ở call sau (nếu phải gọi API). Để đọc DOM thì không cần await.

### JS snippet — summary + danh sách KPI (an toàn với privacy hook)
```javascript
(function(){
 function safe(s){return (s||'').replace(/[^\p{L}\p{N} ,.()/%–-]/gu,'').replace(/\s+/g,' ').trim();}
 var bt=document.body.innerText;
 if(!/Mục tiêu công việc/.test(bt)) return 'NOT LOADED YET';
 var commits=(bt.match(/Commits\s*\((\d+)\)/)||[])[1]||'?';
 var labels=['Tổng KPI','Đã duyệt','Chờ duyệt'],sum={};
 var leaf=[...document.querySelectorAll('*')].filter(e=>e.children.length===0);
 labels.forEach(function(lb){var n=leaf.find(e=>e.innerText&&e.innerText.trim()===lb);
   sum[lb]=n&&n.parentElement&&n.parentElement.innerText.match(/\d+/)?n.parentElement.innerText.match(/\d+/)[0]:'?';});
 var t=[...document.querySelectorAll('table')].find(tb=>/Chi tiết KPI/.test(tb.innerText)&&/Trạng thái/.test(tb.innerText));
 var kpis=[];
 if(t){[...t.querySelectorAll('tr')].slice(1).forEach(function(tr){var c=[...tr.querySelectorAll('td')];if(!c.length)return;
   kpis.push({name:safe(c[0]&&c[0].innerText).slice(0,80), muctieu:safe(c[1]&&c[1].innerText).slice(0,90), kq:safe(c[2]&&c[2].innerText).slice(0,90)});});}
 return JSON.stringify({commits:commits,summary:sum,kpiCount:kpis.length,kpis:kpis}).slice(0,2600);
})()
```
> Cột bảng KPI: `0`=Chi tiết KPI(tên) · `1`=Mục tiêu · `2`=**Kết quả** · `3`=Ghi chú · `4`=Trạng thái(bỏ qua) · `5`=Hành động(bỏ, có URL). Trang cũng hiện "Đánh giá P2+ T{n}" + lịch sử (vd "T04/2026 1.04 (Tốt)").

## Cách B — auth bằng cookie từ iCloud Drive (khi browser chưa login)

File credentials trên iCloud Drive chứa `sid` (JWT) + `ssid`; repo KHÔNG chứa file secret nào. Privacy-hook có thể chặn đọc → cần user phê duyệt. KHÔNG nhúng literal credential vào lệnh (secret-scan hook chặn) — nạp qua helper:
```bash
source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive
# validate (200=OK, 302/401=hết hạn):
curl -s -o /dev/null -w "%{http_code}\n" -H "Cookie: sid=$sid; ssid=$ssid" https://my.inet.vn/account/kpi
```
⚠️ API gateway `accountkpi/search` cần thêm header `token` (set lúc SSO login, KHÔNG có trong file env) → curl thường trả `{"status":"error","message":"Login required"}`. Vì vậy **ưu tiên Cách A** (browser). Cookie JWT có `exp` — kiểm tra hạn trước khi dùng.

## Map KPI ↔ git
- Với mỗi KPI: đọc tên + Mục tiêu + Kết quả → suy ra từ khóa → `git_month_evidence.py --grep "<kw>"` lấy SHA minh chứng.
- KPI ngoài repo dự án chính (vd whois trên inet.vn) → ghi "ngoài repo, verify qua Kết quả 'đã online'", không kết luận thiếu.
- "Commits (N)" my.inet.vn đếm thường khớp git count (lệch nhẹ do dedupe merge / gộp nhiều repo).
