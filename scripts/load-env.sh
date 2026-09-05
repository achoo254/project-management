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
