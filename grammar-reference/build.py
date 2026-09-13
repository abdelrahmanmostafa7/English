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
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header reading-progress" aria-label="Reading progress">
    <div class="progress-bar-row">
      <a class="home-link" href="../index.html" aria-label="Home" title="Home"></a>
      <button type="button" class="toc-toggle" id="tocToggle" aria-controls="sidebar" aria-expanded="true" aria-label="Hide contents"></button>
      <div class="progress-meta">
        <span class="progress-part" id="progressPart">Cover</span>
        <span class="progress-title" id="progressTitle">English Grammar Reference</span>
        <span class="progress-pct" id="progressPct" aria-hidden="true">0%</span>
      </div>
    </div>
    <div class="progress-track" aria-hidden="true">
      <div class="progress-fill" id="progressFill"></div>
    </div>
    <p class="visually-hidden" id="progressStatus" role="status" aria-live="polite"></p>
  </header>

  <div class="layout">
    <aside class="sidebar" id="sidebar" aria-label="Table of contents">
      <h2>Contents</h2>
      {sidebar_html()}
    </aside>

    <div class="main-wrap">
      <main id="main">
        <header class="cover" id="cover">
          <p class="eyebrow">CEFR A1 → C2 · Reference Edition</p>
          <h1>English Grammar Reference</h1>
          <div class="cover-summary">
            <p><strong>What it is.</strong> A complete grammar reference from A1 foundations to C2 academic and professional English — rules, forms, examples, and common mistakes in one place.</p>
            <p><strong>How to use it.</strong> Start with Part 1, study each topic with its examples, then return anytime through Contents and the indexes for fast lookup.</p>
            <p><strong>Why we made it.</strong> So you have a durable long-term study companion — not a short course you finish and forget.</p>
          </div>
        </header>

        {parts_html}

        <footer class="site-footer">
          <p>English Grammar Reference A1–C2 · Reference edition · For personal study</p>
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
