# Environment Configuration Guide

Guide for setting up `.env` files across all sub-repos. **NEVER commit `.env` files to git.**

---

## File Naming Convention

```
.env.<NODE_ENV>          # Standard environment (development, staging)
.env.<username>          # Per-developer config (dattqh, ducnd)
```

Backend/Resource load env via: `.env` (base) -> `.env.${NODE_ENV}` (override).
Run per-developer config with: `pnpm <username>` (e.g. `pnpm dattqh`).

---

## Backend (`server-tools-backend/`)

### Core

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3000` |
| `NODE_ENV` | Environment name | `development` |
| `BASE_URL` | API base URL | `http://localhost:${PORT}` |
| `TRUST_PROXY` | Trust X-Forwarded-For header | `false` |
| `IP_SERVER` | Public IP of this server | — |
| `LOG_LEVEL` | Winston log level | `info` |

### SSO Authentication

| Variable | Description | Example |
|----------|-------------|---------|
| `SSO_INET_REQUEST` | SSO base URL | `https://sso.inet.vn` |
| `PATH_VERIFY_SID_REQUEST` | SSO verify SID endpoint path | `/api/...` |
| `PATH_CHECK_SESSION_ACTIVE_REQUEST` | SSO check session endpoint path | `/api/...` |
| `ACCOUNT_SUPER_ADMIN` | Space-separated super admin emails | `admin@inet.vn` |

### MongoDB

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_NAME` | Database name | — |
| `DB_HOST_NAME` | MongoDB host | — |
| `DB_PORT` | MongoDB port | `27017` |
| `DB_USER_NAME` | MongoDB username | — |
| `DB_PASSWORD` | MongoDB password | — |
| `STORAGE_TYPE` | Storage backend | `mongodb` |

### TimescaleDB (Metrics)

| Variable | Description | Default |
|----------|-------------|---------|
| `TIMESCALEDB_HOST` | TimescaleDB host | `localhost` |
| `TIMESCALEDB_PORT` | TimescaleDB port | `5432` |
| `TIMESCALEDB_DATABASE` | Database name | — |
| `TIMESCALEDB_USER` | DB username | — |
| `TIMESCALEDB_PASSWORD` | DB password | — |

### Encryption Keys

| Variable | Description | Notes |
|----------|-------------|-------|
| `CREDENTIAL_ENCRYPTION_KEY` | AES-256-GCM key for SSH credentials | **Required.** Must be consistent across deployments |
| `TOKEN_ENCRYPTION_KEY` | Key for SSO token cache encryption | **Required.** |
| `PRIVATE_KEY_AUTH` | JWT/auth private key | **Required.** |

### Telegram Notifications

| Variable | Description | Example |
|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | System alert bot token | `7131184196:AAErl...` |
| `TELEGRAM_CHAT_ID` | System alert chat/group ID | `1587073536` |
| `TELEGRAM_TOPIC_ID` | Forum topic ID (optional) | `123` |
| `SSH_WATCH_TELEGRAM_BOT_TOKEN` | SSH Watch notification bot (separate bot) | `8764774498:AAF5k...` |

### Agent Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `AGENT_LATEST_VERSION` | Latest agent binary version | `1.0.0` |
| `AGENT_HEARTBEAT_INTERVAL` | Heartbeat interval (seconds, 1-3600) | `30` |
| `AGENT_COMMAND_POLL_INTERVAL` | Command poll interval (seconds, 1-3600) | `10` |
| `AGENT_METRICS_INTERVAL` | Metrics collection interval (seconds, 1-3600) | `60` |
| `AGENT_METRICS_HISTORY_STREAM_INTERVAL_SEC` | SSE metrics push interval (seconds, 1-300) | `3` |
| `AGENT_GATEWAY` | Gateway URL for agents | — |

### Resource Service

| Variable | Description | Default |
|----------|-------------|---------|
| `RESOURCE_SERVICE_URL` | Internal URL to resource server | `http://localhost:8004` |
| `RESOURCE_PUBLIC_URL` | Public URL for download links | Falls back to `RESOURCE_SERVICE_URL` |
| `RAT_SIGNING_ALG` | RAT token algorithm | `HS256` |
| `RAT_SIGNING_SECRET` | RAT signing secret (HS256) | — |
| `RAT_SIGNING_PRIVATE_KEY` | RAT private key (RS256, optional) | — |
| `RESOURCE_SERVICE_AUTH_SECRET` | Shared auth secret with resource server | — |

### Socket.IO

