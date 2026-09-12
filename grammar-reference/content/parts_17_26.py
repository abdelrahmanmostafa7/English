"""Parts 17–26: Negation through Punctuation."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, box
)


def part_17():
    s = []
    s.append(part_header(17, "Negation",
        "English negation uses <em>not</em>, negative determiners/pronouns (<em>no, nothing</em>), and negative adverbs "
        "(<em>never, hardly</em>). Word order, scope, and inversion matter at higher levels."))

    s.append(rule(
        "not with auxiliaries",
        "Place <em>not</em> (n't) after the first auxiliary/modal/be. Use do-support with simple present/past lexical verbs.",
        examples_list=[
            "She is not available. / She isn't available.",
            "We have not finished. / We haven't finished.",
            "They do not agree. / They don't agree.",
            "I did not approve that PR.",
        ],
        levels=["A1", "A2"],
    ))

    s.append(rule(
        "no vs not / nothing vs not anything",
        "<em>no</em> + noun; <em>not</em> + article/determiner phrase. Negative pronouns already negate — avoid double negation in standard English.",
        examples_list=[
            "There is no evidence. / There isn't any evidence.",
            "I have no idea. / I don't have any idea.",
            "Nobody called. / I didn't see anyone.",
            "Nothing changed. / I didn't change anything.",
        ],
        mistakes_list=[
            ("I don't know nothing.", "I don't know anything. / I know nothing.", "Standard English avoids double negatives."),
            ("She didn't say nothing.", "She didn't say anything."),
        ],
        levels=["A2", "B1"],
    ))

    s.append(table(
        ["Negative form", "Example"],
        [
            ["never", "We never store plaintext passwords."],
            ["nobody / no one", "Nobody owns that service."],
            ["nothing", "Nothing is blocked."],
            ["nowhere", "The package is nowhere in the registry."],
            ["neither… nor…", "Neither the API nor the UI failed."],
            ["hardly / barely / scarcely", "We hardly ever reboot production. (already negative in meaning)"],
            ["seldom / rarely", "They rarely miss standups."],
        ],
    ))

    s.append(warning(
        "<p>Adverbs like <em>hardly, barely, scarcely, never, seldom</em> are negative in meaning. "
        "Do not add another negation: <span class='wrong'>I can't hardly see</span> → "
        "<span class='correct'>I can hardly see</span>.</p>"
    ))

    s.append(rule(
        "Negative inversion (formal/emphatic)",
        "When a negative/limiting adverbial starts the clause, invert auxiliary and subject.",
        examples_list=[
            "Never have I seen such clean logs.",
            "Rarely do we get zero incidents in a month.",
            "Hardly had we deployed when alerts fired.",
            "Not only did they fix the bug, but they also added tests.",
            "Under no circumstances should you commit secrets.",
        ],
        levels=["C1", "C2"],
    ))

    s.append(rule(
        "Scope of negation",
        "Where <em>not</em> sits changes meaning. Compare quantifiers and focus.",
        examples_list=[
            "I didn't advise everyone to quit. (maybe advised some)",
            "I advised everyone not to quit.",
            "All engineers are not on-call. (ambiguous) → Prefer: Not all engineers are on-call. / No engineers are on-call.",
        ],
        levels=["B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_18():
    s = []
    s.append(part_header(18, "Clauses",
        "Clauses are the main way English builds complex meaning: noun clauses as subjects/objects, "
        "relative clauses as noun modifiers, and adverb clauses as circumstance markers."))

    s.append(h3("Noun clauses", "p18-noun"))
    s.append(rule(
        "Noun (content) clauses",
        "Introduced by <em>that, if/whether, wh-words</em>. They act as subjects, objects, or complements.",
        examples_list=[
            "I know that the deadline is Friday.",
            "Whether we ship depends on QA.",
            "What we need is clearer ownership. (also cleft-like)",
            "The question is why latency spiked.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Relative clauses", "p18-rel"))
    s.append(rule(
        "Defining vs non-defining",
        "Defining (restrictive) clauses identify which one; no commas. "
        "Non-defining add extra information; use commas; do not use <em>that</em>; do not omit the pronoun.",
        examples_list=[
            "Defining: Engineers who write tests ship faster.",
            "Defining: The library that we chose is typed.",
            "Non-defining: Our CTO, who joined in 2019, prefers Rust.",
            "Non-defining: The old API, which we deprecated, still gets traffic.",
        ],
        mistakes_list=[
            ("Our CTO who joined in 2019 prefers Rust.", "Add commas if there is only one CTO."),
            ("The API, that we deprecated, still gets traffic.", "Use which (or who) after a comma — not that."),
        ],
        levels=["B1", "B2"],
    ))

    s.append(table(
        ["Pronoun / adverb", "Use"],
        [
            ["who / whom / whose", "people; whom = object (formal)"],
            ["which", "things; non-defining; also clause reference"],
            ["that", "defining clauses (people/things); not after comma"],
            ["where / when / why", "place / time / reason relative adverbs"],
            ["∅ (omission)", "object pronoun in defining clauses: the tool (that) we use"],
        ],
    ))

    s.append(rule(
        "Reduced relative clauses",
        "Defining clauses can reduce: active → present participle; passive → past participle.",
        examples_list=[
            "Engineers working remotely must VPN in. (= who work)",
            "Tickets closed last week are archived. (= that were closed)",
            "The people invited to the demo arrived early. (= who were invited)",
        ],
        levels=["B2", "C1"],
    ))

    s.append(h3("Adverb clauses", "p18-adv"))
    s.append(table(
        ["Meaning", "Subordinators", "Example"],
        [
            ["Time", "when, while, as, before, after, until, since, as soon as, once", "After we merged, we tagged a release."],
            ["Reason", "because, since, as", "Because the cache was cold, latency rose."],
            ["Purpose", "so that, in order that", "We logged verbosely so that we could debug."],
            ["Result", "so… that, such… that", "It was so slow that users bounced."],
            ["Contrast", "while, whereas", "Staging is green, whereas production is flaky."],
            ["Concession", "although, though, even though, while", "Although we rushed, quality held."],
            ["Condition", "if, unless, provided, as long as", "Unless it fails, we proceed."],
            ["Comparison", "as… as, than, the way", "It behaved as we expected."],
        ],
    ))

    s.append(rule(
        "Reduced adverb clauses",
        "When subjects match, some adverb clauses reduce to participial or verbless clauses.",
        examples_list=[
            "While reviewing the PR, she found a race condition.",
            "If necessary, roll back.",
            "Although exhausted, he finished the postmortem.",
        ],
        levels=["B2", "C1"],
    ))
    s.append(warning(
        "<p>Avoid dangling modifiers: <span class='wrong'>Walking into the office, the coffee smelled great.</span> "
        "→ <span class='correct'>Walking into the office, I noticed the coffee smelled great.</span></p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_19():
    s = []
    s.append(part_header(19, "Comparison",
        "Comparison covers comparative/superlative forms, equality structures, modifiers of degree, "
        "and advanced correlative patterns."))

    s.append(rule(
        "Forming comparatives and superlatives",
        "One-syllable: -er/-est. Two syllables: often -er or more; -y → ier. Three+: more/most. "
        "Irregular: good/better/best; bad/worse/worst; far/farther|further; little/less/least; many|much/more/most.",
        examples_list=[
            "faster, simpler, happier, more reliable, most secure",
            "This build is better than the last one.",
            "She is the most careful reviewer on the team.",
        ],
        mistakes_list=[
            ("more faster", "faster / much faster"),
            ("the most unique", "unique / truly unique", "Avoid grading absolute adjectives carelessly."),
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Equality and inequality",
        "<em>as… as</em> for equality; <em>not as/so… as</em> for inequality. "
        "<em>less/fewer</em> for lower degree/quantity; <em>more/most</em> for higher.",
        examples_list=[
            "Go is as fast as we need for this service.",
            "The UI is not as intuitive as the old one.",
            "fewer tickets / less downtime / less noise",
        ],
        levels=["A2", "B1"],
    ))
    s.append(note(
        "<p>Careful usage: <em>fewer</em> with plurals, <em>less</em> with uncountables. "
        "Spoken English often uses <em>less</em> with plurals (<em>less tickets</em>) — marked in formal writing.</p>"
    ))

    s.append(rule(
        "Modifying comparatives",
        "Intensify with <em>much, far, a lot, way (informal), significantly</em>. Soften with <em>a bit, slightly, rather</em>. "
        "Do not use <em>very</em> directly before a comparative (*very better).",
        examples_list=[
            "much clearer, far more stable, a lot easier, slightly worse",
            "The more we automate, the fewer incidents we see.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Advanced comparison patterns",
        "Correlative <em>the… the…</em>, double marking (usually avoided), progressive comparison with <em>increasingly</em>.",
        examples_list=[
            "The sooner we decide, the better.",
            "The more carefully you test, the fewer regressions you ship.",
            "Increasingly complex systems need better observability.",
            "This approach is becoming more and more popular.",
        ],
        levels=["B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_20():
    s = []
    s.append(part_header(20, "Participles & Participial Clauses",
        "Participles (-ing / -ed / having + PP) create compact modifiers and adverbial clauses. "
        "They are powerful in formal writing and dangerous when dangling."))

    s.append(rule(
        "Present, past, and perfect participles",
        "Present participle: V-ing (active/in-progress). Past participle: V-ed/irregular (often passive/completed). "
        "Perfect participle: having + PP (earlier completion).",
        examples_list=[
            "a growing codebase; growing quickly, the team hired more engineers",
            "written documentation; Written in Rust, the service uses little memory",
            "Having finished the migration, we deleted the legacy tables.",
        ],
        levels=["B1", "B2", "C1"],
    ))

    s.append(rule(
        "Participial adjectives",
        "Many participles act as adjectives: interesting/interested, surprising/surprised, frozen, dedicated.",
        examples_list=[
            "a dedicated engineer; frozen requirements; a surprising result",
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Participial clauses",
        "They can express time, reason, result, or concession when the subject matches the main clause.",
        examples_list=[
            "Walking into the office, I noticed the monitors were off.",
            "Being tired, she postponed the demo.",
            "Compared with last quarter, churn is lower.",
            "Given that the risk is high, we should wait.",
            "Having been warned twice, he still committed the key. (perfect passive participle)",
        ],
        levels=["B2", "C1"],
    ))

    s.append(warning(
        "<p><strong>Dangling participle:</strong> the implied subject of the participle must be the main-clause subject.</p>"
        "<p><span class='wrong'>Having failed the tests, the release was cancelled.</span> "
        "(The release did not fail the tests.)</p>"
        "<p><span class='correct'>Having failed the tests, we cancelled the release.</span> / "
        "<span class='correct'>Because the tests failed, the release was cancelled.</span></p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_21():
    s = []
    s.append(part_header(21, "Causative Structures",
        "Causatives express that someone arranges, forces, allows, or helps an action. "
        "Forms differ after have/get/make/let/help."))

    s.append(table(
        ["Structure", "Meaning", "Example"],
        [
            ["have something done", "arrange a service (often professional)", "We had the office rewired."],
            ["get something done", "similar; often more informal / effortful", "I need to get my laptop repaired."],
            ["have someone do something", "give responsibility / instruct (esp. AmE)", "I'll have Nora review the RFC."],
            ["get someone to do something", "persuade / manage to make someone act", "We got the vendor to extend the SLA."],
            ["make someone do something", "force / compel (bare infinitive)", "The outage made us rethink our SLOs."],
            ["let someone do something", "allow (bare infinitive)", "They let us deploy after hours."],
            ["help someone (to) do", "assist; to is optional", "She helped me (to) write the tests."],
        ],
        caption="Causative and related patterns",
    ))

    s.append(mistakes(
        ("She made me to wait.", "She made me wait."),
        ("They let me to leave.", "They let me leave."),
        ("I had my car to repair.", "I had my car repaired."),
        ("We got them do it.", "We got them to do it."),
    ))

    s.append(compare(
        "<p><em>I had my hair cut</em> = someone cut it for me.<br>"
        "<em>I cut my hair</em> = I did it myself (or ambiguous).<br>"
        "<em>I had him cut my hair</em> = I instructed him to cut it.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_22():
    s = []
    s.append(part_header(22, "Phrasal & Multi-Word Verbs",
        "Multi-word verbs combine a verb with particles/prepositions. Meaning is often idiomatic. "
        "Syntax depends on whether the particle is separable and whether an object is required."))

    s.append(rule(
        "Three common types",
        "Phrasal verbs (verb + adverb particle), prepositional verbs (verb + preposition), "
        "and phrasal-prepositional verbs (verb + particle + preposition).",
        examples_list=[
            "turn off the lights / turn the lights off (phrasal, separable)",
            "look after the servers (prepositional, inseparable)",
            "look forward to the retro / put up with downtime (phrasal-prepositional)",
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Separable vs inseparable & pronoun placement",
        "With separable transitive phrasal verbs, noun objects can go before or after the particle; "
        "pronoun objects must go between verb and particle.",
        examples_list=[
            "Turn off the server. / Turn the server off.",
            "Turn it off. <span class='wrong'>Turn off it.</span>",
            "Look after them. <span class='wrong'>Look them after.</span>",
            "We ran out of disk space.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(table(
        ["Verb", "Type", "Example meaning"],
        [
            ["turn off / on", "separable", "power; also 'cause dislike'"],
            ["give up", "sep/insep patterns", "stop trying; quit a habit"],
            ["look up", "separable", "search for information"],
            ["look after", "prepositional", "take care of"],
            ["look for", "prepositional", "search"],
            ["look forward to", "phr-prep", "anticipate with pleasure (+ gerund)"],
            ["put up with", "phr-prep", "tolerate"],
            ["run out of", "phr-prep", "have none left"],
            ["break down", "intransitive / sep", "stop working; analyse"],
            ["bring up", "separable", "mention; raise a child"],
            ["call off", "separable", "cancel"],
            ["carry out", "separable", "execute (a plan)"],
            ["figure out", "separable", "understand/solve"],
            ["set up", "separable", "arrange/install"],
            ["take off", "intransitive / sep", "leave ground; remove"],
            ["work out", "intransitive / sep", "exercise; calculate; go well"],
        ],
        caption="High-frequency multi-word verbs (sample)",
    ))

    s.append(note(
        "<p>Prefer a single-word formal equivalent in academic writing when tone requires: "
        "<em>investigate</em> (look into), <em>tolerate</em> (put up with), <em>postpone</em> (put off). "
        "In everyday professional English, phrasal verbs are natural and expected.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_23():
    s = []
    s.append(part_header(23, "Word Order",
        "Beyond SVO, English orders adjectives, adverbials, indirect objects, and focused elements in conventional ways. "
        "Advanced order includes fronting, inversion, and clefting (Part 24)."))

    s.append(rule(
        "Objects and indirect objects",
        "V + IO + DO or V + DO + to/for + IO. Pronoun-friendly patterns prefer to/for with two pronouns.",
        examples_list=[
            "Send the client the invoice. / Send the invoice to the client.",
            "Send it to them. (natural)",
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Adverbial order (end position)",
        "A common preference: manner → place → time — but information structure can override.",
        examples_list=[
            "She explained the design clearly in the meeting yesterday.",
            "We met in Cairo last week.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Frequency and mid-position",
        "always, usually, often, sometimes, rarely, never — typically mid-position.",
        examples_list=[
            "She is always online by nine.",
            "We have never lost a backup.",
            "They can usually join remotely.",
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Fronting and emphasis (preview)",
        "Moving an element to the front highlights it: <em>This part I can fix today.</em> "
        "Negative fronting triggers inversion (Parts 17 & 24).",
        levels=["C1", "C2"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_24():
    s = []
    s.append(part_header(24, "Emphasis & Advanced Structures",
        "Clefts, fronting, inversion, emphatic <em>do</em>, substitution, and ellipsis help manage focus and avoid repetition — "
        "especially in C1–C2 writing and speaking."))

    s.append(rule(
        "Cleft sentences (it-clefts)",
        "It + be + highlighted element + relative clause. Used to focus one piece of information.",
        examples_list=[
            "It was Nora who found the race condition.",
            "It was the cache that caused the spike.",
            "It was yesterday that we noticed the drift.",
        ],
        levels=["B2", "C1"],
    ))

    s.append(rule(
        "Pseudo-clefts (wh-clefts)",
        "What-clause + be + focus. Excellent for defining needs and correcting focus.",
        examples_list=[
            "What we need is better observability.",
            "What surprised me was the latency, not the CPU.",
            "What you should do is open a Sev-2.",
        ],
        levels=["B2", "C1"],
    ))

    s.append(rule(
        "Inversion for emphasis",
        "After negative/limiting adverbials and in conditional inversion.",
        examples_list=[
            "Never have we shipped without tests.",
            "Only then did we understand the root cause.",
            "Not until midnight did the alerts stop.",
            "Had we known, we would have scaled up.",
        ],
        levels=["C1", "C2"],
    ))

    s.append(rule(
        "Emphatic do",
        "Use do/does/did + bare infinitive to emphasise affirmation or contrast.",
        examples_list=[
            "I do understand your concern.",
            "She did send the email — check spam.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Substitution and ellipsis",
        "Substitute with <em>so, not, one/ones, do so, that</em>; omit recoverable material in coordination and replies.",
        examples_list=[
            "I think so. / I hope not.",
            "She fixed the bug, and Maya did too.",
            "Want coffee? — I might. (ellipsis)",
            "If you can join, please do.",
        ],
        levels=["B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_25():
    s = []
    s.append(part_header(25, "Discourse & Cohesion",
        "Grammar at paragraph level: how reference, substitution, ellipsis, conjunction, and discourse markers "
        "create coherence across sentences."))

    s.append(rule(
        "Reference",
        "Use pronouns, demonstratives, and the definite article to point back (anaphora) or forward (cataphora) clearly.",
        examples_list=[
            "We tried a blue-green deploy. This reduced downtime.",
            "Here is the plan: we freeze features, then migrate.",
        ],
        levels=["B1", "B2", "C1"],
    ))

    s.append(table(
        ["Relation", "Markers"],
        [
            ["Addition", "also, furthermore, in addition, moreover, besides"],
            ["Contrast", "however, on the other hand, nevertheless, yet, in contrast"],
            ["Cause/result", "therefore, consequently, as a result, so, thus"],
            ["Sequence", "first, then, next, finally, meanwhile, subsequently"],
            ["Example", "for example, for instance, such as, namely"],
            ["Concession", "admittedly, of course, even so, still"],
            ["Rephrasing", "in other words, that is (i.e.), to put it simply"],
            ["Summing up", "overall, in summary, to conclude"],
        ],
        caption="Common discourse markers",
    ))

    s.append(note(
        "<p>In formal writing, connect sentences with markers sparingly and precisely. "
        "Do not start every sentence with <em>However</em> or <em>Moreover</em>. "
        "Coherence also comes from repeating key nouns and keeping topics continuous.</p>"
    ))

    s.append(rule(
        "Paragraph-level grammar",
        "Keep one main idea per paragraph. Use topic sentences. Maintain consistent tense unless time shifts for a reason. "
        "Prefer given → new information order: start with known information, end with new.",
        levels=["B2", "C1", "C2"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_26():
    s = []
    s.append(part_header(26, "Punctuation & Written Grammar",
        "Punctuation encodes grammar: clause boundaries, lists, possession, quotation, and interruption. "
        "This part focuses on grammar-related punctuation choices."))

    s.append(table(
        ["Mark", "Core grammar uses"],
        [
            ["Period / full stop (.)", "End statements; decimals; abbreviations (AmE styles vary)"],
            ["Comma (,)", "lists; compound sentences with coordinating conjunctions; non-defining clauses; introductory adverbials; tag questions"],
            ["Semicolon (;)", "link related independent clauses; complex lists"],
            ["Colon (:)", "introduce explanation, list, quotation after an independent clause"],
            ["Apostrophe (')", "possession; contractions (it's = it is; its = possessive)"],
            ["Quotation marks", "direct speech; titles (style-dependent); scare quotes (careful)"],
            ["Parentheses ( )", "asides; optional material"],
            ["Dashes (— / –)", "emphasis/interruption (em dash); ranges (en dash)"],
            ["Hyphen (-)", "compound adjectives before nouns; some prefixes"],
            ["Ellipsis (…)", "omission; trailing off in dialogue"],
        ],
    ))

    s.append(mistakes(
        ("Its raining.", "It's raining."),
        ("The teams decision", "The team's decision"),
        ("We deployed, then we monitored. (OK)", "Avoid comma splices: <em>We deployed, we monitored.</em> → add and/so or use a semicolon."),
        ("Although it failed, but we continued.", "Although it failed, we continued.", "Do not combine although + but."),
    ))

    s.append(rule(
        "Capitalization (grammar-adjacent)",
        "Capitalise sentence starts, proper nouns, days/months, titles with names, and the pronoun <em>I</em>. "
        "Do not capitalise common nouns for emphasis in standard prose.",
        examples_list=[
            "On Monday, Doctor Hassan joined from Cairo.",
            "She asked, \"Is the API ready?\"",
        ],
        levels=["A2", "B1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def parts_17_to_26():
    return "\n".join([
        part_17(), part_18(), part_19(), part_20(),
        part_21(), part_22(), part_23(), part_24(),
        part_25(), part_26(),
    ])
