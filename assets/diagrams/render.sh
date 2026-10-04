#!/bin/zsh
# Renderiza los SVG de esta carpeta a PNG (2x) en src/media/ con Chrome headless.
# Uso: ./render.sh [nombre.svg ...]   (sin argumentos: todos)
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/../../src/media"
files=("$@")
[ ${#files[@]} -eq 0 ] && files=("$DIR"/*.svg)
for f in $files; do
  f="${f:A}"
  name=$(basename "$f" .svg)
  w=$(grep -o 'width="[0-9]*"' "$f" | head -1 | grep -o '[0-9]*')
  h=$(grep -o 'height="[0-9]*"' "$f" | head -1 | grep -o '[0-9]*')
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=$w,$h \
    --screenshot="$OUT/$name.png" "file://$f" 2>/dev/null
  echo "$name.png ($((w*2))x$((h*2)))"
done
