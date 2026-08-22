#!/usr/bin/env python3
"""Copy a legacy static site beneath Astro public/legacy and rewrite root-relative links."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil

SKIP = {".git"}
ATTR = re.compile(r"(?P<name>\b(?:href|src|poster|srcset|action))=(?P<quote>['\"])/(?P<path>(?!/|legacy/)[^'\"]*)", re.I)
CSS = re.compile(r"url\((?P<quote>['\"]?)/(?P<path>(?!/|legacy/)[^)'\"]*)(?P=quote)\)", re.I)


def rewrite_root_links(text: str) -> str:
    text = ATTR.sub(lambda match: f"{match.group('name')}={match.group('quote')}/legacy/{match.group('path')}", text)
    return CSS.sub(lambda match: f"url({match.group('quote')}/legacy/{match.group('path')}{match.group('quote')})", text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Existing generated Hexo site directory")
    parser.add_argument("destination", type=Path, help="Astro public/legacy destination directory")
    args = parser.parse_args()
    source = args.source.resolve()
    destination = args.destination.resolve()
    if not (source / "index.html").is_file():
        raise SystemExit(f"Expected legacy index.html under {source}")
    shutil.rmtree(destination, ignore_errors=True)
    destination.mkdir(parents=True)
    copied = 0
    rewritten = 0
    for path in source.rglob("*"):
        rel = path.relative_to(source)
        if any(part in SKIP for part in rel.parts) or not path.is_file():
            continue
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix.lower() in {".html", ".css"}:
            target.write_text(rewrite_root_links(path.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
            rewritten += 1
        else:
            shutil.copy2(path, target)
        copied += 1
    print(f"Copied {copied} files; rewrote {rewritten} HTML/CSS files into {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
