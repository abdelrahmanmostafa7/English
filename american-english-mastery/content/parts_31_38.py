"""Parts 31–38: Practice references, CEFR, tables, indexes, checklists."""
import json
from pathlib import Path
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, note, warning, table, badge
)

DATA = Path(__file__).resolve().parent.parent / "data" / "vocab.json"


def part_31():
    s = [part_header(31, "Shadowing Reference",
        "You already shadow. Use this as a checklist for quality — not as a replacement course.")]
    s.append(table(
        ["Mode", "Focus"],
        [
            ["With captions", "Map sound → spelling; notice reductions in text"],
            ["No captions", "Train ear for stress/rhythm/linking"],
            ["Slow repetition", "Accuracy of R, TH, vowels, endings"],
            ["Normal speed", "Rhythm and connected speech"],
            ["Record & compare", "Find mismatches in stress/intonation"],
            ["Stress imitation", "Copy content-word peaks only"],
            ["Rhythm imitation", "Compress unstressed syllables"],
            ["Intonation imitation", "Copy pitch shape on the final focus word"],
        ],
    ))
    s.append(note("<p>Shadow short clips (10–30 seconds). One feature at a time beats everything at once.</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_32():
    s = [part_header(32, "Speaking Reference",
        "Tools for real-time speaking: thinking time, repair, paraphrase, and keeping talk going.")]
    s.append(ul(
        "<em>Let me put it another way.</em>",
        "<em>What I'm trying to say is…</em>",
        "<em>I can't remember the exact word, but…</em>",
        "<em>Basically…</em> / <em>More specifically…</em>",
        "<em>Sorry, let me restart.</em>",
        "<em>In other words…</em>",
        "<em>The short version is…</em>",
        "<em>How do you say…?</em>",
        "<em>It's kind of like…</em>",
        "<em>Does that make sense so far?</em>",
    ))
    s.append(rule(
        "Fillers (use lightly)",
        "Natural fillers buy time: <em>um, uh, like, you know, I mean</em>. "
        "Overuse hurts clarity — especially in interviews. Prefer meaningful frames: <em>Let me think</em>.",
        levels=["B1", "B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_33():
    s = [part_header(33, "Register",
        "Choose language that fits audience and channel. The same idea can be grammatical in several registers.")]
    s.append(table(
        ["Register", "Where it fits", "Example"],
        [
            ["Slang", "Close friends; rarely at work", "That meeting was a dumpster fire."],
            ["Casual", "Teammates / informal chat", "I'll ping you when it's done."],
            ["Conversational / neutral", "Default spoken American English", "I'll let you know when it's done."],
            ["Professional", "Work meetings, Slack with stakeholders", "I'll follow up once the fix is deployed."],
            ["Formal", "Careful email, legal, academic tone", "Please be advised that the change has been implemented."],
            ["Academic", "Papers / formal analysis", "The results suggest a significant reduction in latency."],
        ],
    ))
    s.append(warning("<p>Do not teach or use slang as if it were standard professional English. Label it and keep it optional.</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_34():
    s = [part_header(34, "CEFR Progression",
        "Approximate A1→C2 map for this book's domains. CEFR is not defined by vocabulary count alone.")]
    s.append(table(
        ["Area", "A1–A2", "B1–B2", "C1–C2"],
        [
            ["Pronunciation", "Clear consonants/vowels; -s/-ed; basic stress", "Schwa, sentence stress, Flap T awareness, linking", "Flexible intonation, controlled reductions, high intelligibility at speed"],
            ["Vocabulary", "High-frequency daily words", "Collocations, phrasals, workplace core", "Precise professional/academic choices; nuance"],
            ["Expressions", "Greetings, simple requests", "Opinion/softening/clarifying frames", "Subtle disagreement, negotiation, humor control"],
            ["Conversation", "Short exchanges", "Maintain & repair conversations", "Lead discussions; manage face/politeness"],
            ["Workplace / SE", "Basic status phrases", "Meetings, reviews, incidents", "Architecture trade-offs; executive-clear updates"],
            ["Interview", "Simple self-intro", "STAR stories; clarify questions", "Think aloud with structure; negotiate uncertainty"],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_35():
    s = [part_header(35, "Quick Reference Tables",
        "Dense lookup tables for printing as a quick deck inside the full reference.")]
    s.append(h3("Consonant highlights (GA)"))
    s.append(table(["IPA", "Example"], [
        ["/ɹ/", "car, red, teacher"], ["/θ ð/", "think / this"], ["/ŋ/", "sing, think"],
        ["/ɾ/", "water, better, city"], ["/ʃ tʃ/", "ship / chip"], ["/dʒ/", "job, bridge"],
    ]))
    s.append(h3("Vowel highlights (GA)"))
    s.append(table(["Contrast", "Pairs"], [
        ["/i ɪ/", "sheep / ship"], ["/ɛ æ/", "bed / bad"], ["/æ ʌ/", "cat / cut"],
        ["/ʊ u/", "full / fool"], ["/ə/", "about, problem, support"],
    ]))
    s.append(h3("-s / -ed"))
    s.append(p("/s/ /z/ /ɪz/ · /t/ /d/ /ɪd/ — see Parts 13–14."))
    s.append(h3("Flap T / schwa / linking"))
    s.append(p("Flap between vowels before unstressed syllable · schwa in unstressed syllables · link final C to next V."))
    s.append(h3("Reductions (casual)"))
    s.append(p("gonna / wanna / gotta / kinda / lemme / gimme / didja / whaddya — prefer careful forms in interviews."))
    s.append(part_footer())
    return "\n".join(s)


def part_36():
    vocab = json.loads(DATA.read_text(encoding="utf-8"))
    s = [part_header(36, "Alphabetical Vocabulary Index",
        f"Index of {len(vocab)} core lexical items. Click through to entries in Part 17.")]
    # Group by first letter
    from collections import defaultdict
    buckets = defaultdict(list)
    for e in vocab:
        buckets[e["word"][0].upper()].append(e)
    s.append('<div class="index-alpha">')
    for letter in sorted(buckets):
        s.append(f'<div class="letter"><h4>{letter}</h4><ul>')
        for e in sorted(buckets[letter], key=lambda x: x["word"]):
            s.append(f'<li><a href="#v-{e["id"]}">{e["word"]}</a> <span class="pos">{e.get("level","")}</span></li>')
        s.append("</ul></div>")
    s.append("</div>")
    s.append(part_footer())
    return "\n".join(s)


def part_37():
    import re
    # Keep in sync with Part 23 expression texts
    texts = [
        "Hey, how's it going?", "Good to see you.", "Long time no see.",
        "How was your weekend?", "Crazy weather, huh?",
        "Got a minute?", "Quick question for you.",
        "I should let you go.", "Talk soon.",
        "Could you give me a hand with this?", "I'm stuck on…",
        "What exactly do you mean by…?", "Just to make sure I understand…",
        "That makes sense.", "Sounds good.",
        "That's a good point.", "I'm with you on that.",
        "I'm not sure I agree.", "I get where you're coming from, but…",
        "From my perspective…", "I feel like…",
        "I'm not sure.", "It depends.",
        "Sorry about that.", "I owe you an apology.",
        "I appreciate it.", "Thanks for the heads-up.",
        "Would you mind…?", "When you get a chance…",
        "I wish I could, but…", "That's not going to work for me.",
        "What if we…?", "If I were you, I'd…",
        "Let me think.", "That's a good question.",
        "I see what you mean.", "Tell me about it.",
        "Sorry to interrupt…", "Quick follow-up on that…",
        "Speaking of which…", "Anyway…",
        "This is getting out of hand.", "I'm a bit concerned about…", "That's awesome!",
    ]

    def eid(text):
        x = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48]
        return "e-" + x

    s = [part_header(37, "Alphabetical Expression Index",
        "Index of key daily expressions from Part 23.")]
    s.append('<div class="index-alpha"><div class="letter"><ul>')
    for text in sorted(texts, key=lambda x: x.lower()):
        s.append(f'<li><a href="#{eid(text)}">{text}</a></li>')
    s.append("</ul></div></div>")
    s.append(part_footer())
    return "\n".join(s)


def part_38():
    s = [part_header(38, "Master Reference Checklists",
        "Use these checklists periodically to audit pronunciation, vocabulary, and communication readiness.")]
    checks = {
        "Pronunciation Checklist": [
            "Rhotic R in car/first/teacher",
            "TH /θ/ and /ð/ distinct from /s t d z/",
            "Flap T recognized in water/better/city",
            "Schwa in unstressed syllables",
            "-s endings /s z ɪz/ audible",
            "-ed endings /t d ɪd/ correct syllable count",
            "Word stress on key professional terms",
            "Sentence stress on content/focus words",
            "Basic linking C→V",
            "Intonation fits statements vs yes/no questions",
        ],
        "Vocabulary Checklist": [
            "Can use core A1–A2 words without translation delay",
            "Know collocations for make/take/do/get/have",
            "Can recognize high-value B1–B2 workplace words",
            "Active use of key SE terms (deploy, latency, review…)",
            "Word families for decide/develop/communicate…",
            "Confusing pairs checked (affect/effect, job/work…)",
        ],
        "Expression Checklist": [
            "Open/close conversations naturally",
            "Clarify and confirm without freezing",
            "Disagree politely",
            "Buy thinking time professionally",
            "Register control (casual vs professional)",
        ],
        "Connected Speech Checklist": [
            "Hear gonna/wanna without confusion",
            "Decode weak forms of to/for/and/can",
            "Reconstruct careful English from casual audio",
            "Produce moderate linking without mumbling",
        ],
        "Workplace English Checklist": [
            "Status updates: on track / at risk / blocked",
            "Ask for clarification of requirements",
            "Give actionable feedback",
            "Negotiate deadlines and priorities",
        ],
        "Interview English Checklist": [
            "Clear self-intro under 60–90 seconds",
            "STAR behavioral answers",
            "Think-aloud frames under pressure",
            "Clarifying questions before coding/design",
            "Trade-off language (because / trade-off / consider)",
        ],
    }
    for title, items in checks.items():
        s.append(h3(title))
        s.append('<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
    s.append(part_footer())
    return "\n".join(s)


def parts_31_to_38():
    return "\n".join([
        part_31(), part_32(), part_33(), part_34(),
        part_35(), part_36(), part_37(), part_38(),
    ])
