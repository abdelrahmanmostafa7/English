"""Parts 1–8: How AE works through sentence stress."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, pron_box, box
)


def part_01():
    s = [part_header(1, "How American English Works",
        "Pronouncing words one-by-one is not enough. Natural American English is a system: sounds, stress, "
        "rhythm, intonation, and connected speech working together.")]
    s.append(h3("Core concepts", "p1-concepts"))
    s.append(table(
        ["Term", "Meaning", "Why it matters"],
        [
            ["Pronunciation", "How individual sounds and words are produced", "Accuracy of /r/, TH, vowels, endings"],
            ["Accent", "Overall sound pattern of a variety (e.g., General American)", "GA is the model here — not Hollywood imitation"],
            ["Fluency", "Smooth flow of speech with appropriate pacing", "Not the same as speed or native-like accent"],
            ["Intelligibility", "How easily listeners understand you", "Highest priority for most learners"],
            ["Rhythm", "Pattern of stressed and unstressed beats", "Makes English sound 'English'"],
            ["Stress", "Extra energy on a syllable or word", "Changes meaning and clarity"],
            ["Intonation", "Pitch movement across phrases", "Signals questions, attitude, politeness"],
            ["Connected speech", "How words link and reduce in real speech", "Why listening feels hard"],
        ],
    ))
    s.append(rule(
        "Why correct words can still sound unnatural",
        "If every syllable is equally strong, if function words are fully pronounced, if there is no linking, "
        "and if intonation is flat, speech can be accurate but foreign-sounding. Americans listen for stress peaks "
        "and compressed weak syllables.",
        examples_list=[
            "Word-by-word: I · AM · GO · ING · TO · MEET · YOU · TO · MOR · ROW (unnatural)",
            "Natural GA: I'm gonna meet you tomorrow / more carefully: I'm going to meet you tomorrow "
            "(with reductions on am/to and stress on meet / TOMorrow)",
        ],
        levels=["A2", "B1", "B2"],
    ))
    s.append(h3("The mastery path", "p1-path"))
    s.append(p(
        "<strong>Sound → Word → Stress → Expression → Sentence → Connected Speech → Conversation</strong>"
    ))
    s.append(ul(
        "Sound: consonants, vowels, diphthongs that affect intelligibility",
        "Word: clear citation form + American spelling→sound patterns",
        "Stress: correct syllable prominence inside words",
        "Expression: chunks and collocations, not isolated translations",
        "Sentence: content-word stress and focus",
        "Connected speech: linking, weak forms, Flap T, reductions",
        "Conversation: management phrases, register, repair strategies",
    ))
    s.append(note(
        "<p>This book supports practice you already do (shadowing, listening, speaking, writing). "
        "Use it to check <em>what</em> to aim for and <em>why</em> something sounded different.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_02():
    s = [part_header(2, "American English Sound System",
        "A practical map of General American sounds — enough phonetics to train your ear and mouth, "
        "without turning into an academic textbook.")]
    s.append(rule(
        "Phonemes and minimal pairs",
        "A phoneme is a sound that can change meaning. Minimal pairs prove a contrast matters: "
        "<em>ship/sheep</em>, <em>bit/beat</em>, <em>thin/then</em>.",
        examples_list=[
            "live /lɪv/ vs leave /liv/",
            "bad /bæd/ vs bed /bɛd/",
            "full /fʊl/ vs fool /ful/",
        ],
        levels=["A1", "A2", "B1"],
    ))
    s.append(table(
        ["Category", "What to notice in GA"],
        [
            ["Consonants", "Include /θ ð ɹ ŋ/; Flap T /ɾ/ in many words"],
            ["Vowels", "Tense/lax pairs; /æ/; often no British /ɒ/; cot–caught varies by region"],
            ["Diphthongs", "/aɪ aʊ ɔɪ eɪ oʊ/ — gliding vowels"],
            ["Voiced vs voiceless", "Vocal fold vibration: /s/ vs /z/, /f/ vs /v/, /θ/ vs /ð/"],
            ["Syllables", "Every word has ≥1 syllable; stress picks the strong one(s)"],
            ["IPA", "Used here for clarity; GA symbols (e.g., /ɹ/ or /r/ for American R)"],
        ],
    ))
    s.append(pron_box(
        "<p>This book uses a practical GA transcription style, e.g. <em>water</em> /ˈwɔɾɚ/ or /ˈwɑɾɚ/ "
        "(regional vowel varies; Flap T is the key American feature).</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def _sound(sym, name, voicing, mouth, spell, pairs, words, notes="", levels=None):
    return rule(
        f"{sym} — {name}",
        f"<strong>Voicing:</strong> {voicing}. <strong>Mouth:</strong> {mouth}",
        when=[f"Common spellings: {spell}", f"American note: {notes}"] if notes else [f"Common spellings: {spell}"],
        examples_list=[f"Words: {words}", f"Minimal pairs: {pairs}"],
        levels=levels or ["A1", "A2", "B1"],
    )


def part_03():
    s = [part_header(3, "Consonants",
        "Systematic consonant reference for General American. Focus on contrasts that affect intelligibility.")]
    sounds = [
        ("/p/", "voiceless bilabial stop", "voiceless", "Lips close; puff of air at start of stressed syllables (aspiration)",
         "p, pp", "pat/bat, peach/beach", "pen, happy, stop", "Aspirated in pin; softer after /s/ as in spin"),
        ("/b/", "voiced bilabial stop", "voiced", "Lips close; vocal folds vibrate",
         "b, bb", "pat/bat", "be, hobby, job", ""),
        ("/t/", "voiceless alveolar stop", "voiceless", "Tongue tip to ridge behind teeth",
         "t, tt, ed (/t/)", "tie/die, write/ride", "time, better, cat", "See Part 4 for Flap T / aspirated T / glottal T"),
        ("/d/", "voiced alveolar stop", "voiced", "Same place as /t/, with voice",
         "d, dd, ed (/d/)", "tie/die", "day, ready, made", "May also flap in some contexts"),
        ("/k/", "voiceless velar stop", "voiceless", "Back of tongue to soft palate",
         "k, c, ck, ch (school)", "coat/goat", "cat, back, school", "Aspirated in key"),
        ("/g/", "voiced velar stop", "voiced", "Same place as /k/, with voice",
         "g, gg", "coat/goat", "go, bigger, bag", ""),
        ("/f/", "voiceless labiodental fricative", "voiceless", "Upper teeth on lower lip; continuous air",
         "f, ph, gh (laugh)", "fan/van, safe/save", "for, phone, laugh", ""),
        ("/v/", "voiced labiodental fricative", "voiced", "Same as /f/ with voice",
         "v", "fan/van", "very, have, of (/əv/)", "of usually /əv/; careful speech may reduce further"),
        ("/θ/", "voiceless dental fricative (TH)", "voiceless", "Tongue lightly between/near teeth; air friction — not /s/ or /t/",
         "th", "thin/sin, thigh/tie", "think, both, math", "Critical American sound — Part 4"),
        ("/ð/", "voiced dental fricative (TH)", "voiced", "Same place as /θ/ with voice",
         "th", "then/den, they/day", "the, this, brother", "Function words often use /ð/"),
        ("/s/", "voiceless alveolar fricative", "voiceless", "Narrow groove; hissy air",
         "s, ss, c (city), x", "sip/zip, price/prize", "see, miss, race", ""),
        ("/z/", "voiced alveolar fricative", "voiced", "Same as /s/ with voice",
         "z, s (as /z/), x", "sip/zip", "zoo, easy, dogs", "Plural/3rd-person -s often /z/ — Part 13"),
        ("/ʃ/", "voiceless postalveolar fricative (SH)", "voiceless", "Lips rounded; tongue farther back than /s/",
         "sh, ti (nation), ci,ssi", "shoe/chew, ship/chip", "she, nation, pressure", ""),
        ("/ʒ/", "voiced postalveolar fricative", "voiced", "Same as /ʃ/ with voice",
         "s (measure), ge (beige)", "confusion/Confucian (advanced)", "measure, vision, garage (GA often /ʒ/ or /dʒ/)", "Less common; learn in key words"),
        ("/tʃ/", "voiceless affricate (CH)", "voiceless", "Stop + fricative: /t/+/ʃ/",
         "ch, tch, tu (nature)", "chip/ship, cheap/jeep", "chair, watch, nature", ""),
        ("/dʒ/", "voiced affricate (J)", "voiced", "Stop + fricative: /d/+/ʒ/",
         "j, g (giant), dge", "jeep/cheap", "job, bridge, graduate", ""),
        ("/h/", "voiceless glottal fricative", "voiceless (breath)", "Open vocal tract; breathy onset",
         "h, wh (sometimes)", "heat/eat", "he, ahead, who", "Often reduced/deleted in unstressed he/him/her in fast speech"),
        ("/m/", "bilabial nasal", "voiced", "Lips closed; air through nose",
         "m, mm, mb (silent b)", "map/nap", "me, summer, comb", ""),
        ("/n/", "alveolar nasal", "voiced", "Tongue tip up; air through nose",
         "n, nn, kn (silent k)", "map/nap", "no, dinner, know", ""),
        ("/ŋ/", "velar nasal (NG)", "voiced", "Back of tongue up like /k/; nasal airflow — no hard /g/ needed in singer",
         "ng, n before /k g/", "thin/thing, sin/sing", "sing, think, bank", "Part 4 — avoid adding /g/ in -ing for most GA speakers"),
        ("/l/", "alveolar lateral", "voiced", "Tongue tip up; air around sides",
         "l, ll", "light/right, late/rate", "like, call, people", "Clear L vs dark L — Part 4"),
        ("/r/ (/ɹ/)", "American rhotic approximant", "voiced", "Tongue bunched/retroflex; no lip trill; tip not tapping",
         "r, rr, wr", "right/light, raw/law", "red, car, write", "Rhotic R — Part 4 (core American feature)"),
        ("/w/", "labio-velar approximant", "voiced", "Rounded lips + raised back tongue; glide",
         "w, wh", "wet/vet, wine/vine", "we, always, what", "Keep distinct from /v/"),
        ("/j/", "palatal approximant (Y)", "voiced", "Tongue near hard palate; glide into vowel",
         "y, i (onion), u (use=/jus/)", "yet/jet", "yes, you, music", "you/your often reduce in connected speech"),
    ]
    for row in sounds:
        s.append(_sound(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    s.append(part_footer())
    return "\n".join(s)


def part_04():
    s = [part_header(4, "Important American Sounds",
        "Dedicated training targets for General American: R, TH, Flap T, American T variants, L, and NG.")]
    s.append(h3("American R (rhotic)", "p4-r"))
    s.append(rule(
        "Rhotic R",
        "General American pronounces /r/ after vowels: car, hard, first, teacher. "
        "(Many British accents drop post-vocalic R.)",
        when=[
            "Initial: red, right, really — tongue bunched; no lip vibration",
            "Medial: very, story, sorry",
            "Final / r-colored: car /kɑr/, more /mɔr/, bird /bɝd/, teacher /ˈtitʃɚ/",
            "R-colored vowels: /ɝ/ (stressed, bird), /ɚ/ (unstressed, teacher)",
        ],
        examples_list=[
            "car, hard, first, nurse, better, computer",
            "Mirror practice: hold tongue tense without touching the roof hard",
        ],
        mistakes_list=[
            ("cah (dropping R)", "car /kɑr/", "Keep rhotic R in GA"),
            ("trilled Spanish-like R", "American approximant /ɹ/", "No tap/trill for standard GA"),
        ],
        levels=["A2", "B1", "B2"],
    ))
    s.append(h3("TH — /θ/ and /ð/", "p4-th"))
    s.append(table(
        ["Sound", "Voicing", "Typical words"],
        [
            ["/θ/", "voiceless", "think, thank, both, math, three, birthday"],
            ["/ð/", "voiced", "the, this, that, these, those, brother, mother, weather"],
        ],
    ))
    s.append(mistakes(
        ("tink / sink for think", "think with tongue at teeth /θ/", "Not /t/ or /s/"),
        ("dis / zat for this", "this /ðɪs/", "Voiced TH, not /d/ or /z/"),
    ))
    s.append(h3("Flap T /ɾ/", "p4-flap"))
    s.append(rule(
        "When T (and sometimes D) becomes a flap",
        "In GA, /t/ or /d/ between vowels often becomes a quick tap /ɾ/ when the following syllable is unstressed. "
        "It can sound like a soft 'd' to learners.",
        when=[
            "Common: water, better, city, pretty, waiting, meeting, computer (middle t), Saturday",
            "After /n/ sometimes nasal flap: twenty ≈ twenny (casual)",
            "Does NOT flap when: T starts a stressed syllable (attain, return), or after consonants in many cases (after), or careful citation speech",
            "Spelling still t/tt — pronunciation changes",
        ],
        examples_list=[
            "water /ˈwɔɾɚ/ · better /ˈbɛɾɚ/ · city /ˈsɪɾi/ · pretty /ˈprɪɾi/",
            "waiting /ˈweɪɾɪŋ/ · writer ≈ rider in many accents (context disambiguates)",
        ],
        levels=["B1", "B2", "C1"],
    ))
    s.append(h3("American T variants (practical)", "p4-t"))
    s.append(table(
        ["Variant", "Where", "Example"],
        [
            ["Aspirated [tʰ]", "Start of stressed syllable", "time, attack (second t)"],
            ["Unaspirated [t]", "After /s/", "stop, stay, student"],
            ["Flap [ɾ]", "Vowel_T_unstressedV", "better, city"],
            ["Unreleased [t̚]", "End of words/phrases (common)", "cat_, that_ (hold, little release)"],
            ["Glottalized /ʔ/ influence", "Before /n/ or casual button/mountain", "button ≈ bu'n (casual GA)"],
        ],
    ))
    s.append(note("<p>Train Flap T and final unreleased T for listening first; produce them gradually so you stay intelligible.</p>"))
    s.append(h3("Clear L vs dark L", "p4-l"))
    s.append(rule(
        "L quality",
        "Clear L (lighter) often before vowels: light, leave, hello. "
        "Dark L (tongue back raised) often at ends and before consonants: feel, full, milk, people.",
        examples_list=["light vs feel", "law vs ball", "play vs help"],
        levels=["B1", "B2"],
    ))
    s.append(h3("NG /ŋ/", "p4-ng"))
    s.append(rule(
        "/ŋ/",
        "Make /ŋ/ with the tongue position of /k/ but nasal airflow. In words like <em>singer</em>, GA usually has no hard /g/. "
        "<em>finger</em> does include /g/: /ˈfɪŋɡɚ/.",
        examples_list=["sing, singing, thing, think (/ŋk/), bank, long"],
        mistakes_list=[
            ("sin-gin with hard g in singing", "singing /ˈsɪŋɪŋ/", "No extra /g/ for most -ing forms"),
            ("replacing /ŋ/ with /n/", "thing ≠ thin", "Keep velar place"),
        ],
        levels=["A2", "B1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_05():
    s = [part_header(5, "American Vowels",
        "Practical GA vowel contrasts that change meaning. Regional variation exists (cot–caught); "
        "focus on contrasts that stay important for intelligibility.")]
    s.append(table(
        ["Contrast", "Examples", "Tip"],
        [
            ["/i/ vs /ɪ/", "sheep/ship, leave/live, seat/sit", "Tense /i/ longer & fronter; /ɪ/ laxer"],
            ["/ɛ/ vs /æ/", "bed/bad, said/sad, pen/pan", "/æ/ more open (GA 'cat' is distinctive)"],
            ["/æ/ vs /ʌ/", "cat/cut, bat/but, ran/run", "/ʌ/ more central (strut)"],
            ["/ɑ/ vs /ɔ/", "cot/caught (merged for many Americans)", "If merged, both may sound like /ɑ/; still learn spellings"],
            ["/ʊ/ vs /u/", "full/fool, pull/pool", "/u/ tenser, often with lip rounding"],
            ["/ʌ/ vs /ɑ/", "cut/cot, luck/lock", "Central vs open back"],
        ],
    ))
    s.append(h3("Core vowels & diphthongs", "p5-core"))
    s.append(table(
        ["IPA", "Keyword", "Notes"],
        [
            ["/i/", "fleece / see", "beat, need, key"],
            ["/ɪ/", "kit / sit", "big, women (/ˈwɪmɪn/)"],
            ["/ɛ/", "dress / bed", "said, friend"],
            ["/æ/", "trap / cat", "ask, laugh (GA /æ/)"],
            ["/ɑ/", "lot/father (GA)", "stop, father; cot"],
            ["/ɔ/", "thought (if distinct)", "law, bought — varies"],
            ["/ʊ/", "foot / book", "put, could"],
            ["/u/", "goose / food", "new, true"],
            ["/ʌ/", "strut / cup", "love, money"],
            ["/ə/", "schwa / about", "See Part 6 — most common vowel"],
            ["/ɝ/ /ɚ/", "bird / teacher", "R-colored"],
            ["/eɪ/", "face / day", "make, wait"],
            ["/aɪ/", "price / my", "time, write"],
            ["/ɔɪ/", "choice / boy", "point, noise"],
            ["/oʊ/", "goat / go", "home, know (GA /oʊ/)"],
            ["/aʊ/", "mouth / now", "out, down"],
        ],
    ))
    s.append(examples(
        "ship /ʃɪp/ vs sheep /ʃip/",
        "live /lɪv/ vs leave /liv/",
        "bad /bæd/ vs bed /bɛd/",
        "cut /kʌt/ vs cat /kæt/",
        "full /fʊl/ vs fool /ful/",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_06():
    s = [part_header(6, "Schwa & Vowel Reduction",
        "Schwa /ə/ is the most common vowel in American English. Unstressed syllables shrink — "
        "this is a major reason American speech sounds fast.")]
    s.append(rule(
        "What is schwa?",
        "Schwa /ə/ is a short, neutral, central vowel in unstressed syllables: <em>about, problem, support, banana</em>.",
        examples_list=[
            "a<strong>bout</strong> /əˈbaʊt/",
            "<strong>prob</strong>lem /ˈprɑbləm/",
            "sup<strong>port</strong> /səˈpɔrt/",
            "pho<strong>to</strong>graph /ˈfoʊtəɡræf/ vs pho<strong>tog</strong>raphy /fəˈtɑɡrəfi/",
        ],
        levels=["A2", "B1", "B2"],
    ))
    s.append(rule(
        "Function-word reduction",
        "Small grammar words often reduce in natural speech: a, an, the, to, for, of, and, can, you…",
        examples_list=[
            "the → /ðə/ before consonants; /ði/ before vowels (careful)",
            "to → /tə/ : want to go ≈ wanna go (casual)",
            "for → /fɚ/ or /fər/: for a minute",
            "and → /ən/ or /n/: rock and roll ≈ rock 'n' roll",
            "can (ability) → /kən/; can't stays stronger /kænt/",
        ],
        levels=["B1", "B2", "C1"],
    ))
    s.append(warning(
        "<p>Do not reduce content words (nouns, main verbs, adjectives, adverbs) the same way. "
        "Over-reducing stressed words hurts clarity — especially at work.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_07():
    s = [part_header(7, "Word Stress",
        "English is stress-timed at the word level too: one syllable usually carries primary stress. "
        "Wrong stress often hurts intelligibility more than a slightly wrong vowel.")]
    s.append(rule(
        "Primary vs secondary stress",
        "Primary stress is the strongest syllable. Longer words may also have secondary stress.",
        examples_list=[
            "com<strong>PU</strong>ter · infor<strong>MA</strong>tion · ˌengiˈneer",
            "PHOtograph · phoTOgraphy · photoGRAPHic",
        ],
        levels=["A2", "B1", "B2"],
    ))
    s.append(table(
        ["Pattern", "Examples"],
        [
            ["Two-syllable nouns often first syllable", "TAble, WINdow, PROblem (many exceptions)"],
            ["Two-syllable verbs often second syllable", "deCIDE, beGIN, reCEIVE (many exceptions)"],
            ["Noun/verb pairs", "REcord (n) / reCORD (v); OBject / obJECT; PREsent / preSENT"],
            ["Compounds (nouns)", "STRES on first: POSToffice, SOFTware, CHECKout"],
            ["Compounds (adjectives often second when predicative nuance)", "old-FASHioned; stress can shift with focus"],
            ["Suffix -tion/-sion", "Stress usually on syllable before: naTION, deCIsion, inforMAtion"],
            ["Suffix -ic", "Stress usually before -ic: ecoNOmic, scienTIfic"],
            ["Suffix -ity", "Stress before -ity: possiBIlity, creaTIvity"],
            ["Prefixes un-/re-/in- often unstressed", "unHAPPy, reWRITE (unless contrastive)"],
        ],
    ))
    s.append(mistakes(
        ("comPUter with final stress", "comPUter /kəmˈpjutɚ/"),
        ("DEVelopment with wrong peak", "deVELopment /dɪˈvɛləpmənt/"),
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_08():
    s = [part_header(8, "Sentence Stress",
        "In sentences, Americans stress content words and reduce function words. "
        "Moving the focus stress changes meaning.")]
    s.append(table(
        ["Usually stressed (content)", "Usually unstressed (function)"],
        [
            ["Nouns, main verbs, adjectives, adverbs, WH-words, negatives", "a/an/the, to/of/for, and/but, pronouns, aux (unless focused)"],
        ],
    ))
    s.append(rule(
        "Focus and contrastive stress",
        "New or important information gets the nuclear stress. Contrastive stress highlights an alternative.",
        examples_list=[
            "I need the rePORT (not the slides).",
            "SHE fixed it (not me).",
            "I didn't say he stole the money. (deny saying)",
            "I didn't say HE stole the money. (someone else?)",
            "I didn't say he STOLE the money. (maybe borrowed)",
            "I didn't say he stole the MONEY. (maybe something else)",
        ],
        levels=["B1", "B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def parts_1_to_8():
    return "\n".join([part_01(), part_02(), part_03(), part_04(),
                      part_05(), part_06(), part_07(), part_08()])
