# English Grammar Reference A1–C2

A complete, print-ready English grammar reference book covering CEFR levels **A1 through C2**.

## Open the book

Open `index.html` in any modern browser.

## Save as PDF

1. Open `index.html`
2. Use **File → Print** (or the **Print / Save PDF** button)
3. Set paper size to **A4**
4. Enable backgrounds if you want callout colours
5. Choose **Save as PDF**

## Project structure

```
grammar-reference/
├── index.html          # Full book (generated)
├── css/
│   ├── styles.css      # Screen layout & typography
│   └── print.css       # A4 print / PDF rules
├── js/
│   └── nav.js          # TOC toggle + active section
├── assets/             # Reserved for future media
├── content/            # Source content modules (Python)
├── helpers.py
├── build.py            # Rebuilds index.html
└── README.md
```

## Rebuild from source

If you edit the Python content modules:

```bash
cd grammar-reference
python3 build.py
```

## Design notes

- Semantic HTML with internal navigation and indexes
- Professional reference typography (Source Serif 4 + IBM Plex Sans)
- Rule blocks: definition → form → use → examples → mistakes → compare
- Print CSS: A4 page size, page breaks between parts, avoid breaking tables/callouts awkwardly
