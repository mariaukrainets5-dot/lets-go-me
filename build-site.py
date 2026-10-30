#!/usr/bin/env python3
"""Wraps index.html (Artifact format, no document tags) into docs/index.html for GitHub Pages."""
from pathlib import Path

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Беги по морю в летающих ботинках, уворачивайся от акул и крокодилов, решай задачи и спаси кита от китобоев.">
<style>
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); box-sizing: border-box; }
body { margin: 0; font: 14px system-ui, sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
"""
root = Path(__file__).parent
page = (root / "index.html").read_text(encoding="utf-8")
head, body = page.split('<div id="game">', 1)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(
    HEAD + head + '</head>\n<body>\n<div id="game">' + body + "</body>\n</html>\n", encoding="utf-8"
)
