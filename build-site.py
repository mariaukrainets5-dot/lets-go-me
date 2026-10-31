#!/usr/bin/env python3
"""Wraps index.html (Artifact format, no document tags) into docs/index.html for GitHub Pages."""
from pathlib import Path
import shutil

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Беги по морю в летающих ботинках, уворачивайся от акул и крокодилов, решай задачи и спаси кита от китобоев.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Let's Go Me">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#072b3f">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<style>
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); box-sizing: border-box; }
body { margin: 0; font: 14px system-ui, sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
"""
SW = """<script>if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js');</script>
"""
root = Path(__file__).parent
page = (root / "index.html").read_text(encoding="utf-8")
head, body = page.split('<div id="game">', 1)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(
    HEAD + head + '</head>\n<body>\n<div id="game">' + body + SW + "</body>\n</html>\n", encoding="utf-8"
)

# I Will Catch You lives next to the main game at /catch/.
game = (root / "catch" / "index.html").read_text(encoding="utf-8")
head, body = game.split('<canvas id="c"', 1)
(root / "docs" / "catch").mkdir(exist_ok=True)
(root / "docs" / "catch" / "index.html").write_text(
    '<!doctype html>\n<html lang="ru">\n<head>\n' + head + '</head>\n<body>\n<canvas id="c"' + body + "</body>\n</html>\n",
    encoding="utf-8",
)
shutil.copytree(root / "catch" / "art", root / "docs" / "catch" / "art", dirs_exist_ok=True)
