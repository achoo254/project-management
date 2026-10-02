#!/usr/bin/env bash
# Nạp credentials my.inet.vn + GitLab từ iCloud Drive vào môi trường shell hiện tại.
#
# Secret KHÔNG nằm trong repo: file sống ở iCloud Drive nên đồng bộ sẵn giữa các
# máy của cùng một người và không bao giờ có nguy cơ bị commit nhầm.
#
# iCloud Drive nằm ở vị trí khác nhau tuỳ hệ điều hành, nên script dò lần lượt
# các vị trí đã biết (macOS, Windows/Git Bash) và dừng ở file đầu tiên tồn tại.
# Máy có đường dẫn lạ thì đặt sẵn INET_ENV_FILE trước khi source.
#
# Cookie SSO inet.vn ($sid $ssid) lấy từ access-tokens.json (entry service "inet.vn",
# type "session-cookie") — sổ token chung trên iCloud Drive; giá trị trong file env chỉ
# còn là dự phòng khi chưa có entry đó. Máy có đường dẫn lạ thì đặt sẵn ACCESS_TOKENS_JSON.
#
# Dùng:  source scripts/load-env.sh
# Sau đó có sẵn: $sid $ssid $GITLABS_USERNAME $GITLABS_EMAIL $GITLABS_ACCESS_TOKEN

INET_ENV_CANDIDATES=(
  "$HOME/Library/Mobile Documents/com~apple~CloudDocs/secrets/inet-project-management.env"  # macOS
  "$HOME/iCloudDrive/secrets/inet-project-management.env"                                   # Windows (Git Bash)
  "$USERPROFILE/iCloudDrive/secrets/inet-project-management.env"                            # Windows (USERPROFILE khác HOME)
)

if [ -z "${INET_ENV_FILE:-}" ]; then
  for candidate in "${INET_ENV_CANDIDATES[@]}"; do
    if [ -f "$candidate" ]; then
      INET_ENV_FILE="$candidate"
      break
    fi
  done
fi

if [ -z "${INET_ENV_FILE:-}" ] || [ ! -f "$INET_ENV_FILE" ]; then
  echo "ERROR: không tìm thấy credentials tại các vị trí đã biết:" >&2
  for candidate in "${INET_ENV_CANDIDATES[@]}"; do
    echo "  $candidate" >&2
  done
  echo "Tạo file đó theo mẫu .env.example (iCloud Drive sẽ tự đồng bộ sang máy khác)," >&2
  echo "hoặc đặt INET_ENV_FILE=<đường dẫn> trước khi source script này." >&2
  return 1 2>/dev/null || exit 1
fi

set -a
# shellcheck disable=SC1090
. "$INET_ENV_FILE"
set +a

ACCESS_TOKENS_CANDIDATES=(
  "$HOME/Library/Mobile Documents/com~apple~CloudDocs/cong-viec/Cong viec/ENV production/access-tokens.json"  # macOS
  "$HOME/iCloudDrive/cong-viec/Cong viec/ENV production/access-tokens.json"                                   # Windows (Git Bash)
  "$USERPROFILE/iCloudDrive/cong-viec/Cong viec/ENV production/access-tokens.json"                            # Windows (USERPROFILE khác HOME)
)

if [ -z "${ACCESS_TOKENS_JSON:-}" ]; then
  for candidate in "${ACCESS_TOKENS_CANDIDATES[@]}"; do
    if [ -f "$candidate" ]; then
      ACCESS_TOKENS_JSON="$candidate"
      break
    fi
  done
fi

if [ -n "${ACCESS_TOKENS_JSON:-}" ] && [ -f "$ACCESS_TOKENS_JSON" ] && command -v jq >/dev/null 2>&1; then
  INET_SSO_FILTER='.tokens[]|select(.service=="inet.vn" and .type=="session-cookie")|.token'
  inet_sid="$(jq -r "$INET_SSO_FILTER.sid // empty" "$ACCESS_TOKENS_JSON")"
  inet_ssid="$(jq -r "$INET_SSO_FILTER.ssid // empty" "$ACCESS_TOKENS_JSON")"
  if [ -n "$inet_sid" ] && [ -n "$inet_ssid" ]; then
    export sid="$inet_sid" ssid="$inet_ssid"
  else
    echo "WARNING: access-tokens.json chưa có cookie inet.vn (sid/ssid) — dùng giá trị trong $INET_ENV_FILE." >&2
  fi
  unset inet_sid inet_ssid INET_SSO_FILTER
else
  echo "WARNING: không đọc được access-tokens.json (thiếu file hoặc jq) — sid/ssid lấy từ $INET_ENV_FILE." >&2
fi
