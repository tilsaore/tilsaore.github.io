"""Build the Spanish (/es/) and Portuguese (/pt/) homepages from index.html.

index.html (English) is the source of truth. Each translation module in
tools/i18n/ lists (english, translated) string pairs. Every English string
must still appear in index.html, so the build fails loudly when the English
page changes and a translation needs updating.

Usage:
    python3 tools/build_i18n.py
"""
from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://tilsaore.com"
LANGS = {
    # code: (output dir, og:locale, label in the switcher summary)
    "es": ("es", "es_LA", "Idioma: Español"),
    "pt": ("pt", "pt_BR", "Idioma: Português"),
}
# Titles kept in English on translated pages; tagged lang="en" for screen readers.
ENGLISH_TITLES = [
    "Critical Minerals in Latin America",
    "Competitive Retail Electricity Markets and Consumer Switching in Texas",
    "Mining, Governance, and Communities",
    "Building Barriers, Blocking Progress: Critical Minerals and Trade",
    "Political Risk and Resource Nationalism in Latin American Mining and Minerals",
    "Paving the Road for Competitive Green Hydrogen Hubs: Does Chile Have a Chance?",
    "Rice energy research explores practical solutions to global supply-chain challenges",
    "Rice experts available to discuss UAE exit from OPEC, global energy implications",
    "What Do Trade Tensions Mean for Critical Minerals? (PDF)",
    "Governance and climate finance in the developing world (PDF)",
]


def replace_once_or_more(html: str, old: str, new: str, lang: str) -> str:
    if old not in html:
        sys.exit(f"[{lang}] English string not found in index.html; update tools/i18n/{lang}.py:\n  {old[:100]}")
    return html.replace(old, new)


def build(lang: str, source: str) -> str:
    out_dir, locale, summary_label = LANGS[lang]
    pairs = importlib.import_module(f"i18n.{lang}").PAIRS
    html = source

    # 1. Mark English-language titles before translating surrounding text.
    for title in ENGLISH_TITLES:
        html = replace_once_or_more(html, f'">{title}</a>', f'" lang="en">{title}</a>', lang)

    # 2. Translate text, longest strings first so sentences win over fragments.
    for old, new in sorted(pairs, key=lambda p: -len(p[0])):
        html = replace_once_or_more(html, old, new, lang)

    # 3. Page-level metadata and paths (pages live one directory down).
    html = html.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    html = html.replace(f'<link rel="canonical" href="{SITE}/">', f'<link rel="canonical" href="{SITE}/{out_dir}/">', 1)
    html = html.replace(f'<meta property="og:url" content="{SITE}/">', f'<meta property="og:url" content="{SITE}/{out_dir}/">', 1)
    html = html.replace('<meta property="og:locale" content="en_US">', f'<meta property="og:locale" content="{locale}">', 1)
    html = html.replace(f'<meta property="og:locale:alternate" content="{locale}">', '<meta property="og:locale:alternate" content="en_US">', 1)
    html = re.sub(r'(href|src)="(images|files)/', r'\1="../\2/', html)

    # 4. Language switcher: label and current-page marker.
    html = html.replace('aria-label="Language: English" title="Language"', f'aria-label="{summary_label}" title="Idioma"', 1)
    html = html.replace('<ul class="lang-menu" aria-label="Language">', '<ul class="lang-menu" aria-label="Idioma">', 1)
    html = html.replace(' aria-current="page">English</a>', '>English</a>', 1)
    html = html.replace(f'hreflang="{lang}">', f'hreflang="{lang}" aria-current="page">', 1)
    return html


def main() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    source = (ROOT / "index.html").read_text(encoding="utf-8")
    for lang, (out_dir, _, _) in LANGS.items():
        target = ROOT / out_dir / "index.html"
        target.parent.mkdir(exist_ok=True)
        target.write_text(build(lang, source), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
