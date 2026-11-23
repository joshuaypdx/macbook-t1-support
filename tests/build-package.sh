#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
stage=$(mktemp -d)
trap 'rm -rf -- "$stage"' EXIT
mkdir -m 0755 "$stage/root"
cp -a src/{etc,usr} "$stage/root/"
cp -a src/debian "$stage/root/DEBIAN"
find "$stage/root" -type d -exec chmod 0755 {} +
find "$stage/root" -type f ! -perm /111 -exec chmod 0644 {} +
find "$stage/root" -type f -perm /111 -exec chmod 0755 {} +
version=$(sed -n 's/^Version: //p' src/debian/control)
export SOURCE_DATE_EPOCH=0
find "$stage/root" -exec touch -h -d "@$SOURCE_DATE_EPOCH" {} +
dpkg-deb --root-owner-group -Zxz -z9 --build "$stage/root" "${1:-packages/mbp132-support_${version}_all.deb}"
