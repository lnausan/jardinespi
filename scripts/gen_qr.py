#!/usr/bin/env python3
"""Genera media/qr.png con el enlace actual del sitio (GitHub Pages).

Solo usa la biblioteca estándar. Requiere conexión a internet una vez:

    python3 scripts/gen_qr.py
"""
from __future__ import annotations

import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "qr.png"
SITE_URL = "https://lnausan.github.io/jardinespi/"


def main() -> None:
    qs = urllib.parse.quote(SITE_URL, safe="")
    api = f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={qs}"
    urllib.request.urlretrieve(api, OUT)
    print(f"Guardado: {OUT} ({OUT.stat().st_size} bytes)\n  → {SITE_URL}")


if __name__ == "__main__":
    main()
