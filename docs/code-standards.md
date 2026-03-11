# Code Standards & Conventions

## File Naming Conventions

### Meeting Notes (`weekly meetings/`)
- **Format:** `DD-MM-YYYY.md`
- **Example:** `02-03-2026.md` (March 2, 2026)
- **Organization:**
  - Files for 2025: Place in `weekly meetings/2025/` subdirectory
  - Files for 2026 onwards: Place in `weekly meetings/YYYY/` subdirectory
  - Keep root-level directory clean; migrate old files to year folders quarterly

### P2 Evaluation Files (`members/` and root)
- **Master Template:** `P2_Form_BP_Cong_Nghe.xlsx` (root, immutable)
- **Member Forms:** `P2_Form_BP_Cong_Nghe - {FirstName}.xlsx`
- **Naming Pattern:**
  - Full Vietnamese first name (as shown in examples: Đạt, Đức, Hổ, Chương, Hoàng)
  - Space before hyphen, space after hyphen (` - `)
  - .xlsx extension (Excel 2007+)
- **Examples:**
  - `P2_Form_BP_Cong_Nghe - Dat.xlsx` ✓
  - `P2_Form_BP_Cong_Nghe - Duc.xlsx` ✓
  - `P2_Form_BP_Cong_Nghe-Duc.xlsx` ✗ (missing spaces)
  - `P2-Duc.xlsx` ✗ (incomplete prefix)

### Configuration Files
- **Credentials:** `.env` (git-ignored, never commit)
  - Format: Key=Value pairs
  - Required keys: `MY_INET_SID`, `MY_INET_SSID`
  - Update monthly as sessions expire
- **.gitignore:** Standard template (no custom modifications needed)

### Automation Tools
- **Skill Files:** `.claude/okr-kpi-myinet/SKILL.md`
  - Frontmatter: name, description, license, version, argument-hint
  - Documentation format: Markdown with code blocks for examples
  - Usage examples: Show command-line patterns for users

## Meeting Notes Format

### File Structure
```markdown
## 📅 Tháng MM-YYYY
**Người tham dự:** Name1, Name2, Name3, ...

### 📝 Nội dung chính

- **MemberName:**
  - Task description (OKR)
  - Task description (KPI)
  - Additional context if needed

- **MemberName:**
  - Task description (KPI)
  - Task description (OKR)

### ✅ Hành động / Mục tiêu
- Bullet point 1
- Bullet point 2

---

## 📚 Đào tạo / Chia sẻ

- Tuần 1: Topic – Speaker
- Tuần 2: Topic – Speaker
- Tuần 3: Topic – Speaker
- Tuần 4: Topic – Speaker
```

### Requirements
1. **Header:** Include month/year as `## 📅 Tháng MM-YYYY`
2. **Attendees:** List at top with emoji, comma-separated names
3. **Content Organization:**
   - One member per bullet point
   - Group OKRs and KPIs by member
   - Use parenthetical notation `(OKR)` or `(KPI)` to distinguish type
   - Include Vietnamese task descriptions
4. **Action Items:** Dedicated section summarizing decisions & commitments
5. **Training:** Weekly session schedule with speaker assignment
6. **Language:** Vietnamese throughout (team communicates in Vietnamese)

### Example Entry (Correct Format)
```markdown
- **Hổ:**
  - 100% Design System (OKR)

- **Tuấn Anh:**
  - Cải thiện quy trình xử lý lạm dụng tự động (OKR)
  - Cải thiện hệ thống số hóa tài liệu (KPI)
```

## Excel (P2 Evaluation) Conventions

### Master Template (`P2_Form_BP_Cong_Nghe.xlsx`)
- **Ownership:** Immutable. Only Team Lead updates.
- **Use:** Template source for member-specific copies
- **Preservation:** Never modify directly; create member-specific files instead

