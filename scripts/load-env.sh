#!/usr/bin/env bash
# Nạp credentials my.inet.vn + GitLab từ iCloud Drive vào môi trường shell hiện tại.
#
# Secret KHÔNG nằm trong repo: file sống ở iCloud Drive nên đồng bộ sẵn giữa các
# máy của cùng một người và không bao giờ có nguy cơ bị commit nhầm.
#
# Dùng:  source scripts/load-env.sh
# Sau đó có sẵn: $sid $ssid $GITLABS_USERNAME $GITLABS_EMAIL $GITLABS_ACCESS_TOKEN

INET_ENV_FILE="$HOME/Library/Mobile Documents/com~apple~CloudDocs/secrets/inet-project-management.env"

if [ ! -f "$INET_ENV_FILE" ]; then
  echo "ERROR: không tìm thấy credentials tại:" >&2
  echo "  $INET_ENV_FILE" >&2
  echo "Tạo file đó theo mẫu .env.example (iCloud Drive sẽ tự đồng bộ sang máy khác)." >&2
  return 1 2>/dev/null || exit 1
fi

set -a
# shellcheck disable=SC1090
. "$INET_ENV_FILE"
set +a
