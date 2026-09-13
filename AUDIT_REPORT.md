# English Reference Books — Full Audit

**Audit mode:** read-only. No project files were modified except creation of this report.  
**Date:** 2026-09-13  
**Method:** Inspected live `index.html`, CSS, JS, Python sources, and `data/vocab.json` (not README claims alone).

---

## Executive Summary

Both projects are browser-based HTML reference books with a shared modern UI (sticky reading progress, collapsible sidebar, part panels). They are **structurally ambitious** and **complementary in intent**: grammar explains structure; American English Mastery targets pronunciation, lexicon, and spoken communication.

**Verdict in one line:**

- **`grammar-reference`** is a **serious, mostly real grammar book** with strong topic coverage and a particularly solid tense system — but uneven entry depth, thin C2 treatment, and **no print CSS**.
- **`american-english-mastery`** has a **credible pronunciation spine and useful expression/SE phrase banks**, but its advertised “3000 core vocabulary” is largely **template filler**, so the project is **not yet a trustworthy vocabulary reference**.

| Project | Overall score (/100) | Ready for serious long-term use? |
|---|---|---|
| Grammar Reference | **74** | **Mostly yes** for grammar study/lookup, with caveats |
| American English Mastery | **49** | **Partially** — pronunciation/phrases yes; vocabulary **no** until rewritten |

---

## Project Inventory

### Shared characteristics

| Feature | Grammar Reference | American English Mastery |
|---|---|---|
| Main deliverable | Single `index.html` | Single `index.html` |
| CSS | `css/styles.css` only | `css/styles.css` only |
| JS | `js/nav.js` | `js/nav.js` |
| Print CSS | **Absent** (`print.css` removed; README still claims it) | **Absent** |
| Search | None | None |
| Progress tracking | Per-part scroll progress bar + % | Same |
| Sidebar | Collapsible (desktop + mobile), localStorage | Same |
| Interactive | TOC toggle, backdrop (mobile), active nav highlight | Same |
| Audio/media assets | None | None |

### `grammar-reference`

| Item | Finding |
|---|---|
| Total tracked source files (excl. `__pycache__`) | **12** meaningful sources (+ compiled `.pyc`) |
| HTML | 1 (`index.html`) |
| CSS | 1 (`styles.css`) |
| JS | 1 (`nav.js`) |
| Content sources | `content/parts_01_08.py` … `parts_27_34.py`, `extra_depth.py`, `helpers.py`, `build.py` |
| Assets | None present |
| Major parts | **34** |
| H3 topics | **121** |
| Rule blocks | **173** |
| Tables | **74** |
| Indexes | Common Error Index (Part 33), Grammar Index (Part 34), Master Quick Reference (Part 32), CEFR map (Part 31) |
| Vocabulary/expressions | N/A (grammar book) |
| Example boxes | 182 |
| Mistake boxes | 58 |
| Compare boxes | 15 |
| CEFR badge hits | A1:20 · A2:64 · B1:97 · B2:79 · C1:43 · C2:10 |

### `american-english-mastery`

| Item | Finding |
|---|---|
| Total tracked source files (excl. `__pycache__`) | **13** meaningful sources |
| HTML | 1 (`index.html`, very large due to vocab dump) |
| CSS | 1 (`styles.css`) |
| JS | 1 (`nav.js`) |
| Data | `data/vocab.json` (**3050** entries) |
| Content sources | `content/parts_01_08.py` … `parts_31_38.py`, `helpers.py`, `build.py` |
| Assets | None |
| Major parts | **38** |
| Vocabulary cards in HTML | **3050** unique IDs |
| Expression cards | **44** |
| Tables | **28** |
| Indexes | Alphabetical Vocabulary Index (Part 36), Expression Index (Part 37), Checklists (Part 38) |
| Vocab by CEFR (actual) | A1:261 · A2:421 · B1:527 · B2:1118 · C1:723 · **C2:0** |

---

## Grammar Reference

### Coverage

**Overall:** Broad and largely real. The 34-part map matches a serious A1–C2 reference outline.

