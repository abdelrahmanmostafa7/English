#!/usr/bin/env python3
"""Build American English Mastery Reference (A1–C2) print-ready HTML."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "index.html"

PART_TITLES = [
    (1, "How American English Works"),
    (2, "American English Sound System"),
    (3, "Consonants"),
    (4, "Important American Sounds"),
    (5, "American Vowels"),
    (6, "Schwa & Vowel Reduction"),
    (7, "Word Stress"),
    (8, "Sentence Stress"),
    (9, "American Rhythm"),
    (10, "Intonation"),
    (11, "Connected Speech"),
    (12, "Common American Reductions"),
    (13, "Final -S Rules"),
    (14, "Final -ED Rules"),
    (15, "Spelling → Pronunciation"),
    (16, "Pronunciation Difficulties"),
    (17, "3000 Core American Vocabulary"),
    (18, "Word Families"),
    (19, "Collocations"),
    (20, "High-Value Verbs"),
    (21, "Phrasal Verbs"),
    (22, "Confusing Words"),
    (23, "Daily Expressions"),
    (24, "Natural Conversational Patterns"),
    (25, "Conversation Management"),
    (26, "Workplace English"),
    (27, "Software Engineering English"),
    (28, "Interview English"),
    (29, "American vs Textbook English"),
    (30, "Listening Reference"),
    (31, "Shadowing Reference"),
    (32, "Speaking Reference"),
    (33, "Register"),
    (34, "CEFR Progression"),
    (35, "Quick Reference Tables"),
    (36, "Alphabetical Vocabulary Index"),
    (37, "Alphabetical Expression Index"),
    (38, "Master Reference Checklists"),
]


def toc_html():
    items = [
        f'<li><a href="#part-{n:02d}"><span class="toc-num">{n:02d}</span> <span>{t}</span></a></li>'
        for n, t in PART_TITLES
    ]
    return f'<ol>\n{"".join(items)}\n</ol>'


def sidebar_html():
    items = [
        f'<li><a href="#part-{n:02d}" data-nav="part-{n:02d}">{n}. {t}</a></li>'
        for n, t in PART_TITLES
    ]
    return f'<ol>\n{"".join(items)}\n</ol>'


def build():
    from content import all_parts

    parts_html = all_parts()
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="American English Mastery Reference: General American pronunciation, core vocabulary, expressions, connected speech, and professional communication (A1–C2).">
  <title>American English Mastery Reference</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header reading-progress" aria-label="Reading progress">
    <div class="progress-bar-row">
      <button type="button" class="toc-toggle" id="tocToggle" aria-controls="sidebar" aria-expanded="true" aria-label="Hide contents"></button>
      <div class="progress-meta">
        <span class="progress-part" id="progressPart">Cover</span>
        <span class="progress-title" id="progressTitle">American English Mastery Reference</span>
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
          <p class="eyebrow">General American · A1 → C2 · Reference Edition</p>
          <h1>American English Mastery Reference</h1>
          <div class="cover-summary">
            <p><strong>What it is.</strong> General American pronunciation, 3000 core vocabulary items, daily expressions, and connected-speech patterns for natural listening and speaking.</p>
            <p><strong>How to use it.</strong> Follow the path Sounds → Words → Stress → Expressions → Connected Speech → Conversation, then use the tables and indexes whenever you need a quick check.</p>
            <p><strong>Why we made it.</strong> So you can sound clearer, understand real American English faster, and communicate with confidence at work and in daily life.</p>
          </div>
        </header>
        {parts_html}
        <footer class="site-footer">
          <p>American English Mastery Reference · General American · A1–C2</p>
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
