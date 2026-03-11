# Cloud Panel Backend — Phase 2 OKR

**Date:** 2026-03-11 | **Project:** Cloud Panel | **Scope:** Backend (Phase 2 — Infrastructure Enhancement)
**Timeline:** Q1–Q2 2026 | **Source:** [development-roadmap.md](https://gitlabs.inet.vn/server-tools/server-tools-document/cloud-panel-project-management/-/blob/main/docs/development-roadmap.md)

---

## Context

Phase 1 (Core Platform) ~97% complete. Phase 2 gồm 8 features, target Q1–Q2 2026.
Milestones: M2.1 (Alert + Notification) → M2.2 (File Manager + Firewall) → M2.3 (Key Rotation + Sharing + Data Expansion).

**Stack:** Node.js + Express + TypeScript, MongoDB, TimescaleDB, Socket.IO, Go Agent.

---

## Objective 1: Xây dựng hệ thống Alert & Notification hoàn chỉnh

> Features: F-ALERT-01 (Alert Rule Engine) + F-NOTIF-01 (Notification Channels)

| # | Key Result | Đo lường |
|---|-----------|---------|
| KR1 | Hoàn thành API Alert Rule Engine: CRUD rule, threshold config (CPU/RAM/Disk/BW), severity levels (Critical/Warning/Log) | API deployed, unit test ≥80% |
| KR2 | Tích hợp ≥3 notification channels (Telegram Bot, Email SMTP, Slack/Discord) với routing theo severity | End-to-end test trên staging |
| KR3 | Alert engine xử lý real-time metrics từ agent, trigger alert ≤10s khi vượt threshold | Benchmark đạt SLA |

---

## Objective 2: Mở rộng khả năng quản lý server từ xa

> Features: F-FMGR-01 (File Manager) + F-FWDET-01 (Firewall Detection) + F-ADATA-01 (Agent Data Expansion)

| # | Key Result | Đo lường |
|---|-----------|---------|
| KR1 | File Manager API: upload/download/browse qua SSH session, hỗ trợ file ≤100MB | Test trên ≥3 OS (Ubuntu, CentOS, Debian) |
| KR2 | Firewall Detection API: detect iptables/ufw/nftables, trả current rules (read-only) | Chính xác trên ≥3 loại firewall |
| KR3 | Agent Data Expansion: thu thập dmidecode, service list, user list, login logs hàng ngày | Data lưu MongoDB, API query hoạt động |

---

## Objective 3: Nâng cao bảo mật & chất lượng API

> Features: F-ROT-01 (Key Rotation) + F-SHARE-01 (Server Sharing) + Security Hardening

| # | Key Result | Đo lường |
|---|-----------|---------|
| KR1 | Password/SSH Key Rotation: scheduled auto-renewal, auto-generate + encrypt (AES-256) | Rotation đúng schedule, 0 downtime |
| KR2 | Server Sharing API: share server/group với scoped permissions (view-only, execute, full) | RBAC test pass, ≥3 permission levels |
| KR3 | Postman Collection (JSON) cho toàn bộ Phase 2 endpoints + tài liệu API kèm theo; rate limiting & input validation (Zod) trên tất cả routes mới | Collection exported, 0 endpoint thiếu validation |

---

## Notes

- Ưu tiên Objective 1 nếu chỉ chọn 1 — ROI cao nhất, foundation cho monitoring toàn hệ thống
- Dependency: Alert Engine (2.1) trước → Notification Channels (2.2) phụ thuộc vào nó
- Phase 1 cần hoàn thành 100% trước khi bắt tay Phase 2
- Feature F-XFER-01 (Transfer Server) đã loại khỏi OKR này, thay bằng API docs & security hardening
