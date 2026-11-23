#!/usr/bin/env python3
"""Read-only offline QA: source matches downloadable .deb exactly."""
from pathlib import Path
import hashlib
import subprocess
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src'
VERSION = next(line.split(': ', 1)[1] for line in (SOURCE / 'debian/control').read_text().splitlines()
               if line.startswith('Version: '))
DEB = ROOT / 'packages' / f'mbp132-support_{VERSION}_all.deb'


def cmd(*args):
    return subprocess.check_output(args, text=True).strip()


checksums = {name: digest for digest, name in
             (line.split() for line in (DEB.parent / 'SHA256SUMS').read_text().splitlines())}
for package in DEB.parent.glob('*.deb'):
    assert hashlib.sha256(package.read_bytes()).hexdigest() == checksums[package.name], package
if len(sys.argv) > 1:
    DEB = Path(sys.argv[1]).resolve()
assert DEB.is_file(), f'Package missing: {DEB}'
assert cmd('dpkg-deb', '-f', str(DEB), 'Package') == 'mbp132-support'
assert cmd('dpkg-deb', '-f', str(DEB), 'Version') == VERSION
assert cmd('dpkg-deb', '-f', str(DEB), 'Architecture') == 'all'

with tempfile.TemporaryDirectory() as tmp:
    extracted = Path(tmp) / 'payload'
    controls = Path(tmp) / 'meta'
    subprocess.run(['dpkg-deb', '-x', str(DEB), str(extracted)], check=True)
    subprocess.run(['dpkg-deb', '-e', str(DEB), str(controls)], check=True)
    for source_dir, target_dir in [(SOURCE / 'debian', controls), (SOURCE / 'usr', extracted / 'usr'),
                                  (SOURCE / 'etc', extracted / 'etc')]:
        source_files = {p.relative_to(source_dir) for p in source_dir.rglob('*') if p.is_file()}
        target_files = {p.relative_to(target_dir) for p in target_dir.rglob('*') if p.is_file()}
        assert source_files == target_files, f'Unexpected or missing files in {source_dir}'
        for rel in source_files:
            source, target = source_dir / rel, target_dir / rel
            assert source.read_bytes() == target.read_bytes(), f'Package content differs: {rel}'
            mode = 0o755 if source.stat().st_mode & 0o111 else 0o644
            assert target.stat().st_mode & 0o7777 == mode, f'Package permissions differ: {rel}'
print(f'PASS: {VERSION} checksums, metadata, contents and permissions')
