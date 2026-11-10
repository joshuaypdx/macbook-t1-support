#!/usr/bin/env python3
"""Read-only offline QA: source matches downloadable .deb exactly."""
from pathlib import Path
import hashlib
import subprocess
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]
DEB = ROOT / 'packages' / 'mbp132-support_0.5.0_all.deb'
SOURCE = ROOT / 'src'
EXPECTED_SHA = '4e6a372db887b575649f60d1b17a00a7900ff8ed975143b71a43d74662b7d09b'


def cmd(*args):
    return subprocess.check_output(args, text=True).strip()


assert DEB.is_file(), f'Package missing: {DEB}'
assert hashlib.sha256(DEB.read_bytes()).hexdigest() == EXPECTED_SHA, 'Published beta .deb differs from real-hardware-tested binary. Refuse release until tested version/checksum are updated.'
assert cmd('dpkg-deb', '-f', str(DEB), 'Package') == 'mbp132-support'
assert cmd('dpkg-deb', '-f', str(DEB), 'Version') == '0.5.0'

with tempfile.TemporaryDirectory() as tmp:
    extracted = Path(tmp) / 'payload'
    controls = Path(tmp) / 'meta'
    subprocess.run(['dpkg-deb', '-x', str(DEB), str(extracted)], check=True)
    subprocess.run(['dpkg-deb', '-e', str(DEB), str(controls)], check=True)
    checked = 0
    for file in SOURCE.rglob('*'):
        if not file.is_file() or file.relative_to(SOURCE).parts[0] == 'tests':
            continue
        rel = file.relative_to(SOURCE)
        if rel.parts[0] == 'debian':
            counterpart = controls / rel.name
        elif rel.parts[0] in ('usr', 'etc'):
            counterpart = extracted / rel
        else:
            continue
        assert counterpart.is_file(), f'Package lacks source-matching file: {rel}'
        assert file.read_bytes() == counterpart.read_bytes(), f'Package content differs from source: {rel}'
        checked += 1
    assert checked > 8, f'Too few source/package matches: {checked}'
print(f'PASS: tested v0.5.0 .deb checksum, control metadata, and {checked} exact source payload files')
