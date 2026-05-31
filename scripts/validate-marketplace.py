#!/usr/bin/env python3
"""Validate the yikusiel-codex-marketplace manifest.

Checks .agents/plugins/marketplace.json for:
  * valid JSON
  * correct marketplace name (must stay "yikusiel-codex-marketplace")
  * no duplicate plugin names
  * every plugin has a name + source
  * plugin counts by category and by source type
  * lists all external (git-subdir / url) sources
  * (optional) with --online, verifies each external manifest is reachable

Usage:
  python scripts/validate-marketplace.py
  python scripts/validate-marketplace.py --online

Exit code: 0 = all checks passed, 1 = at least one check failed.
"""
import collections
import json
import sys
from pathlib import Path

EXPECTED_NAME = "yikusiel-codex-marketplace"
MANIFEST = Path(__file__).resolve().parents[1] / ".agents" / "plugins" / "marketplace.json"


def manifest_url(source):
    """Build the raw GitHub URL for an external plugin's .codex-plugin/plugin.json."""
    url = source.get("url")
    ref = source.get("ref", "main")
    path = source.get("path")
    sub = f"{path.rstrip('/')}/.codex-plugin/plugin.json" if path else ".codex-plugin/plugin.json"
    return f"https://raw.githubusercontent.com/{url}/{ref}/{sub}"


def main():
    online = "--online" in sys.argv[1:]
    errors = []

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: cannot read/parse {MANIFEST}: {e}")
        return 1
    print(f"OK   valid JSON: {MANIFEST}")

    name = data.get("name")
    if name != EXPECTED_NAME:
        errors.append(f"marketplace name is {name!r}, expected {EXPECTED_NAME!r}")
    print(f"     name: {name}")
    print(f"     interface.displayName: {data.get('interface', {}).get('displayName')}")

    plugins = data.get("plugins", [])
    print(f"     plugin_count: {len(plugins)}")

    names = [p.get("name") for p in plugins]
    dupes = [n for n, c in collections.Counter(names).items() if c > 1]
    if dupes:
        errors.append(f"duplicate plugin names: {dupes}")
    print(f"     duplicates: {dupes or 'none'}")

    for p in plugins:
        if not p.get("name"):
            errors.append(f"entry missing 'name': {p}")
        elif not p.get("source"):
            errors.append(f"{p.get('name')}: missing 'source'")

    cats = collections.Counter((p.get("category") or "(none)") for p in plugins)
    print("\ncategories:")
    for cat, n in sorted(cats.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {n:>4}  {cat}")

    def stype(p):
        s = p.get("source")
        return s.get("source") if isinstance(s, dict) else "string"

    print("\nsource_types:", dict(collections.Counter(stype(p) for p in plugins)))

    ext = [p for p in plugins if isinstance(p.get("source"), dict) and p["source"].get("source") in ("git-subdir", "url")]
    print(f"\nexternal sources ({len(ext)}):")
    for p in sorted(ext, key=lambda p: p["name"]):
        s = p["source"]
        print(f"  {p['name']:<26} {s.get('source'):<10} {str(s.get('url')):<42} {s.get('path', '(root)')} @ {s.get('ref', '?')}")

    if online:
        import urllib.request
        print("\n[--online] verifying external manifests are reachable...")
        for p in sorted(ext, key=lambda p: p["name"]):
            raw_url = manifest_url(p["source"])
            try:
                with urllib.request.urlopen(raw_url, timeout=20) as r:
                    ok = r.status == 200
            except Exception:
                ok = False
            print(f"  {'OK  ' if ok else 'FAIL'} {p['name']:<26} {raw_url}")
            if not ok:
                errors.append(f"{p['name']}: manifest not reachable ({raw_url})")

    print()
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