| Variable | Description | Default |
|----------|-------------|---------|
| `SOCKET_CORS_ORIGIN` | CORS origins | `*` |
| `SOCKET_CONNECT_TIMEOUT` | Connection timeout (ms) | `45000` |
| `SOCKET_PING_INTERVAL` | Ping interval (ms) | `25000` |
| `SOCKET_PING_TIMEOUT` | Ping timeout (ms) | `20000` |
| `SOCKET_MAX_HTTP_BUFFER_SIZE` | Max HTTP buffer | `1e6` |
| `SOCKET_TRANSPORTS` | Transport methods | `websocket,polling` |
| `SOCKET_PER_MESSAGE_DEFLATE` | Enable compression | `true` |
| `SOCKET_DEFLATE_THRESHOLD` | Compression threshold (bytes) | `1024` |
| `SOCKET_ALLOW_EIO3` | Allow Engine.IO v3 | `false` |
| `SOCKET_RATE_LIMIT_ENABLED` | Enable rate limiting | `true` |
| `SOCKET_RATE_LIMIT_CAPACITY` | Rate limit bucket size | `100` |
| `SOCKET_RATE_LIMIT_REFILL_RATE` | Refill rate per second | `10` |
| `SOCKET_RATE_LIMIT_EVENTS` | Events to rate limit | `message,send,emit` |
| `SOCKET_RATE_LIMIT_DISCONNECT` | Disconnect on limit | `false` |
| `SOCKET_ROOM_LIMIT_ENABLED` | Enable room limits | `false` |
| `SOCKET_ROOM_LIMIT_MAX_USERS` | Max users per room | `100` |

### File Upload & CI/CD

| Variable | Description | Default |
|----------|-------------|---------|
| `UPLOAD_TEMP_TEMPLATE_DIR` | Temporary template directory | `uploads/temp/template` |
| `GITLABS_USERNAME` | GitLabs username (CI/CD) | — |
| `GITLABS_EMAIL` | GitLabs email (CI/CD) | — |
| `GITLABS_ACCESS_TOKEN` | GitLabs **Project Access Token** (CI/CD). **NOT a User/Personal Access Token.** Each project must use its own project-scoped token. | — |
| `GITLAB_ACCESS_TOKEN` | GitLab **Project Access Token** for CI/CD pipeline notifications (read_api scope). Configured as CI/CD variable per project. | — |

> **Important — GitLab Access Tokens:**
> - All GitLab access tokens in this system are **Project Access Tokens**, NOT User/Personal Access Tokens.
> - Each project (backend, client, resource) must have its own Project Access Token configured in **Settings → Access Tokens** on GitLab.
> - CI/CD pipelines use project-level API endpoints (`/api/v4/projects/:id/...`), so the token must be scoped to the correct project.
> - Required scope: `read_api` (for pipeline job details and failure notifications).

---

## Client (`server-tools-client/`)

Client runs in browser/Electron. Configuration is build-time via Vite. Only `VITE_`-prefixed vars are bundled.

### Build Environment Variables

Inject at build time via `.env.staging`, `.env.production`:

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_BACKEND_URL` | Backend API base URL | `http://localhost:8003` |
| `VITE_SOCKET_URL` | Socket.IO server URL | Window origin |
| `VITE_APP_TITLE` | Application title | `Cloud Panel Client` |
| `VITE_APP_ENV` | Environment mode | Vite mode |
| `VITE_AGENT_LATEST_VERSION` | Default agent binary version | `v1.0.1` |
| `VITE_DEV_PORT` | Dev server port | `5173` |
| `VITE_TELEGRAM_BOT_CODE` | Telegram bot code (external) | — |
| `VITE_TELEGRAM_BOT_CODE_NB` | Telegram bot code (internal network) | — |
| `VITE_TELEGRAM_BOT_USERNAME` | Telegram bot username | `cloudpanel_bot` |

### Development-Only Variables

| Variable | Description | Security |
|----------|-------------|----------|
| `VITE_MOCK_SID` | Mock session ID for dev/testing | Blanked in non-dev builds |
| `VITE_MOCK_SSID` | Mock secure session ID for dev/testing | Blanked in non-dev builds |

### Development (Vite Dev Server)

During `pnpm dev`, Vite proxies `/api`, `/public`, `/socket.io` to `VITE_BACKEND_URL`:
```bash
pnpm dev
# Vite dev server on http://localhost:5173
# Proxies /api -> http://localhost:8003
```

### Environment Helper