#### Foundations (Part 1) — **Good / Excellent**
Present: sentence needs, subject, finite/non-finite verb, predicate, direct/indirect object, subject/object complements, phrases vs clauses, sentence patterns.  
Modern SE-flavored examples are a strength.

#### Nouns (Part 2) — **Good**
Common/proper, concrete/abstract, countable/uncountable, plurals, possessives, collective, noun phrases, nominalization appear.  
Compound nouns appear in classification tables more than as a deep dedicated treatment.

#### Pronouns (Part 3) — **Good**
Personal/object/possessive/reflexive/reciprocal/demonstrative/indefinite/interrogative/relative, dummy *it*, existential *there*, *one/ones*, reference/agreement are present.

#### Determiners (Part 4) — **Good**
Articles (preview), demonstratives, possessives, quantifiers, numbers, distributives, interrogatives, pre-/postdeterminers, order covered at reference depth.

#### Articles (Part 5) — **Good, with gaps**
Strong on *a/an*, *the*, zero article, generics, institutions, transport, meals, sports, languages, geography.  
**Thin/missing:** diseases, media systems as dedicated difficult cases.

#### Adjectives (Part 6) — **Good**
Attributive/predicative, order, gradable/non-gradable, comparison links, participial adjectives, adj+prep present.

#### Adverbs (Part 7) — **Good**
Manner/place/time/frequency/degree/viewpoint/focusing/linking/stance, position, adjective vs adverb, *hard/hardly*-type contrasts present.

#### Prepositions (Part 8) — **Good**
Time/place/movement and dependent prepositions (V/Adj/N + prep), phrasal-prepositional notes present.

