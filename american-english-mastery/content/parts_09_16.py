"""Parts 9–16: Rhythm through pronunciation troubleshooting."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, pron_box
)


def part_09():
    s = [part_header(9, "American Rhythm",
        "American English rhythm is stress-timed: stressed syllables come at roughly regular beats, "
        "while unstressed syllables compress. That compression — not raw speed — often makes speech sound fast.")]
    s.append(rule(
        "Stressed beats and thought groups",
        "Speak in thought groups (chunks of meaning). Inside each group, hit content-word beats and shrink the rest.",
        examples_list=[
            "I'm / WORKing on / the PAYment BUG // I'll UPDate you / after LUNCH.",
            "Clap only on capitals while saying the line naturally.",
        ],
        levels=["B1", "B2", "C1"],
    ))
    s.append(ul(
        "Rhythm groups ≈ short phrases between brief pauses",
        "Reductions and schwa keep timing even",
        "Over-pronouncing every word destroys rhythm and can sound robotic",
        "In professional settings, keep rhythm natural but avoid extreme casual reductions",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_10():
    s = [part_header(10, "Intonation",
        "Pitch movement signals sentence type and attitude. Train patterns that matter for clarity and politeness.")]
    s.append(table(
        ["Pattern", "Common use", "Example"],
        [
            ["Falling ↘", "Statements, WH-questions, confident ends", "It's ready↘ · Where do you work↘"],
            ["Rising ↗", "Yes/No questions, checking, friendliness", "Are you free↗ · Ready↗"],
            ["Fall-rise ↘↗", "Uncertainty, polite disagreement, implication", "I could↘↗ · It's possible↘↗"],
            ["List intonation", "Rise on items, fall on last", "We need auth↗, tests↗, and docs↘"],
            ["Surprise / echo", "Higher rise or wider range", "You deleted proDUction↗"],
        ],
    ))
    s.append(note(
        "<p>Sarcasm often uses exaggerated or mismatched intonation with the words — recognize it in listening; "
        "use carefully in speech.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_11():
    s = [part_header(11, "Connected Speech",
        "Words blend in natural American speech. Train these processes for listening first, then careful production.")]
    s.append(table(
        ["Process", "What happens", "Example"],
        [
            ["C→V linking", "Final consonant links to next vowel", "pick_up · turn_off · an_apple"],
            ["V→V linking", "Glide /w/ or /j/ may appear", "go_away ≈ go_waway · I_agree ≈ I_yagree"],
            ["C→C transitions", "Blend or simplify clusters", "best_time · next_week"],
            ["Weak forms", "Function words reduce", "for /fɚ/ · to /tə/ · and /ən/"],
            ["Assimilation", "Sound becomes more like neighbor", "ten bells ≈ tem bells (casual) · did you ≈ didʒə"],
            ["Elision", "Sound drops", "friendship (d may weaken) · camera ≈ camra"],
            ["Contractions", "Grammar words fuse", "I'm, don't, we've, she's"],
            ["Flap T", "See Part 4", "get_out ≈ geɾ_out in fast speech sometimes"],
        ],
    ))
    s.append(examples(
        "What do you want? → Whaddya want? (casual) / What do you want? (careful)",
        "Did you eat yet? → Didja eat yet? (casual)",
        "Could you help me? → Couldja help me? (casual)",
    ))
    s.append(warning(
        "<p>Professional rule: understand heavy reductions; produce moderate linking and weak forms. "
        "Extreme reductions can hurt credibility in interviews and client calls.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_12():
    s = [part_header(12, "Common American Reductions",
        "Reference for careful vs conversational forms. Use conversational reductions in casual talk; "
        "prefer clearer forms at work when precision matters.")]
    rows = [
        ["going to", "going to", "gonna", "I'm gonna ship it (casual)"],
        ["want to", "want to", "wanna", "I wanna ask something"],
        ["have to", "have to", "hafta / have to", "I have to leave / I hafta leave"],
        ["got to", "have got to", "gotta", "I gotta go (casual)"],
        ["kind of", "kind of", "kinda", "It's kinda slow"],
        ["sort of", "sort of", "sorta", "I sorta agree"],
        ["give me", "give me", "gimme", "Gimme a second"],
        ["let me", "let me", "lemme", "Lemme check"],
        ["tell him/her", "tell him", "tell 'im / teller (fast)", "Tell 'im I'll call"],
        ["did you", "did you", "didja /dɪdʒə/", "Didja see that?"],
        ["what do you", "what do you", "whaddya / whatcha", "Whaddya think?"],
        ["could you", "could you", "couldja", "Couldja review this?"],
        ["would you", "would you", "wouldja", "Wouldja mind waiting?"],
        ["should you", "should you", "shouldja (less common)", "Should you restart it? (usually clear)"],
        ["don't know", "don't know", "dunno", "I dunno (casual)"],
        ["out of", "out of", "outta", "I'm outta time"],
    ]
    s.append(table(["Phrase", "Careful", "Conversational", "Note"], rows))
    s.append(note(
        "<p><span class='register'>professional</span> Prefer <em>going to / want to / have to</em> in interviews, "
        "demos, and client meetings. Reductions are fine in standup banter with teammates who share that register.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_13():
    s = [part_header(13, "Final -S Rules",
        "Plural nouns, 3rd-person singular verbs, and possessives share three pronunciation endings: /s/, /z/, /ɪz/.")]
    s.append(table(
        ["Ending", "After", "Examples"],
        [
            ["/s/", "voiceless sounds (p t k f θ)", "cats, books, laughs, months (careful), waits"],
            ["/z/", "voiced sounds & vowels", "dogs, drives, plays, keys, needs"],
            ["/ɪz/ or /əz/", "sibilants /s z ʃ ʒ tʃ dʒ/", "buses, boxes, watches, judges, wishes, quizzes"],
        ],
    ))
    s.append(mistakes(
        ("watchs /watʃs/", "watches /ˈwɑtʃɪz/"),
        ("dropping -s entirely", "She works /wɝks/", "Keep the ending audible"),
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_14():
    s = [part_header(14, "Final -ED Rules",
        "Past tense, past participles, and many adjectives ending in -ed use /t/, /d/, or /ɪd/.")]
    s.append(table(
        ["Ending", "After", "Examples"],
        [
            ["/t/", "voiceless (except /t/)", "watched, liked, missed, fixed, stopped"],
            ["/d/", "voiced (except /d/) & vowels", "played, called, cleaned, used, loved"],
            ["/ɪd/ or /əd/", "/t/ or /d/", "wanted, needed, decided, started, downloaded"],
        ],
    ))
    s.append(note(
        "<p>Adjective note: <em>aged wine</em> vs <em>aged /ˈeɪdʒɪd/ man</em> — a few adjectives keep /ɪd/ unexpectedly "
        "(learned/blessed vary). Learn common ones as chunks.</p>"
    ))
    s.append(mistakes(
        ("wantəd with wrong vowel stress", "wanted /ˈwɑntɪd/ — extra syllable only after t/d"),
        ("watchɛd as two heavy syllables", "watched /wɑtʃt/ — one syllable"),
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_15():
    s = [part_header(15, "Spelling → Pronunciation",
        "English spelling is partly patterned, partly historical. Use reliable patterns; memorize exceptions.")]
    s.append(table(
        ["Pattern", "Typical sound", "Reliability"],
        [
            ["silent e (make, time)", "previous vowel 'says its name' often", "Useful tendency; many exceptions"],
            ["ai/ay, ee/ea", "/eɪ/, /i/ commonly", "High but not perfect (said, steak)"],
            ["oa/ow (goat, know)", "/oʊ/ commonly", "ow also /aʊ/ (now)"],
            ["oo", "/u/ food · /ʊ/ book", "Must learn by word"],
            ["ough", "many: though /oʊ/, through /u/, tough /ʌf/, cough /ɔf/, bough /aʊ/", "Low — memorize"],
            ["augh", "laugh /æf/ (GA), taught /ɔt/", "Limited set"],
            ["tion / sion", "/ʃən/ · /ʒən/ (vision)", "High for -tion"],
            ["ture", "/tʃɚ/ nature, culture", "High"],
            ["ph", "/f/ phone", "High"],
            ["ch", "/tʃ/ chair · /k/ school · /ʃ/ machine", "Medium — word-based"],
            ["th", "/θ/ or /ð/", "See Part 4"],
            ["wh", "/w/ what (GA) · /h/ who", "GA usually /w/"],
            ["kn- / wr- / -mb", "silent k/w/b: know, write, comb", "High for these clusters"],
            ["c before e/i/y", "often /s/ city", "Useful"],
            ["g before e/i/y", "often /dʒ/ giant (many exceptions: get, give)", "Medium"],
        ],
    ))
    s.append(warning("<p>Never assume spelling fully predicts GA pronunciation — check stress + IPA for new professional terms.</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_16():
    s = [part_header(16, "Pronunciation Difficulties for Learners",
        "Troubleshooting guide: if X sounds wrong, check these targets and minimal pairs.")]
    s.append(table(
        ["If this is hard…", "Check…", "Minimal pairs / drills"],
        [
            ["R", "Tongue bunch; rhotic endings; no trill", "right/light · raw/law · car (hold /r/)"],
            ["TH", "Tongue at teeth; /θ/ vs /ð/", "thin/tin · then/den · think/sink"],
            ["W vs V", "Lip rounding /w/ vs teeth-on-lip /v/", "west/vest · wine/vine"],
            ["P/B", "Aspiration on stressed p; voicing on b", "pat/bat · peach/beach"],
            ["F/V", "Continuous friction; voicing", "fan/van · safe/save"],
            ["S/Z", "Voicing; -s endings", "sip/zip · price/prize"],
            ["SH/CH", "Fricative vs affricate", "ship/chip · wash/watch"],
            ["L/R", "L lateral vs R approximant", "late/rate · light/right · collect/correct"],
            ["Short vs long vowels", "Lax/tense pairs; length + quality", "ship/sheep · full/fool · live/leave"],
            ["Stress", "Primary stress syllable", "PHOtograph / phoTOgraphy"],
            ["Schwa", "Unstressed syllables reduce", "about · problem · support"],
            ["Word endings", "-s / -ed rules; final consonants", "liked / wants / needed"],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def parts_9_to_16():
    return "\n".join([
        part_09(), part_10(), part_11(), part_12(),
        part_13(), part_14(), part_15(), part_16(),
    ])