Client uses centralized config via `src/utils/env.ts`:
- `getEnv(key, defaultValue)` - String with fallback
- `getEnvBoolean(key, defaultValue)` - Boolean parsing
- `getEnvNumber(key, defaultValue)` - Number parsing
- `appConfig` - Centralized configuration object

---

## Agent (`server-tools-agent/`)

Agent reads environment on startup. Deploy via systemd/docker with `.env` file or environment variables. Config precedence: JSON config file > environment variables.

### Server Configuration

| Variable | Default | Purpose |
|----------|---------|---------|
| `SERVER_HOST` | `0.0.0.0` | HTTP server bind address |
| `SERVER_PORT` | `8080` | HTTP server port |
| `SERVER_ENABLED` | `false` | Enable/disable HTTP server |

### Identity & Authentication

| Variable | Default | Purpose |
|----------|---------|---------|
| `AGENT_ID` | — | **Required.** Unique agent identifier |
| `AGENT_NAME` | `server-tools-agent` | Agent display name |
| `AGENT_VERSION` | `1.0.0` | Agent version (overrideable via build flag) |
| `AGENT_TOKEN` | — | **Required.** Agent auth token |
| `ENVIRONMENT` | `dev` | Environment context (dev/staging/production) |

### Backend Communication

| Variable | Default | Purpose |
|----------|---------|---------|
| `BACKEND_URL` | `http://localhost:3000` | Backend API endpoint URL |
| `BACKEND_API_KEY` | — | Auth key for backend communication |
| `BACKEND_TIMEOUT` | `30` | Backend request timeout (seconds) |
| `GATEWAY_ENDPOINT` | — | Gateway endpoint URL (alternative to BACKEND_URL) |

### Timing & Polling Intervals

| Variable | Default | Purpose |
|----------|---------|---------|
| `HEARTBEAT_INTERVAL` | `30` | Heartbeat send interval (seconds) |
| `SERVER_INFO_INTERVAL` | `300` | Server inventory send interval (seconds) |
| `COMMAND_POLL_INTERVAL` | `10` | Command polling interval (seconds) |
| `METRICS_INTERVAL` | `60` | Metrics collection interval (seconds) |

### Auto-Update Settings

| Variable | Default | Purpose |
|----------|---------|---------|
| `UPDATE_ENABLED` | `true` | Enable auto-update mechanism |
| `AUTO_UPDATE` | `auto` | Auto-update mode (`auto` or `manual`) |
| `UPDATE_AUTO_UPDATE` | `false` | Auto-apply updates without manual approval |
| `UPDATE_CHECK_INTERVAL` | `60` | Check for updates every N minutes |
| `UPDATE_ENDPOINT` | `/version/check` | Endpoint path for update checks |
| `UPDATE_BACKUP_DIR` | `/opt/cloud-panel-agent/backups` | Backup directory for rollback |
| `UPDATE_ROLLBACK_ON_ERROR` | `true` | Rollback to previous binary if update fails |

### Logging

| Variable | Default | Purpose |
|----------|---------|---------|
| `LOG_LEVEL` | `info` | Log level (debug, info, warn, error) |
| `LOG_DIR` | `/opt/cloud-panel-agent/logs` | Agent log directory |
| `LOG_RETENTION_DAYS` | `7` | Log file retention period (days) |
| `LOG_CLEANUP_INTERVAL_HOURS` | `24` | Log cleanup check interval (hours) |

### Command Log Streaming

| Variable | Default | Purpose |
|----------|---------|---------|
| `COMMAND_LOG_LOCAL_DIR` | `/var/log/cloud-panel-agent/commands` | Local command log directory |
| `COMMAND_LOG_BATCH_SIZE` | `8192` | Command log batch size (bytes) |
| `COMMAND_LOG_FLUSH_INTERVAL` | `500` | Log flush interval (ms) |
| `COMMAND_LOG_RETENTION_DAYS` | `7` | Command log retention (days) |

### SSH Watch & Monitoring (Linux only)

| Variable | Default | Purpose |
|----------|---------|---------|
| `SSHWATCH_ENABLED` | `false` | Enable SSH connection monitoring |
| `SSHWATCH_LOG_LEVEL` | `WARNING` | SSHWatch log level (DEBUG/INFO/WARNING/ERROR/CRITICAL) |
| `SSHWATCH_API_URL` | Derives from `BACKEND_URL` | SSH log ingestion endpoint |
| `AGENT_DISABLE_NODE_EXPORTER` | — | Set to `1` to disable node_exporter metrics |

### Installation & Paths

| Variable | Default | Purpose |
|----------|---------|---------|
| `INSTALL_DIR` | `/opt/cloud-panel-agent` | Agent installation directory |

