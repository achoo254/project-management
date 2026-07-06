# Team Roster & Repo Mapping — BP Công Nghệ iNET

> ⚠️ **NGUYÊN TẮC CỐT LÕI: project của mỗi người THAY ĐỔI theo tháng — KHÔNG cố định.**
> Tách 3 phần: (1) Danh tính người = ỔN ĐỊNH · (2) Catalog repo = ỔN ĐỊNH · (3) Ai-làm-gì-tháng-nào = **BIẾN ĐỘNG, phải xác định lại mỗi kỳ** (mục §3).

## §1. Danh tính thành viên (ỔN ĐỊNH)

| Tên | username/email | Vai trò mặc định | KPI URL (my.inet.vn) | File P2 | git author identities (regex) |
|---|---|---|---|---|---|
| Trịnh Quốc Hoàn Đạt | `dattqh` / dattqh@inet.vn | Fullstack · Trưởng phòng | /account/kpi/detail/dattqh@inet.vn | `...- Dat.xlsx` | `dattqh\|DatTQH\|Dat Tran\|quocdat254` |
| Nguyễn Đăng Đức | `ducnd` / ducnd@inet.vn | Frontend | /account/kpi/detail/ducnd@inet.vn | `...- Duc.xlsx` | `ducnd\|Ducnd` |
| Bùi Văn Hổ | `hobv` / hobv@inet.vn | Design System | /account/kpi/detail/hobv@inet.vn | `...- Ho.xlsx` | `hobv\|HoBV` |
| Đinh Tiến Chương | `chuongdt` / chuongdt@inet.vn | Frontend | /account/kpi/detail/chuongdt@inet.vn | `...- Chuong.xlsx` | `chuongdt\|23august\|Chương` |
| Trần Công Tuấn Anh | `anhtct` / anhtct@inet.vn | AI Research | /account/kpi/detail/anhtct@inet.vn | `...- TuanAnh.xlsx` (nếu có) | (chưa biết — lấy bằng `git shortlog -sne`) |

- File P2 trong `D:\CONG VIEC\project-management\members\T{n}\` (T{n}=tháng, vd `T5`). `Vai trò mặc định` chỉ là gợi ý — vai trò thực đọc từ ô B4 file P2.
- 1 người có thể có nhiều git identity (email công ty + email cá nhân + tên hiển thị). Đạt từng commit dưới `quocdat254@gmail.com`. Verify mỗi repo: `git shortlog -sne --all`.

## §2. Catalog repo đã biết (tra cứu path→URL)

> ⚠️ **Local path KHÁC NHAU theo từng máy/người — các path dưới chỉ là MẶC ĐỊNH trên máy hiện tại, KHÔNG đảm bảo đúng mọi nơi.**
> **Luôn verify trước khi scan:** `git -C "<path>" rev-parse --is-inside-work-tree` (hoặc `git_month_evidence.py` tự trả `{"error":"repo_not_found"}`).
> Nếu path không tồn tại / không phải git repo → **HỎI USER đường dẫn đúng** (kèm gợi ý: máy này clone repo ở đâu?). TUYỆT ĐỐI KHÔNG đoán, KHÔNG bỏ qua âm thầm, KHÔNG coi là "0 commit = không làm việc".

| Project | Local path (mặc định máy hiện tại) | GitLab base (commit URL = base + `/-/commit/<sha>`) |
|---|---|---|
| OneDash (cũ: Cloud Panel) | `D:\CONG VIEC\cloud-panel-application` | `https://gitlabs.inet.vn/server-tools/cloud-panel-application` |
| OneMail (workspace) | `D:\CONG VIEC\workspace-application` | `https://gitlabs.inet.vn/inet-workspace/workspace-application` |
| Portal | `D:\CONG VIEC\portal.inet.vn\portal-client` + `\portal-server` | `https://gitlabs.inet.vn/donv/portal-client` · `/donv/portal-server` |
| Developers | `D:\CONG VIEC\developers.inet.vn` | `https://gitlabs.inet.vn/donv/developers.inet.vn` |
| Design System | `D:\CONG VIEC\design-sys-fe` | `https://gitlabs.inet.vn/design-system/design-sys-fe` |

> Catalog có thể thiếu project mới. Nếu kỳ này ai đó làm project chưa có trong bảng → hỏi user local path + lấy GitLab base từ `git -C <path> remote get-url origin`, rồi bổ sung dòng mới.

## §3. Ai làm project nào THÁNG NÀY (BIẾN ĐỘNG — XÁC ĐỊNH LẠI MỖI KỲ)

**KHÔNG giả định từ kỳ trước.** Mỗi lần chạy, xác định assignment của tháng đang audit theo thứ tự:

1. **Nguồn chính — KPI my.inet.vn:** đọc KPI detail của từng người (Workflow Step 3). **Tên + Mục tiêu của mỗi KPI tiết lộ project** (vd KPI "...dùng Cloud Panel" → OneDash; "...whois inet.vn" → website inet.vn). Đây là nguồn đáng tin nhất vì chính người đó đăng ký.
2. **Đối chiếu git:** với mỗi project nghi ngờ trong §2, chạy `git_month_evidence.py` lọc theo author của người đó → repo nào có commit tháng đó = project thực sự làm.
3. **Hỏi user** nếu KPI mơ hồ / project ngoài catalog / không khớp git.

→ Sau khi xác định, ghi assignment vào file `audit-T{n}.json` (input cho report), KHÔNG sửa cố định vào file này.

### Snapshot ví dụ — KỲ T05/2026 (CHỈ tham khảo, KHÔNG dùng cho kỳ khác)
- Đạt → OneDash + OneMail · Đức → OneDash · Hổ → Design System · Chương → Portal + Developers · Tuấn Anh → (chưa map).
> Các kỳ sau có thể hoàn toàn khác (vd Đức chuyển sang Portal, Hổ thêm project mới...). Luôn chạy lại §3.
