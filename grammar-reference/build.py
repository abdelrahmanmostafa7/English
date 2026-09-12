#!/usr/bin/env python3
"""Build English Grammar Reference A1–C2 as a single print-ready HTML book."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "index.html"

PART_TITLES = [
    (1, "Grammar Foundations"),
    (2, "Nouns"),
    (3, "Pronouns"),
    (4, "Determiners"),
    (5, "Articles"),
    (6, "Adjectives"),
    (7, "Adverbs"),
    (8, "Prepositions"),
    (9, "Verbs"),
    (10, "Complete Tense System"),
    (11, "Modal Verbs"),
    (12, "Gerunds & Infinitives"),
    (13, "Conditionals"),
    (14, "Passive Voice"),
    (15, "Reported Speech"),
    (16, "Questions"),
    (17, "Negation"),
    (18, "Clauses"),
    (19, "Comparison"),
    (20, "Participles & Participial Clauses"),
    (21, "Causative Structures"),
    (22, "Phrasal & Multi-Word Verbs"),
    (23, "Word Order"),
    (24, "Emphasis & Advanced Structures"),
    (25, "Discourse & Cohesion"),
    (26, "Punctuation & Written Grammar"),
    (27, "Formal vs Informal English"),
    (28, "Common English Mistakes"),
    (29, "Confusing Structures"),
    (30, "Natural English Grammar"),
    (31, "CEFR Reference"),
    (32, "Master Quick Reference"),
    (33, "Common Error Index"),
    (34, "Grammar Index"),
]


def toc_html():
    items = []
    for n, t in PART_TITLES:
        items.append(
            f'<li><a href="#part-{n:02d}"><span class="toc-num">{n:02d}</span> <span>{t}</span></a></li>'
        )
    return f'<ol>\n{"".join(items)}\n</ol>'


def sidebar_html():
    items = []
    for n, t in PART_TITLES:
        items.append(f'<li><a href="#part-{n:02d}" data-nav="part-{n:02d}">{n}. {t}</a></li>')
    return f'<ol>\n{"".join(items)}\n</ol>'


def build():
    from content import all_parts

    parts_html = all_parts()
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A complete English grammar reference book covering CEFR levels A1 through C2. Print-ready A4 HTML.">
  <title>English Grammar Reference A1–C2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  <link rel="stylesheet" href="css/print.css" media="print">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header no-print">
    <a class="brand" href="#cover">English Grammar Reference A1–C2</a>
    <div class="header-actions">
      <button type="button" class="toc-toggle" id="tocToggle" aria-expanded="false">Contents</button>
      <button type="button" id="printBtn">Print / Save PDF</button>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar no-print" id="sidebar" aria-label="Table of contents">
      <h2>Contents</h2>
      {sidebar_html()}
    </aside>

    <div class="main-wrap">
      <main id="main">
        <header class="cover" id="cover">
          <p class="eyebrow">CEFR A1 → C2 · Reference Edition</p>
          <h1>English Grammar Reference</h1>
          <p class="subtitle">A complete, print-ready grammar book for long-term study and lookup — from foundations through advanced academic and professional English.</p>
        </header>

        {parts_html}

        <footer class="site-footer">
          <p>English Grammar Reference A1–C2 · Reference edition · For personal study · Print on A4</p>
        </footer>
      </main>
    </div>
  </div>

  <script src="js/nav.js"></script>
</body>
</html>
'''
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