### Example Agent `.env` File
```bash
# Identity
AGENT_ID=agent-prod-db01
AGENT_TOKEN=ABC123DEF456...
ENVIRONMENT=production

# Server
SERVER_HOST=0.0.0.0
SERVER_PORT=8080
SERVER_ENABLED=true

# Backend
BACKEND_URL=https://api.cloudpanel.inet.vn
BACKEND_TIMEOUT=30

# Heartbeat & Metrics
HEARTBEAT_INTERVAL=30
METRICS_INTERVAL=60
COMMAND_POLL_INTERVAL=10

# Updates
UPDATE_ENABLED=true
UPDATE_AUTO_UPDATE=false
UPDATE_CHECK_INTERVAL=60
UPDATE_ROLLBACK_ON_ERROR=true

# Logging
LOG_LEVEL=info
LOG_DIR=/opt/cloud-panel-agent/logs

# SSH Watch (Linux only)
SSHWATCH_ENABLED=true
SSHWATCH_LOG_LEVEL=WARNING
```

---

## Resource Server (`cloud-panel-resource/`)

Hosts agent binaries, templates, and GeoIP data. Configure via `.env`:

### Core

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3001` |
| `NODE_ENV` | Runtime environment | `development` |
| `LOG_LEVEL` | Winston log level | `info` |

### MongoDB

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_URI` / `MONGODB_URI` | Full MongoDB connection URI (takes precedence) | `mongodb://localhost:27017` |
| `DB_HOST_NAME` | MongoDB host (fallback) | — |
| `DB_PORT` | MongoDB port (fallback) | `27017` |
| `DB_USER_NAME` | MongoDB username (fallback) | — |
| `DB_PASSWORD` | MongoDB password (fallback) | — |
| `MONGO_DB_NAME` / `DB_NAME` | Database name | `cloud-panel-resource` |

Connection precedence: `MONGO_URI` > component auth (`DB_HOST_NAME`+credentials) > `mongodb://localhost:27017`.

### Authentication (RAT)

| Variable | Description | Default |
|----------|-------------|---------|
| `RAT_SIGNING_ALG` | Resource Access Token algorithm | `HS256` |
| `RAT_SIGNING_SECRET` | RAT signing secret (HS256) | — |
| `RAT_JWKS_URL` | JWKS endpoint for RAT verification (alternative) | — |
| `RESOURCE_SERVICE_AUTH_SECRET` | Shared secret with backend | — |

### File Storage

| Variable | Description | Default |
|----------|-------------|---------|
| `AGENT_FOLDER` | Agent binaries folder | `agent` |
| `GEO_DATA_FOLDER` | GeoLite2 MMDB files folder | `geo-data` |

### MaxMind GeoIP

| Variable | Description | Notes |
|----------|-------------|-------|
| `MAXMIND_ACCOUNT_ID` | MaxMind account ID | Both required for auto-update |
| `MAXMIND_LICENSE_KEY` | MaxMind license key | Auto-update runs daily if both set |

### Telegram Notifications

| Variable | Description | Default |
|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | — |
| `TELEGRAM_CHAT_ID` | Telegram chat/channel ID | — |
| `TELEGRAM_TOPIC_ID` | Forum topic ID (optional) | `0` |

---

## Security Rules

1. **NEVER** commit `.env` files — they are in `.gitignore`
2. **NEVER** log or expose encryption keys, passwords, or tokens in responses
3. Encryption keys (`CREDENTIAL_ENCRYPTION_KEY`, `TOKEN_ENCRYPTION_KEY`) must match across all instances sharing the same DB — changing them invalidates existing encrypted data
4. Use single quotes around passwords with special characters: `DB_PASSWORD='P@ss&word'`
5. Each developer maintains their own `.env.<username>` file locally
6. `VITE_MOCK_SID`/`VITE_MOCK_SSID` are automatically blanked in non-dev builds

---

## Quick Start Template

```bash
# Copy from a teammate's env (without sensitive values) or create fresh:
cp .env.example .env.<your-username>

# Backend — minimum required values:
PORT=8003
DB_NAME=server_tools_v2_db
DB_HOST_NAME=127.0.0.1
DB_PORT=27017
DB_USER_NAME=...
DB_PASSWORD='...'
SSO_INET_REQUEST=https://sso.inet.vn
CREDENTIAL_ENCRYPTION_KEY=...
TOKEN_ENCRYPTION_KEY=...
PRIVATE_KEY_AUTH=...
```