#### Verbs (Part 9) — **Excellent on statives**
Auxiliaries, linking, transitive/intransitive, regular/irregular, multi-word preview.  
**Stative verbs are clearly explained**, including:
- *I agree* vs *I am agree*
- *I know* vs *I am knowing*
- dynamic reinterpretations (*I'm seeing the client*)  
Also reinforced in Present Simple mistakes and the Common Error Index.

#### Tenses (Part 10) — **Excellent structure**
All major present/past/future forms listed below are present as dedicated sections, plus future-in-the-past, time clauses, sequence-of-tenses overview, and comparison workshops.

#### Modals / Gerunds / Conditionals / Passive / Reported / Questions / Negation / Clauses — **Good overall**
Meaning-changing pairs (*stop/remember/forget/try/regret/mean*) are present.  
Zero–third + mixed, unless/provided/as long as/in case/even if/only if, wish/if only, inverted conditionals present.  
Get-passive, impersonal passive, causatives present; “reporting passive” as a named deep section is weaker.  
Question tags, embedded questions present; “indirect questions” terminology less consistently labeled.

#### Advanced (Parts 19–30) — **Good / Partial**
Participles, causatives, phrasals, word order, clefts/fronting/inversion/emphasis/ellipsis, discourse, punctuation, formal vs informal, mistake banks, confusing structures, natural grammar — present, but several later parts are shorter than early core parts.

### Missing Topics

| Topic | Status |
|---|---|
| Diseases (article patterns) | Missing / not meaningfully covered |
| Media article patterns (the news / radio / TV systems) | Thin/missing as dedicated case set |
| Compound nouns (deep morphology/stress patterns) | Partial (classification, not deep) |
| Reporting passive (named, systematic) | Partial |
| Indirect questions (as consistently labeled system) | Partial (embedded questions exist) |
| Arabic learner notes | Absent entirely |
| Audio examples | Absent |
| Full spoken grammar corpus depth at C2 | Thin |
| Print/PDF stylesheet | **Missing** |

### CEFR Assessment

Do **not** equate badge presence with progression quality. Badges are applied, but density and depth are uneven.

| Level | Rating | Why |
|---|---|---|
| **A1** | **Good** | Foundations, basic articles, Present Simple/Continuous, core patterns present with appropriate simplicity. |
| **A2** | **Good** | Countability, statives, Past Simple/Continuous, going to, comparatives, core mistakes bank support A2 well. |
| **B1** | **Excellent / Good** | Present Perfect, conditionals intro depth, reported speech basics, questions/negation, dependent prepositions — strong. |
| **B2** | **Good** | Perfect continuous, mixed conditionals, passives, clefts beginning, discourse — present and mostly appropriately harder. |
| **C1** | **Partial** | Advanced structures exist, but fewer dedicated deep C1 explorations than a full academic reference; some advanced notes are short. |
| **C2** | **Weak** | Only ~10 C2 badge hits; nuance/register/spoken grammar at true C2 mastery level is underdeveloped. |

**Misclassification risk:** Some B2/C1 topics appear early with multi-level badges (acceptable for reference books), but learners can overestimate readiness because badges often stack A2–B2 on one entry without staged explanations.

### Entry Quality

Sampled across foundations, articles, tenses, statives, conditionals, passives, and advanced emphasis.

| Expected element | Consistency |
|---|---|
| Rule / definition | Usually present |
| Form | Strong in tense system; **weak overall** (~13/158 parsed rule-blocks have explicit `form-pattern`) |
| When to use | Inconsistent (common in strong entries; missing in many) |
| Examples | Generally good; modern/natural; SE-flavored |
| Common mistakes | Present in best entries; **only ~58 mistake boxes** book-wide |
| Comparison | Present for key tense contrasts; sparse elsewhere (~15 compare boxes) |
| Advanced note | Occasional (`box-advanced` = 7) |

**Best-in-book pattern:** Present Perfect entry includes Structure, +/-/?, uses, time expressions, examples, mistakes, AmE/BrE compare — this is the quality target.

**Weak pattern:** Many later/smaller parts are explanatory prose + examples without the full template.

**Arabic:** none.  
**Technical correctness (sampled):** generally sound; stative and Present Perfect guidance are accurate.  
**Duplicates:** intentional reinforcement of *I am agree* across Parts 9, 10, 28, 33 — useful repetition, not harmful.

### Accuracy Issues

No catastrophic systemic grammar falsehoods found in sampled core topics.

Noted issues / risks:

1. **README/docs drift:** README still describes `print.css` and a Print button that no longer exist.
2. **AmE/BrE notes** appear in a British-leaning grammar book with American workplace examples — useful, but branding/positioning is mixed.
3. Some advanced topics are **present by title** but **shallow** (risk of false confidence).
4. C2 labeling is sparse relative to the “A1–C2 complete” claim.

### Redundancy

| Kind | Assessment |
|---|---|
| Stative / *I am agree* repeated | **Useful repetition** |
| Tense comparisons + workshops overlapping | Useful |
| Mistake bank vs inline mistakes | Useful dual access |
| Formal vs informal vs Natural English | Some overlap; mostly complementary |
| True conflicting definitions | Not found in sampling |

### UI/UX

**Strengths**
- Sticky reading progress with part title + %
- Collapsible sidebar (desktop/mobile), icon-only toggle
- Clear part cards, CEFR badges, callout system
- Internal anchors + indexes
- No duplicate IDs detected in `index.html`
- Readable typography (Source Serif 4 / IBM Plex)

**Weaknesses**
- No search (painful for a reference)
- No keyboard shortcut map beyond Esc-close on mobile
- Active-section highlighting relies on scroll math (no IntersectionObserver in current `nav.js`)
- Mobile sidebar works; dense tables still demanding
- Accessibility: icon button has aria-label; progress has live region — decent, not audited to WCAG completeness

### Print/PDF

**Score impact: severe.**

- `css/print.css` **does not exist**
- No `@media print` / `@page` rules in `styles.css`
- README incorrectly claims print-ready A4 CSS and Print button
- Browser print will include sticky header/sidebar chrome unless user manually adjusts
- No controlled page breaks, widow/orphan rules, or print color handling in current CSS

**Print readiness: not production-ready.**

### Score

| Dimension | Score (/10) |
|---|---|
| Coverage | 8.3 |
| Accuracy | 8.5 |
| CEFR progression | 7.2 |
| Explanation quality | 7.0 |
| Examples | 8.0 |
| Common mistakes | 6.8 |
| Advanced grammar | 7.6 |
| Navigation | 7.5 |
| UI | 7.8 |
| Print readiness | 2.5 |
| **Overall** | **74 / 100** |

---

## American English Mastery

### Coverage

The **part map is excellent** (38 parts): sounds → prosody → connected speech → vocab → expressions → workplace/SE/interview → practice references → indexes.

But **depth is highly uneven**:

- Pronunciation Parts 3–4 and difficulties guide: substantive
- Many prosody/connected-speech parts: short tables
- Part 17 vocabulary: enormous file weight, weak content quality
- Parts 26–28 (workplace/SE/interview): useful phrase banks, not deep communication training

### Pronunciation

| Area | Status |
|---|---|
| IPA usage | Present in places; not systematic across lexicon |
| Consonants | Strong (Part 3): voicing + mouth notes + minimal pairs |
| Vowels | Present (Part 5) |
| American R / TH / Flap T / T variants / clear vs dark L / NG | Present (Part 4) — good practical focus |
| Schwa / reduction | Present (Part 6) |
| Word/sentence stress, rhythm, intonation | Present but **thin** (often ~1–2KB sections) |
| Final -s / -ed | Present |
| Spelling→pronunciation | Present |
| Learner difficulties matrix | Good troubleshooting table |

### Connected Speech

Part 11 is a **compact overview table** (linking, weak forms, assimilation, elision, contractions, Flap T) plus a few casual examples and a professional warning.

Part 12 reductions table **does include** the requested set:
going to, want to, have to, got to, kind of, sort of, give me, let me, tell him, did you, what do you, could you, would you, should you (+ dunno/outta).

**Assessment:** checklist coverage is good; pedagogical depth (HOW to train listening/production step-by-step) is only **Partial**.

### Vocabulary

#### Actual counts
- JSON + HTML cards: **3050** unique headwords
- No duplicate IDs / no duplicate words detected
- CEFR: A1 261, A2 421, B1 527, B2 1118, C1 723, **C2 0**

#### Quality reality (critical)
From `data/vocab.json`:

| Field | Missing / empty |
|---|---|
| meaning | mostly present but **~2494/3050 are generic templates** (“High-value American English item…”) |
| example | **~3004/3050** are the same generic line (“Learn … not in isolation”) |
| arabic | **2986** empty (~64 filled) |
| ipa | **3004** empty (~46 filled) |
| stress | **3050** empty |
| collocations | **3004** empty (~46 filled) |
| patterns | **3043** empty |
| related | **3050** empty |
| mistake | **3050** empty |
| pos | **2494** are `—` |

**Conclusion:** The “3000 vocabulary” claim is true as a **word list size**, false as a **finished vocabulary reference**. Most entries are filler scaffolds.

Part 17 intro promises pronunciation, collocations, register, and Arabic “where useful.” Implementation does not match that promise.

#### Utility evaluation
- List likely contains many high-frequency lemmas (good seed list)
- Also includes many low-teaching-value isolated function words as full “cards” with no pedagogy (`a`, `am`, `and`, etc.)
- Workplace/SE usefulness is not proven by entry content (register=professional on only ~183 items; meanings still mostly templates)
- Obvious filler: template meanings/examples at scale

### Expressions

Part 23 Daily Expressions: **44** cards, grouped by situation (greetings, small talk, clarification, agreeing/disagreeing, requests, refusals, suggestions, buying time, interrupting, topic change, etc.).

**Quality:** generally natural, American, useful, contextualized.  
**Gap:** small inventory for a “mastery” book; register labeling lighter than ideal; not enough workplace-specific expression depth beyond later phrase tables.

Parts 24–25 (conversational patterns / management) exist but are short.

### Workplace English

Part 26 is a **single situation→phrases table** (status, priorities, deadlines, blockers, feedback, meetings, negotiation, etc.).

**Useful as a cheat sheet. Not a full workplace communication curriculum.**

### Software Engineering English

Part 27 covers standups, code review, bugs/incidents, requirements, architecture, collaboration as **bullet phrase lists**.

**Strengths:** authentic phrases (LGTM, WIP PR, Sev-2, trade-off, acceptance criteria).  
**Weaknesses:** no dialogues, no turn-taking models, no “explain a decision” worked examples, little Git/PR process language beyond fragments, no deployment/testing deep patterns.  
**Assessment:** genuine communication **snippets**, not full communication training.

Interview Part 28 similarly: compact STAR/clarify/trade-off phrase table — useful, shallow.

### Entry Quality

| Content type | Quality |
|---|---|
| Consonant/important-sound entries | Good (WHAT/ partial WHY/HOW via voicing+mouth) |
| Connected speech / reductions | Adequate reference tables |
| Expression cards | Good naturalness; limited count |
| Vocabulary cards | **Poor** at scale (template) |
| High-value verbs / collocations / phrasals parts | Mixed; better than Part 17 templates but not encyclopedia-deep |
| Word families | Short |

Pronunciation WHAT/WHY/HOW:
- **WHAT:** usually clear
- **WHY:** sometimes (American features, listening difficulty)
- **HOW:** present for many consonants (mouth/voicing); weaker for rhythm/intonation/connected speech production drills

### Redundancy

| Item | Assessment |
|---|---|
| Reductions listed in Part 12 and mentioned in Part 11 | Useful |
| Checklists repeating phrase themes | Useful |
| 3050 near-identical vocab card templates | **Unnecessary duplication of emptiness** |
| README claiming print.css / print button | Doc redundancy/conflict with reality |

### UI/UX

Same shell strengths as grammar book.

**Extra issues**
- Part 17 massively inflates DOM size (~1.5M+ characters in that section alone) — performance/scroll cost on weaker devices
- No search over 3050 cards makes vocabulary section nearly unusable as a reference
- Alphabetical index exists (Part 36), which partially mitigates no-search, but still heavy

### Print/PDF

Same failure mode as grammar book:
- no `print.css`
- no `@page` / `@media print` in `styles.css`
- README outdated
- Printing 3050 template vocab cards would be an unusable PDF

**Print readiness: not production-ready.**

### Score

| Dimension | Score (/10) |
|---|---|
| Pronunciation coverage | 7.0 |
| American English accuracy | 7.2 |
| Connected speech | 5.5 |
| Vocabulary quality | 2.2 |
| Vocabulary coverage (meaningful) | 4.0 |
| Expressions | 6.5 |
| Natural communication | 5.8 |
| Workplace English | 5.0 |
| Software Engineering English | 4.8 |
| Navigation | 7.5 |
| UI | 7.6 |
| Print readiness | 2.0 |
| **Overall** | **49 / 100** |

---

## Cross-Book Analysis

### Complementarity — **Yes, by design**

| Grammar Reference | American English Mastery |
|---|---|
| Explains *used to* / tense / articles / statives | Should teach how Americans pronounce & deploy them in speech |
| Structural correctness | Intelligibility + naturalness |
| Written and general grammar | Spoken GA + workplace talk |

They should remain **separate**.

### Useful crossover already present
- Grammar examples often use SE/workplace contexts
- AEM interview/SE phrases assume grammar competence
- Both share CEFR framing and UI conventions

### Unnecessary duplication
- Low: some workplace vocabulary ideas appear in both, but roles differ
- High risk if vocab templates are later “expanded” into grammar lessons inside AEM

### Missing connections (not merge — cross-links)
- No cross-references from AEM reductions to grammar future forms (*going to*)
- No link from grammar Present Perfect AmE note to AEM listening/reductions
- No shared terminology glossary
- Grammar has no pronunciation companions; AEM has almost no grammar pointers

---

## P0 — Critical Issues

1. **AEM vocabulary is mostly template filler** (~82% generic meanings; ~98% generic examples; almost no IPA/stress/collocations/mistakes). This falsifies the core “3000 core vocabulary reference” promise.
2. **Print/PDF pipeline missing in both projects** (`print.css` gone; no print CSS; README still markets print-ready A4).
3. **AEM claims A1–C2 vocabulary progression but has zero C2 lexical tier** and weak non-template pedagogy at every level.

## P1 — High Priority

1. Grammar entry template inconsistency (form / when-to-use / mistakes / compare not applied uniformly outside best sections).
2. Grammar C2 depth weak relative to “complete A1–C2” claim.
3. AEM connected speech / stress / rhythm / intonation sections too shallow for “mastery.”
4. AEM SE/workplace/interview sections are phrase lists, not communication pattern lessons.
5. No search in either book (especially fatal for AEM vocab + grammar indexes).
6. README/docs out of sync with UI (print button/CSS, feature claims).
7. Articles difficult cases incomplete (diseases/media etc.).
8. AEM POS tagging mostly missing (`—` on ~2494 entries).

## P2 — Medium Priority

1. Cross-book linking (grammar ↔ pronunciation/usage).
2. Expand expressions beyond 44 cards with register and response pairs.
3. Deeper reporting-passive / compound-noun / indirect-question labeling in grammar.
4. Performance strategy for huge AEM DOM (virtualize/split vocab).
5. More compare boxes for near-tense and near-structure contrasts.
6. Arabic support strategy: either commit (high quality) or stop promising it in AEM Part 17 intro.
7. Accessibility pass (focus states, skip targets, reduced-motion).

## P3 — Low Priority

1. Normalize terminology (indirect vs embedded questions).
2. Reduce repeated *I am agree* appearances if indexes already cover it (optional; currently useful).
3. Visual polish on very short AEM parts so they don’t feel like stubs.
4. Footer/README cleanup of “Print on A4” leftovers.
5. Add “last reviewed” metadata per part.

---

## Top 20 Recommended Improvements

1. Rebuild AEM vocabulary entries with real definitions, examples, IPA, stress, collocations (priority: top 1000 lemmas first).
2. Remove or quarantine template-only vocab cards from the learner-facing book until filled.
3. Restore a real print stylesheet (`@page` A4, hide chrome, page-break-before parts) for both books — or stop claiming print-ready.
4. Add search (at least sidebar filter + vocab/grammar index filter).
5. Bring grammar rule-block template to 80%+ consistency.
6. Expand grammar C1–C2 nuance chapters (spoken grammar, register, advanced cohesion).
7. Deepen AEM Parts 7–12 with drills: listen → notice → controlled produce.
8. Upgrade SE English from bullets to mini-dialogues + decision-explanation frames.
9. Expand Daily Expressions to 150–300 with reply pairs and register tags.
10. Complete article edge-case set (diseases, media, special institutional patterns).
11. Add cross-links between books for high-value structures (*going to*, reductions, Present Perfect AmE).
12. Fix README feature claims to match reality.
13. Add C2 vocabulary tier only with real entries (not empty badges).
14. Fill POS tags in AEM JSON.
15. Add mistake notes for top 200 learner-error lemmas in AEM.
16. Split AEM vocab into lazy-loaded chunks for performance.
17. Add compare modules for Future Continuous vs Perfect Continuous etc. where missing.
18. Strengthen reporting verbs / reporting passive as a coherent grammar package.
19. Add pronunciation audio later (not required for text reference, but high value).
20. Create an editorial QA checklist: no template strings allowed in shipped vocab.

---

## Final Verdict

### Grammar Reference — **74/100**
A **real reference book** with impressive breadth, a strong tense engine, and clear treatment of high-value learner errors (especially statives). It is already useful for serious study and lookup. It is **not** fully “complete C2,” **not** print-ready in the current codebase, and entry quality should be normalized.

### American English Mastery — **49/100**
A **promising shell** with a good pronunciation outline, a practical reductions table, and natural expression/SE phrase snippets. It is **not yet** a serious vocabulary mastery product because the 3050-card core is overwhelmingly empty template text. Until vocabulary is rewritten, long-term learners should treat Part 17 as a **word list stub**, not a reference.

### Ready for serious long-term use?
- **Grammar:** Yes, with known gaps (C2 depth, print, search, entry consistency).
- **AEM:** Only for pronunciation overview + phrases; **not** for vocabulary mastery as currently shipped.

### Issue tally (unique audit findings)

| Priority | Count |
|---|---|
| P0 | **3** |
| P1 | **8** |
| P2 | **7** |
| P3 | **5** |

---

*End of audit. Only this file (`AUDIT_REPORT.md`) was created.*
