# Cloud Panel Backend — Phase 2 OKR

**Date:** 2026-03-11 | **Project:** Cloud Panel | **Scope:** Backend (Phase 2 — Infrastructure Enhancement)
**Timeline:** Q1–Q2 2026 | **Source:** [development-roadmap.md](https://gitlabs.inet.vn/server-tools/server-tools-document/cloud-panel-project-management/-/blob/main/docs/development-roadmap.md)

---

## Context

Phase 1 (Core Platform) ~97% complete. Phase 2 gồm 8 features, target Q1–Q2 2026.
Milestones: M2.1 (Alert + Notification) → M2.2 (File Manager + Firewall) → M2.3 (Key Rotation + Sharing + Data Expansion).

**Stack:** Node.js + Express + TypeScript, MongoDB, TimescaleDB, Socket.IO, Go Agent.

---

## Objective 1: Xay dung he thong Alert & Notification hoan chinh

> Features: F-ALERT-01 (Alert Rule Engine) + F-NOTIF-01 (Notification Channels)

| # | Key Result | Do luong |
|---|-----------|---------|
| KR1 | Hoan thanh API Alert Rule Engine: CRUD rule, threshold config (CPU/RAM/Disk/BW), severity levels (Critical/Warning/Log) | API deployed, unit test ≥80% |
| KR2 | Tich hop ≥3 notification channels (Telegram Bot, Email SMTP, Slack/Discord) voi routing theo severity | End-to-end test tren staging |
| KR3 | Alert engine xu ly real-time metrics tu agent, trigger alert ≤10s khi vuot threshold | Benchmark dat SLA |

---

## Objective 2: Mo rong kha nang quan ly server tu xa

> Features: F-FMGR-01 (File Manager) + F-FWDET-01 (Firewall Detection) + F-ADATA-01 (Agent Data Expansion)

| # | Key Result | Do luong |
|---|-----------|---------|
| KR1 | File Manager API: upload/download/browse qua SSH session, ho tro file ≤100MB | Test tren ≥3 OS (Ubuntu, CentOS, Debian) |
| KR2 | Firewall Detection API: detect iptables/ufw/nftables, tra current rules (read-only) | Chinh xac tren ≥3 loai firewall |
| KR3 | Agent Data Expansion: thu thap dmidecode, service list, user list, login logs hang ngay | Data luu MongoDB, API query hoat dong |

---

## Objective 3: Nang cao bao mat & chat luong API

> Features: F-ROT-01 (Key Rotation) + F-SHARE-01 (Server Sharing) + Security Hardening

| # | Key Result | Do luong |
|---|-----------|---------|
| KR1 | Password/SSH Key Rotation: scheduled auto-renewal, auto-generate + encrypt (AES-256) | Rotation dung schedule, 0 downtime |
| KR2 | Server Sharing API: share server/group voi scoped permissions (view-only, execute, full) | RBAC test pass, ≥3 permission levels |
| KR3 | Postman Collection (JSON) cho toan bo Phase 2 endpoints + tai lieu API kem theo; rate limiting & input validation (Zod) tren tat ca routes moi | Collection exported, 0 endpoint thieu validation |

---

## Notes

- Uu tien Objective 1 neu chi chon 1 — ROI cao nhat, foundation cho monitoring toan he thong
- Dependency: Alert Engine (2.1) truoc → Notification Channels (2.2) phu thuoc vao no
- Phase 1 can hoan thanh 100% truoc khi bat tay Phase 2
- Feature F-XFER-01 (Transfer Server) da loai khoi OKR nay, thay bang API docs & security hardening