### Member Evaluation Files
- **Creation:** Copy master template, rename to `P2_Form_BP_Cong_Nghe - {Name}.xlsx`
- **Personalization:**
  - Update member name, period, and role
  - Preserve all formulas and cell references
  - Do not reorganize columns or sheets
- **Data Entry:**
  - Score columns: P2-Core và P2-Delivery riêng biệt
  - **Công thức tổng:** `P2+ Tổng = (P2-Core × A) + (P2-Delivery × B)` (A, B là trọng số)
  - Summary cells: Auto-calculate via formulas (do not hard-code)
  - Notes/Comments: Plain text in designated cells
- **Review:** Before finalizing, check:
  - All formulas calculate correctly
  - No circular references
  - Scores within valid range
  - Required fields completed

### Excel File Organization (Typical Structure)
| Sheet | Purpose |
|-------|---------|
| Info | Member name, period, role, evaluation date |
| Criteria | Scoring breakdown by category (Kỹ năng, Kết quả, Hành vi, etc.) |
| Summary | Aggregated scores and delivery calculations |
| Notes | Comments from evaluator and member |

*Note: Verify actual sheet structure by opening P2_Form_BP_Cong_Nghe.xlsx*

## Documentation Standards

### Markdown Files in `docs/`
- **Encoding:** UTF-8
- **Line Endings:** LF (Unix style)
- **Sections:** Use H2 (`##`) or H3 (`###`), never H1 (`#`)
- **Tables:** Use pipe syntax; include header separator
- **Code Blocks:** Specify language for syntax highlighting
  ```markdown
  ```python
  # Example code
  ```
  ```
- **Links:**
  - Internal: Relative paths starting with `./` (e.g., `./project-roadmap.md`)
  - External: Full URLs with protocol (e.g., `https://my.inet.vn`)
- **Vietnamese Content:** Acceptable throughout; ensure consistency

### Project Documentation Files
| File | Audience | Update Frequency |
|------|----------|------------------|
| `project-overview-pdr.md` | Team Lead, Developers | Quarterly or after major changes |
| `codebase-summary.md` | All team members | After structural changes |
| `code-standards.md` | All team members | As conventions evolve |
| `project-roadmap.md` | Team Lead, Developers | Monthly at minimum |

## Environment Variables (`.env`)

### Required Variables
```bash
# my.inet.vn session authentication
MY_INET_SID=<session_id_value>
MY_INET_SSID=<secure_session_id_value>
```

### Security Rules
1. **Never commit** `.env` to git repository
2. **Store locally** on development machine only
3. **Update monthly** as sessions typically expire after 30 days
4. **Retrieve:** Browser DevTools → Application → Cookies → copy SID and SSID values
5. **Share:** Only via secure channels (1:1 message, not email/chat)

### Format
- One variable per line
- No spaces around `=` sign
- String values unquoted (unless containing spaces/special chars)
- Comments: Prefix with `#`

## Python Scripts (Archived)

### Location: `scripts/`
Python scripts (openpyxl) for bulk P2 evaluation updates, formula management, and data migration.

### If Reactivating Scripts
- **Python Version:** 3.8+
- **Dependencies:** openpyxl, pandas (optional)
- **Naming:** Use kebab-case: `update-p2-evaluations.py`
- **Error Handling:** Log failures, do not silently ignore
- **Testing:** Test on copy of P2 file before running on originals
- **Documentation:** Include docstring with usage example
- **Backups:** Always backup Excel files before running scripts

## API & Browser Automation Standards

### okr-kpi-myinet Skill
- **Language:** JavaScript (browser automation) + Claude AI
- **Scope:** Read meeting notes → Fill KPI forms on my.inet.vn
- **Authentication:** Cookie-based via `.env` (MY_INET_SID, MY_INET_SSID)
- **Error Handling:**
  - 403/404 response: Log error, skip member, notify user
  - Modal not appearing: Retry once, then report
  - Missing issue data: Ask user for clarification before proceeding
