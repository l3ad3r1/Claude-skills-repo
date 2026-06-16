#!/usr/bin/env python3
"""Parity check between Claude-skills-repo (canonical) and Hermes-skills (derived).

Claude-skills-repo is the canonical source of truth for skill content. The
Hermes-skills repo repackages the same skills into category folders with richer
frontmatter, so it must contain the *same set* of skills and the *same bundled
files* (scripts/examples/reference). Some SKILL.md bodies and frontmatter
descriptions intentionally differ between the two, so those are reported as
warnings rather than errors.

Run before cutting a release:

    python tools/check_parity.py                # assumes Hermes at ../_hermes
    python tools/check_parity.py ../path/to/Hermes-skills
    HERMES_DIR=/path/to/Hermes-skills python tools/check_parity.py

Exit code is non-zero if any ERROR-level drift is found.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Files that are never expected to match (build cruft / OS noise).
IGNORE_PARTS = {"__pycache__"}
IGNORE_SUFFIXES = {".pyc", ".pyo"}
IGNORE_NAMES = {".DS_Store", "Thumbs.db"}


def is_ignored(rel: Path) -> bool:
    if rel.name in IGNORE_NAMES:
        return True
    if rel.suffix in IGNORE_SUFFIXES:
        return True
    return any(part in IGNORE_PARTS for part in rel.parts)


def skill_files(skill_dir: Path) -> set[str]:
    out = set()
    for p in skill_dir.rglob("*"):
        if p.is_file():
            rel = p.relative_to(skill_dir)
            if not is_ignored(rel):
                out.add(rel.as_posix())
    return out


def skill_body(skill_md: Path) -> str:
    """Return the markdown body with the leading YAML frontmatter stripped."""
    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def main() -> int:
    canonical_root = Path(__file__).resolve().parent.parent

    hermes_arg = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("HERMES_DIR")
    hermes_root = Path(hermes_arg) if hermes_arg else canonical_root.parent / "_hermes"
    hermes_root = hermes_root.resolve()

    print(f"canonical (Claude-skills-repo): {canonical_root}")
    print(f"derived   (Hermes-skills):      {hermes_root}")
    print()

    if not (hermes_root / "skills").is_dir():
        print(f"ERROR: no skills/ directory under {hermes_root}")
        return 2

    # canonical: skills/<name>/
    canonical = {
        d.name: d for d in (canonical_root / "skills").iterdir() if d.is_dir()
    }
    # hermes: skills/<category>/<name>/
    hermes: dict[str, Path] = {}
    for cat in (hermes_root / "skills").iterdir():
        if not cat.is_dir():
            continue
        for d in cat.iterdir():
            if d.is_dir():
                hermes[d.name] = d

    errors: list[str] = []
    warnings: list[str] = []

    only_canonical = sorted(set(canonical) - set(hermes))
    only_hermes = sorted(set(hermes) - set(canonical))
    for name in only_canonical:
        errors.append(f"{name}: present in canonical but MISSING from Hermes")
    for name in only_hermes:
        errors.append(f"{name}: present in Hermes but MISSING from canonical")

    for name in sorted(set(canonical) & set(hermes)):
        cfiles = skill_files(canonical[name])
        hfiles = skill_files(hermes[name])
        for f in sorted(cfiles - hfiles):
            errors.append(f"{name}: file in canonical missing from Hermes -> {f}")
        for f in sorted(hfiles - cfiles):
            errors.append(f"{name}: file in Hermes missing from canonical -> {f}")

        cmd = canonical[name] / "SKILL.md"
        hmd = hermes[name] / "SKILL.md"
        if cmd.is_file() and hmd.is_file():
            if skill_body(cmd) != skill_body(hmd):
                warnings.append(f"{name}: SKILL.md body differs (may be intentional)")

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
        print()
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        print(f"\nFAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: {len(canonical)} skills in parity, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
