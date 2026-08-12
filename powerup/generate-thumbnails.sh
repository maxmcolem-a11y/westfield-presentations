#!/bin/zsh
set -euo pipefail

repo_dir="${0:A:h:h}"
output_dir="$repo_dir/powerup/thumbnails"
chrome_bin="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
port="${THUMBNAIL_PORT:-$(python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1]); s.close()')}"

if [[ ! -x "$chrome_bin" ]]; then
  print -u2 "Google Chrome was not found at $chrome_bin"
  exit 1
fi

mkdir -p "$output_dir"
tmp_dir="$(mktemp -d)"
server_log="$tmp_dir/http.log"

cleanup() {
  if [[ -n "${server_pid:-}" ]]; then
    kill "$server_pid" 2>/dev/null || true
  fi
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

cd "$repo_dir"
python3 -m http.server "$port" --bind 127.0.0.1 >"$server_log" 2>&1 &
server_pid=$!

server_ready=false
for _ in {1..40}; do
  if curl -fsS "http://127.0.0.1:$port/index.html" >/dev/null; then
    server_ready=true
    break
  fi
  sleep 0.1
done

if [[ "$server_ready" != true ]]; then
  print -u2 "Thumbnail HTTP server did not start on port $port"
  cat "$server_log" >&2
  exit 1
fi

if (( $# )); then
  presentation_paths=("$@")
else
  presentation_paths=(${(f)$(find . -mindepth 2 -maxdepth 3 -name index.html -print | sed 's#^./##' | sort)})
fi

for presentation_path in "${presentation_paths[@]}"; do
  clean_path="${presentation_path%%\?*}"
  clean_path="${clean_path#/}"
  [[ "$clean_path" == powerup/* ]] && continue
  if [[ "$clean_path" == */ ]]; then
    clean_path="${clean_path}index.html"
  fi
  [[ -f "$clean_path" ]] || { print -u2 "Presentation not found: $clean_path"; exit 1; }

  slug="${clean_path%/index.html}"
  slug="${slug%.html}"
  filename="${slug//\//--}"

  full_png="$tmp_dir/$filename.png"
  thumbnail="$output_dir/$filename.jpg"
  "$chrome_bin" \
    --headless=new \
    --disable-gpu \
    --disable-dev-shm-usage \
    --hide-scrollbars \
    --no-first-run \
    --no-default-browser-check \
    --user-data-dir="$tmp_dir/chrome-$filename" \
    --window-size=1920,1080 \
    --virtual-time-budget=2500 \
    --screenshot="$full_png" \
    "http://127.0.0.1:$port/$clean_path" >/dev/null 2>&1 &
  chrome_pid=$!

  capture_ready=false
  for _ in {1..200}; do
    if [[ -s "$full_png" ]]; then
      capture_ready=true
      break
    fi
    if ! kill -0 "$chrome_pid" 2>/dev/null; then
      break
    fi
    sleep 0.1
  done
  kill "$chrome_pid" 2>/dev/null || true
  wait "$chrome_pid" 2>/dev/null || true

  if [[ "$capture_ready" != true ]]; then
    print -u2 "Capture failed: $clean_path"
    exit 1
  fi

  sips --resampleHeightWidth 189 336 --setProperty format jpeg \
    --setProperty formatOptions 72 "$full_png" --out "$thumbnail" >/dev/null
  chmod 0644 "$thumbnail"
  print "generated $thumbnail"
done