- **User Confirmation:** Always confirm before saving KPI entries (show draft, allow edits)
- **Logging:** Include timestamp and member name in output

### my.inet.vn Form Field Mapping
| Vietnamese Label | Field Purpose | Input Type |
|------------------|---------------|-----------|
| Chi tiết KPI | Links to GitHub issues | Multi-line text + issue picker |
| Mục tiêu | Objective statement | Short text (1-2 sentences) |
| Kết quả | Result/outcome achieved | Short text (1-2 sentences) |
| Ghi chú | Additional notes | Short text (optional) |

## Quality Checklist

Before committing changes:

### Meeting Notes
- [ ] File named `DD-MM-YYYY.md`
- [ ] Header includes month/year: `## 📅 Tháng MM-YYYY`
- [ ] All attendees listed
- [ ] Each member has task list with (OKR) or (KPI) labels
- [ ] Vietnamese language used
- [ ] Action items summarized
- [ ] Training schedule included

### P2 Evaluation Files
- [ ] File named `P2_Form_BP_Cong_Nghe - {Name}.xlsx`
- [ ] Copied from master template (preserves formulas)
- [ ] Member details filled in
- [ ] All scoring cells completed
- [ ] Summary formulas calculate without errors
- [ ] No circular references

### Documentation
- [ ] UTF-8 encoding, LF line endings
- [ ] No H1 headers in docs/ files (use H2+)
- [ ] Internal links are relative paths
- [ ] Code blocks have language specified
- [ ] Tables formatted correctly
- [ ] Spell-checked (Vietnamese or English)

### Code/Automation
- [ ] `.env` not committed (verify .gitignore includes it)
- [ ] Credentials not logged or printed
- [ ] User confirmations implemented for destructive operations
- [ ] Error messages are descriptive and actionable

## Glossary & Vietnamese Terms

| Term | Usage Context |
|------|---------------|
| OKR / Mục tiêu & Kết quả Chính | Strategic quarterly objectives assigned in meeting notes |
| KPI / Chỉ số hiệu suất | Performance metrics tracked on my.inet.vn |
| Mục tiêu | "Objective" - filled in KPI form |
| Kết quả | "Result" - outcome/achievement in KPI form |
| Ghi chú | "Notes" - optional comments in KPI form |
| Chi tiết KPI | "KPI Details" - supporting issue links |
| Trưởng phòng | "Department Head" - team lead role (Đạt) |
| Người tham dự | "Attendees" - meeting participants |
| Nội dung chính | "Main content" - agenda section |
| Hành động / Mục tiêu | "Action / Objective" - summary of decisions |
| Đào tạo / Chia sẻ | "Training / Sharing" - knowledge session schedule |

## Common Mistakes to Avoid

1. **Meeting Notes:** Using English instead of Vietnamese → Keep Vietnamese for consistency
2. **File Naming:** Inconsistent P2 file names → Always use `P2_Form_BP_Cong_Nghe - {Name}.xlsx`
3. **Excel:** Modifying master template → Always work with member-specific copies
4. **Environment:** Committing `.env` → Verify it's in .gitignore and never staged
5. **OKR/KPI Automation:** Assuming form fields are English → Use Vietnamese labels from actual UI
6. **Documentation:** Hardcoding info that changes → Use links to source files instead
7. **Meeting Organization:** Leaving files at root → Move to YYYY/ subfolder after meeting

## Update Frequency & Ownership

| Document | Owner | Frequency |
|----------|-------|-----------|
| Weekly meeting notes | Meeting lead | Weekly (as conducted) |
| P2 evaluation files | Team Lead + individual | Quarterly |
| Master P2 template | Team Lead | As needed (updates to criteria) |
| .env credentials | Team Lead | Monthly (session refresh) |
| Documentation (docs/) | Tech Team / Team Lead | Quarterly or after major changes |
| code-standards.md | Team Lead | As conventions evolve |
