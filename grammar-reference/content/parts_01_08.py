"""Parts 1–8: Foundations through Prepositions."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, box
)


def part_01():
    s = []
    s.append(part_header(1, "Grammar Foundations",
        "Before individual rules (tenses, articles, modals), English has a small set of building blocks. "
        "This part defines the pieces of a sentence and how they fit together — the foundation for every later chapter."))

    s.append(h3("What a sentence needs", "p1-sentence"))
    s.append(p(
        "A typical English sentence names something (the <strong>subject</strong>) and says something about it "
        "(the <strong>predicate</strong>). The predicate always contains a <strong>verb</strong>. "
        "Other pieces — objects, complements, adverbials — add meaning."
    ))
    s.append(badge("A1", "A2", "B1"))

    s.append(rule(
        "Subject",
        "The subject is who or what the sentence is about. It usually comes before the verb in statements. "
        "Subjects can be nouns, pronouns, noun phrases, gerunds, or noun clauses.",
        form="Subject + Verb (+ …)",
        when=[
            "To name the doer or experiencer of the action",
            "To name the thing being described (with linking verbs)",
            "In questions, the subject often follows the auxiliary: <em>Are you ready?</em>",
        ],
        examples_list=[
            "<em>The product manager</em> approved the release.",
            "<em>She</em> works remotely twice a week.",
            "<em>Debugging this API</em> takes patience. (gerund phrase as subject)",
            "<em>What they decided</em> surprised the team. (noun clause as subject)",
        ],
        mistakes_list=[
            ("Is raining.", "It is raining.", "English needs a subject; use dummy <em>it</em> for weather."),
            ("In the meeting was discussed the budget.", "The budget was discussed in the meeting.", "Avoid subject-less passive calques."),
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(rule(
        "Verb (finite vs non-finite)",
        "A <strong>finite</strong> verb shows tense and agrees with the subject (<em>works, worked, is working</em>). "
        "A <strong>non-finite</strong> verb does not show tense by itself: infinitives (<em>to work</em>), "
        "gerunds (<em>working</em>), and participles (<em>working / worked</em>). Every complete sentence needs at least one finite verb "
        "(or an imperative, where the subject <em>you</em> is understood).",
        examples_list=[
            "Finite: She <em>reviews</em> pull requests every morning.",
            "Non-finite: She wants <em>to review</em> the PR. / <em>Reviewing</em> code is part of her job.",
        ],
        mistakes_list=[
            ("She to review the code.", "She reviews the code. / She wants to review the code."),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Predicate",
        "The predicate is everything in the clause except the subject — typically the verb plus objects, complements, and adverbials.",
        examples_list=[
            "The engineers <em>deployed the hotfix before midnight</em>.",
            "The standup <em>was unusually short</em>.",
        ],
        levels=["A2", "B1"],
    ))

    s.append(h3("Objects and complements", "p1-objects"))
    s.append(rule(
        "Direct object",
        "A direct object receives the action of a transitive verb. Ask: <em>Verb + what/whom?</em>",
        form="Subject + Transitive Verb + Direct Object",
        examples_list=[
            "We shipped <em>the feature</em>.",
            "Please email <em>the client</em>.",
            "She fixed <em>three bugs</em> before lunch.",
        ],
        levels=["A1", "A2"],
    ))

    s.append(rule(
        "Indirect object",
        "An indirect object is the person/thing that receives the direct object (often the beneficiary).",
        form="S + V + Indirect Object + Direct Object  OR  S + V + Direct Object + to/for + Indirect Object",
        examples_list=[
            "She sent <em>the team</em> <em>a summary</em>.",
            "She sent <em>a summary</em> <em>to the team</em>.",
            "Can you get <em>me</em> <em>the latest build</em>?",
        ],
        compare_html="<p><em>Give him the keys</em> = <em>Give the keys to him</em>. With pronouns, English prefers: <em>Give them to him</em> (not usually <em>Give him them</em> in careful usage).</p>",
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Subject complement",
        "After linking verbs (<em>be, seem, become, feel, look, sound, remain</em>), a subject complement renames or describes the subject. "
        "It is not an object.",
        form="S + Linking Verb + Subject Complement (noun / adjective / phrase)",
        examples_list=[
            "The meeting <em>was productive</em>. (adjective)",
            "Aisha <em>became the tech lead</em>. (noun phrase)",
            "The logs <em>look incomplete</em>.",
        ],
        mistakes_list=[
            ("She is engineer.", "She is an engineer.", "Articles still apply after linking <em>be</em>."),
            ("The solution seems correctly.", "The solution seems correct.", "Use an adjective, not an adverb, after linking verbs."),
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Object complement",
        "An object complement follows the object and completes its meaning — often after verbs like <em>make, call, consider, appoint, find, elect</em>.",
        form="S + V + Object + Object Complement",
        examples_list=[
            "They appointed her <em>engineering manager</em>.",
            "The board found the proposal <em>unrealistic</em>.",
            "We call this pattern <em>dependency injection</em>.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Verb types that shape sentence patterns", "p1-verb-types"))
    s.append(table(
        ["Type", "Needs object?", "Example"],
        [
            ["Transitive", "Yes (direct object)", "She <em>wrote</em> the spec."],
            ["Intransitive", "No", "The server <em>crashed</em>."],
            ["Linking", "Complement (not object)", "The API <em>seems</em> stable."],
            ["Ditransitive", "Indirect + direct object", "He <em>sent</em> us the invoice."],
            ["Complex-transitive", "Object + complement", "They <em>made</em> him lead."],
        ],
        caption="Core verb types and what follows them",
    ))
    s.append(note(
        "<p>Many verbs are both transitive and intransitive: <em>She reads every night</em> / <em>She reads documentation carefully</em>. "
        "Dictionaries mark this; meaning often shifts slightly.</p>"
    ))

    s.append(h3("Clauses and phrases", "p1-clauses"))
    s.append(rule(
        "Phrase vs clause",
        "A <strong>phrase</strong> is a group of words without a finite verb acting as one unit "
        "(noun phrase, prepositional phrase, verb phrase). A <strong>clause</strong> has a subject–predicate structure "
        "(at least in full clauses).",
        examples_list=[
            "Phrase: <em>after the sprint review</em>",
            "Clause: <em>after we finished the sprint review</em>",
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Independent (main) clause",
        "An independent clause can stand alone as a sentence. It has a subject and a finite verb and expresses a complete idea.",
        examples_list=[
            "The deploy succeeded.",
            "We postponed the launch, <em>and the marketing team updated the landing page</em>.",
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Dependent (subordinate) clause",
        "A dependent clause cannot stand alone. It needs a main clause. Common types: noun clauses, relative (adjective) clauses, adverb clauses.",
        examples_list=[
            "If the tests fail, we roll back. (<em>If the tests fail</em> = dependent)",
            "The engineer who wrote the migration is on leave.",
            "I know that the deadline is Friday.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Auxiliary vs main verbs", "p1-aux"))
    s.append(p(
        "<strong>Main verbs</strong> carry the core meaning (<em>ship, decide, need</em>). "
        "<strong>Auxiliary (helping) verbs</strong> build tense, aspect, voice, modality, and questions/negatives: "
        "<em>be, have, do</em> and the modals (<em>can, will, must…</em>)."
    ))
    s.append(examples(
        "She <em>is reviewing</em> the PR. (<em>is</em> = auxiliary; <em>reviewing</em> = main)",
        "They <em>have finished</em> the migration.",
        "<em>Do</em> you <em>agree</em> with the estimate?",
        "We <em>can ship</em> tomorrow.",
    ))

    s.append(h3("Basic English sentence patterns", "p1-patterns"))
    s.append(p("English relies heavily on word order. Master these five patterns; most sentences are variations of them."))
    s.append(table(
        ["Pattern", "Structure", "Example"],
        [
            ["1", "S + V", "Servers restart."],
            ["2", "S + V + O", "We restarted the servers."],
            ["3", "S + V + C", "The outage was serious."],
            ["4", "S + V + IO + DO", "She sent the client a timeline."],
            ["5", "S + V + O + C", "They elected Nora chair."],
        ],
        caption="Five core clause patterns",
    ))
    s.append(rule(
        "Basic word order in statements",
        "Default English word order is Subject–Verb–Object (SVO). Adverbials of place/time often come at the end; "
        "frequency adverbs often take mid-position (see Part 7 and Part 23).",
        form="Subject + (auxiliary) + Verb + Object + (place) + (time)",
        examples_list=[
            "The team shipped the patch yesterday.",
            "She often joins standups from Cairo.",
        ],
        mistakes_list=[
            ("Yesterday shipped the team the patch.", "The team shipped the patch yesterday."),
            ("She joins often standups.", "She often joins standups."),
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(warning(
        "<p>Do not drop the subject in full sentences (common when translating from pro-drop languages): "
        "<span class='wrong'>Works from home</span> → <span class='correct'>She works from home</span>.</p>"
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_02():
    s = []
    s.append(part_header(2, "Nouns",
        "Nouns name people, places, things, ideas, and events. English noun grammar hinges on countability, "
        "articles, plurals, and how nouns combine into complex noun phrases."))

    s.append(h3("Types of nouns", "p2-types"))
    s.append(table(
        ["Type", "Meaning", "Examples"],
        [
            ["Common", "General class", "engineer, city, meeting"],
            ["Proper", "Specific name (usually capitalised)", "Sara, Cairo, GitHub, Monday"],
            ["Concrete", "Perceivable with senses", "laptop, coffee, office"],
            ["Abstract", "Idea/quality/state", "reliability, freedom, progress"],
            ["Collective", "Group as one unit", "team, staff, committee, audience"],
            ["Compound", "Two+ words forming one noun", "deadline, pull request, whiteboard"],
        ],
    ))

    s.append(rule(
        "Countable vs uncountable",
        "Countable nouns can be singular or plural and take <em>a/an</em> and numbers. "
        "Uncountable nouns are not normally pluralised and do not take <em>a/an</em>. "
        "They take singular verbs and quantifiers like <em>some, much, a little, a piece of</em>.",
        examples_list=[
            "Countable: a ticket / two tickets; a bug / several bugs",
            "Uncountable: information, advice, software, feedback, progress, luggage, furniture",
            "We need <em>more information</em>. (not <em>informations</em>)",
            "She gave me <em>some useful advice</em>. (not <em>an advice</em>)",
        ],
        mistakes_list=[
            ("an information", "some information / a piece of information"),
            ("many softwares", "a lot of software / several software products"),
            ("homeworks", "homework / three homework assignments"),
            ("a feedback", "some feedback / a piece of feedback"),
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(h3("Nouns that change meaning with countability", "p2-dual"))
    s.append(table(
        ["Uncountable (general)", "Countable (specific/instance)"],
        [
            ["paper (material)", "a paper (newspaper/academic article)"],
            ["glass (material)", "a glass (container)"],
            ["experience (knowledge)", "an experience (event)"],
            ["time (uncountable duration)", "a time / times (occasion)"],
            ["business (activity)", "a business (company)"],
            ["work (activity)", "a work (artwork); works (factory)"],
            ["light (illumination)", "a light (lamp)"],
            ["room (space)", "a room (chamber)"],
            ["iron (metal)", "an iron (appliance)"],
            ["coffee (substance)", "a coffee (a serving)"],
        ],
        caption="Same word, different grammar and meaning",
    ))
    s.append(examples(
        "She has a lot of <em>experience</em> with distributed systems.",
        "Working at that startup was a great <em>experience</em>.",
        "Do we have enough <em>time</em>?",
        "There was a <em>time</em> when releases were monthly.",
    ))

    s.append(h3("Plurals", "p2-plurals"))
    s.append(rule(
        "Regular plurals",
        "Most nouns add <em>-s</em> or <em>-es</em>. Spelling rules: consonant+y → ies (<em>company → companies</em>); "
        "o often → es (<em>potato → potatoes</em>) but not always (<em>photo → photos</em>); "
        "f/fe often → ves (<em>life → lives</em>) with exceptions (<em>belief → beliefs</em>).",
        levels=["A1", "A2"],
    ))
    s.append(table(
        ["Singular", "Plural", "Note"],
        [
            ["child", "children", "irregular"],
            ["person", "people (persons = legal/formal)", "people is usual"],
            ["man / woman", "men / women", "irregular"],
            ["foot / tooth", "feet / teeth", "irregular"],
            ["mouse", "mice", "computers: often <em>mouses</em> for devices"],
            ["analysis", "analyses", "Greek/Latin"],
            ["criterion", "criteria", "criterion is singular"],
            ["datum", "data", "data often uncountable/singular in modern use"],
            ["focus", "foci / focuses", "both used"],
            ["index", "indexes / indices", "indexes common in tech"],
            ["formula", "formulas / formulae", "formulas common"],
            ["sheep / deer / fish", "sheep / deer / fish (fishes = types)", "zero plural"],
            ["series / species", "series / species", "same form"],
        ],
        caption="High-value irregular and special plurals",
    ))

    s.append(rule(
        "Collective nouns",
        "Collective nouns name a group. In American English they usually take a singular verb when the group acts as one unit "
        "(<em>The team is ready</em>). British English often allows plural (<em>The team are arguing</em>) when members act individually.",
        examples_list=[
            "The committee <em>has</em> approved the budget. (AmE / unit)",
            "The staff <em>are</em> working from different time zones. (BrE / individuals)",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Possession", "p2-possessive"))
    s.append(rule(
        "Possessive 's and of-phrases",
        "Use <em>'s</em> especially with people, animals, time expressions, and organisations. "
        "Use <em>of</em> with things, long noun phrases, and many abstract relationships.",
        form="noun + 's + noun  ·  of + noun phrase",
        examples_list=[
            "the company's roadmap / the roadmap of the company",
            "yesterday's meeting / a week's notice",
            "the colour of the button (not usually <em>the button's colour</em> in formal writing, though both occur)",
            "the CEO's decision",
        ],
        when=[
            "Singular nouns: <em>engineer → engineer's</em>",
            "Plural ending in s: <em>engineers → engineers'</em>",
            "Irregular plural: <em>children's</em>, <em>people's</em>",
            "Names ending in s: <em>James's</em> or <em>James'</em> (style choice; be consistent)",
        ],
        levels=["A2", "B1"],
    ))
    s.append(rule(
        "Double possessive",
        "English allows <em>a friend of mine / a colleague of Sara's</em> — combining <em>of</em> with a possessive. "
        "It often means 'one among several' and sounds natural with indefinite determiners.",
        examples_list=[
            "A friend of mine recommended this library.",
            "That idea of Nora's actually solved the bottleneck.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Noun modifiers and complex noun phrases", "p2-np"))
    s.append(p(
        "English often stacks nouns as modifiers: <em>user authentication flow</em>, <em>production database migration plan</em>. "
        "The last noun is the head; earlier nouns modify it. Do not pluralise modifiers unless the plural meaning is required "
        "(<em>a systems engineer</em> vs <em>a system engineer</em> — both exist; check collocation)."
    ))
    s.append(examples(
        "customer support ticket",
        "end-to-end encryption key",
        "quarterly performance review",
    ))
    s.append(rule(
        "Nominalization",
        "Nominalization turns verbs/adjectives into nouns (<em>decide → decision, reliable → reliability</em>). "
        "Useful in formal writing, but overuse makes prose heavy. Prefer verbs when clarity matters.",
        examples_list=[
            "We decided to delay the launch. (clearer)",
            "The decision to delay the launch was announced yesterday. (more formal/noun-heavy)",
        ],
        levels=["B2", "C1"],
    ))

    s.append(note(
        "<p><strong>Normally uncountable (learn these):</strong> advice, information, news, furniture, luggage/baggage, "
        "equipment, software, homework, knowledge, progress, research, evidence, traffic, weather, accommodation (BrE often uncountable).</p>"
        "<p>Use partitives: <em>a piece of advice, an item of news, two pieces of luggage, a research paper</em>.</p>"
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_03():
    s = []
    s.append(part_header(3, "Pronouns",
        "Pronouns replace noun phrases to avoid repetition. Accuracy depends on case (subject/object), agreement, "
        "clear reference, and register (especially with generic <em>they</em> and formal alternatives)."))

    s.append(h3("Personal pronouns: case", "p3-personal"))
    s.append(table(
        ["Subject", "Object", "Possessive adj.", "Possessive pronoun", "Reflexive"],
        [
            ["I", "me", "my", "mine", "myself"],
            ["you", "you", "your", "yours", "yourself / yourselves"],
            ["he", "him", "his", "his", "himself"],
            ["she", "her", "her", "hers", "herself"],
            ["it", "it", "its", "—", "itself"],
            ["we", "us", "our", "ours", "ourselves"],
            ["they", "them", "their", "theirs", "themselves"],
        ],
        caption="Personal pronoun paradigm",
    ))
    s.append(mistakes(
        ("Me and Sara fixed the bug.", "Sara and I fixed the bug.", "Subject position needs subject pronouns; polite order puts yourself last."),
        ("Between you and I…", "Between you and me…", "After prepositions, use object pronouns."),
        ("Its' colour", "Its colour", "<em>its</em> = possessive; <em>it's</em> = it is / it has."),
        ("They enjoyed theirselves.", "They enjoyed themselves."),
    ))

    s.append(rule(
        "Possessive adjectives vs possessive pronouns",
        "Possessive adjectives (<em>my, your, their</em>) come before a noun. "
        "Possessive pronouns (<em>mine, yours, theirs</em>) stand alone and replace a noun phrase.",
        examples_list=[
            "This is <em>my</em> laptop. This laptop is <em>mine</em>.",
            "Is this seat <em>yours</em>?",
        ],
        levels=["A1", "A2"],
    ))

    s.append(rule(
        "Reflexive pronouns",
        "Use reflexives when the object refers to the same entity as the subject, or for emphasis (<em>I myself…</em>). "
        "Do not use them as a substitute for subject/object pronouns in coordination.",
        examples_list=[
            "She taught herself TypeScript.",
            "Please help yourself to coffee.",
            "I fixed it myself. (emphasis)",
        ],
        mistakes_list=[
            ("Please contact myself.", "Please contact me."),
            ("If you have questions, ask John or myself.", "…ask John or me."),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Reciprocal pronouns",
        "<em>Each other</em> and <em>one another</em> express mutual action. In modern usage they are largely interchangeable; "
        "some writers prefer <em>one another</em> for more than two, but this is not a hard rule.",
        examples_list=[
            "The two services call each other every few seconds.",
            "Team members trust one another.",
        ],
        levels=["B1"],
    ))

    s.append(h3("Demonstratives, indefinites, interrogatives", "p3-other"))
    s.append(rule(
        "Demonstrative pronouns",
        "<em>This/these</em> (near), <em>that/those</em> (far) can be determiners or pronouns.",
        examples_list=[
            "This is the latest build. Those were outdated screenshots.",
            "I prefer this approach to that.",
        ],
        levels=["A1", "A2"],
    ))

    s.append(rule(
        "Indefinite pronouns",
        "Words like <em>someone, anybody, nothing, everything, each, either, neither, both, few, many, one</em> "
        "refer to non-specific people/things. Most compounds with <em>every-/some-/any-/no-</em> take singular verbs.",
        examples_list=[
            "Everyone is online. (singular verb)",
            "Nothing was broken in production.",
            "Someone left their laptop. (singular <em>they</em> — natural modern English)",
        ],
        mistakes_list=[
            ("Everyone are ready.", "Everyone is ready."),
            ("I don't know nothing.", "I don't know anything. / I know nothing."),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "One / ones",
        "<em>One/ones</em> substitute for countable nouns to avoid repetition.",
        examples_list=[
            "Which ticket do you mean — the urgent one?",
            "We need smaller monitors; these ones are too large.",
        ],
        levels=["A2", "B1"],
    ))

    s.append(h3("Dummy it and existential there", "p3-dummy"))
    s.append(rule(
        "Dummy it",
        "English uses <em>it</em> as an empty subject for weather, time, distance, and extraposed clauses.",
        examples_list=[
            "It is raining in London.",
            "It is 3 p.m. in Cairo.",
            "It is important to document the API.",
            "It seems that the cache is stale.",
        ],
        levels=["A1", "A2", "B1"],
    ))
    s.append(rule(
        "Existential there",
        "<em>There is/are</em> introduces existence or presence. Agreement usually follows the real noun phrase "
        "(though spoken English often uses <em>there's</em> + plural).",
        examples_list=[
            "There is a bug in the payment flow.",
            "There are three open issues.",
            "<span class='register'>SPOKEN</span> There's two problems… (common; write <em>There are</em> in formal prose)",
        ],
        levels=["A1", "A2"],
    ))

    s.append(h3("Relative and interrogative pronouns", "p3-rel"))
    s.append(p("See Part 16 (Questions) and Part 18 (Relative clauses) for full systems. Core forms:"))
    s.append(table(
        ["Pronoun", "Typical use"],
        [
            ["who / whom", "people (whom = object; formal)"],
            ["whose", "possession"],
            ["which", "things; non-defining clauses"],
            ["that", "defining clauses (people/things); not after comma"],
            ["what", "the thing that / interrogative"],
        ],
    ))

    s.append(h3("Pronoun reference and agreement", "p3-ref"))
    s.append(warning(
        "<p>A pronoun must point clearly to an antecedent. Ambiguity is a C1 writing error:</p>"
        "<p><span class='wrong'>When Maya told Hana the news, she was shocked.</span> (Who was shocked?)</p>"
        "<p><span class='correct'>When Maya told Hana the news, Hana was shocked.</span></p>"
    ))
    s.append(advanced(
        "<p><strong>Generic pronouns:</strong> Older formal style used <em>he</em> generically; modern standard English uses "
        "singular <em>they</em>, or rephrases with plurals (<em>users… they</em>). "
        "<em>He or she</em> is possible but often clumsy.</p>"
        "<p><span class='register'>FORMAL</span> One should save one's work frequently. "
        "(academic/old-fashioned in AmE; more natural in BrE formal writing)</p>"
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_04():
    s = []
    s.append(part_header(4, "Determiners",
        "Determiners come at the start of a noun phrase and specify reference and quantity "
        "(articles, demonstratives, possessives, quantifiers, numbers, distributives). "
        "English allows a limited, ordered stack of determiners."))

    s.append(h3("What counts as a determiner", "p4-what"))
    s.append(table(
        ["Category", "Examples"],
        [
            ["Articles", "a, an, the"],
            ["Demonstratives", "this, that, these, those"],
            ["Possessives", "my, your, his, her, its, our, their, whose"],
            ["Quantifiers", "some, any, no, much, many, few, little, enough, several, a lot of"],
            ["Numbers", "one, two, first, second…"],
            ["Distributives", "each, every, either, neither"],
            ["Interrogatives", "which, what, whose"],
        ],
    ))

    s.append(rule(
        "Determiner order (pre-, central, post-)",
        "English noun phrases allow: <strong>predeterminers</strong> → <strong>central determiners</strong> → "
        "<strong>postdeterminers</strong> → adjectives → noun.",
        form="all/both/half/double/such/what/quite/rather → article/demonstrative/possessive → numbers/many/few/other → Adj → Noun",
        examples_list=[
            "all the new tickets",
            "both these approaches",
            "half my salary",
            "twice the cost",
            "such a difficult bug",
            "what a mess",
            "the first two sprints",
            "my many unanswered emails",
        ],
        mistakes_list=[
            ("the all tickets", "all the tickets"),
            ("my this laptop", "this laptop of mine / this laptop"),
            ("these my colleagues", "these colleagues of mine / my colleagues"),
        ],
        levels=["B1", "B2", "C1"],
    ))

    s.append(h3("Predeterminers in detail", "p4-pre"))
    s.append(rule(
        "all / both / half",
        "These can appear before determiners or before pronouns (<em>all of them</em>). "
        "<em>Both</em> is for exactly two.",
        examples_list=[
            "All (of) the tests passed.",
            "Both (of) the designs look clean.",
            "Half (of) the budget is gone.",
            "All of us agreed. / We all agreed.",
        ],
        levels=["A2", "B1"],
    ))
    s.append(rule(
        "such / what (exclamative) / rather / quite",
        "<em>Such</em> and exclamative <em>what</em> often need <em>a/an</em> with singular count nouns. "
        "<em>Quite/rather a</em> + adjective + noun is common in BrE.",
        examples_list=[
            "It was such a clear explanation.",
            "What a useful library!",
            "It was rather a long meeting. <span class='register'>BrE</span>",
            "She's quite a skilled negotiator.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(h3("Quantifiers and agreement", "p4-quant"))
    s.append(table(
        ["With uncountable", "With plural countable", "Notes"],
        [
            ["much, little, a little, a great deal of", "many, few, a few, several", "much/many common in negatives/questions; a lot of in affirmatives"],
            ["a large amount of", "a large number of", "formal alternatives"],
            ["less (increasingly also with plurals)", "fewer (careful usage)", "See Part 19; less is common with plurals in speech"],
        ],
    ))
    s.append(examples(
        "There isn't much time left.",
        "We don't have many open seats.",
        "A few engineers stayed late. (some, positive)",
        "Few engineers stayed late. (almost none — negative tone)",
        "A little patience helps. / Little patience was shown.",
    ))

    s.append(rule(
        "each / every / either / neither",
        "<em>Each</em> and <em>every</em> take singular nouns and usually singular verbs. "
        "<em>Either/neither</em> refer to two options.",
        examples_list=[
            "Each developer owns a service.",
            "Every ticket needs an owner.",
            "Either solution works. / Neither option is ideal.",
        ],
        compare_html="<p><em>Each</em> emphasises individuals; <em>every</em> emphasises the whole group as a set. "
                     "Often interchangeable: <em>each/every day</em>.</p>",
        levels=["A2", "B1"],
    ))

    s.append(note("<p>Articles are determiners too — see Part 5 for the complete article system.</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_05():
    s = []
    s.append(part_header(5, "Articles",
        "English has three article choices: <em>a/an</em> (indefinite), <em>the</em> (definite), and the zero article. "
        "Articles encode whether a noun is known, unique, generic, or newly introduced. This is one of the hardest systems for learners."))

    s.append(h3("A / An — indefinite article", "p5-a"))
    s.append(rule(
        "Form of a / an",
        "Use <em>a</em> before consonant sounds and <em>an</em> before vowel sounds — based on pronunciation, not spelling.",
        examples_list=[
            "a user, a university, a European office (consonant /j/ sound)",
            "an hour, an honour, an MBA, an HTTP header (vowel sound)",
            "an API / a REST API (depends on how you pronounce the initialism)",
        ],
        levels=["A1", "A2"],
    ))
    s.append(rule(
        "Main uses of a/an",
        "Introduce a singular countable noun when it is not uniquely identified for the listener.",
        when=[
            "First mention: <em>I found a bug in checkout.</em>",
            "Jobs and roles: <em>She is a product designer.</em>",
            "Classifications: <em>A whale is a mammal.</em> (also with <em>the</em> for species — see below)",
            "Frequency: <em>twice a week, 80 kilometres an hour</em>",
            "Rates: <em>$50 a ticket</em>",
            "Exclamations: <em>What a day!</em>",
        ],
        examples_list=[
            "We need a staging environment.",
            "He works as an SRE.",
            "They meet three times a month.",
        ],
        mistakes_list=[
            ("She is engineer.", "She is an engineer."),
            ("I have a information.", "I have some information."),
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(h3("The — definite article", "p5-the"))
    s.append(rule(
        "Core meaning of the",
        "Use <em>the</em> when the listener can identify the referent — because it was mentioned, is unique, "
        "is shared knowledge, or is defined by a modifier.",
        when=[
            "Second mention: <em>I found a bug… The bug blocked payments.</em>",
            "Unique in context: <em>Please close the door.</em>",
            "Shared knowledge: <em>the sun, the internet, the CEO</em> (of our company)",
            "Superlatives and ordinals: <em>the best option, the first release</em>",
            "Defining modifiers: <em>the engineer who wrote the migration</em>",
        ],
        levels=["A1", "A2", "B1"],
    ))
    s.append(h3("The with special noun groups", "p5-the-special"))
    s.append(table(
        ["Category", "Usually with the", "Usually without the"],
        [
            ["Geographical", "rivers, seas, oceans, deserts, island groups, mountain ranges: the Nile, the Alps", "most countries, cities, lakes, single mountains: France, Cairo, Lake Victoria, Mount Fuji"],
            ["Exceptions (countries)", "the UK, the UAE, the Netherlands, the United States", "Egypt, Japan, Brazil"],
            ["Institutions (as buildings)", "the bank, the hospital (esp. AmE often without — see zero)", "at school/university/church (primary purpose — BrE patterns)"],
            ["Newspapers", "The Guardian, The New York Times", "many magazines vary"],
            ["Musical instruments", "play the piano / the guitar", "—"],
            ["Species / inventions", "the wolf is endangered; who invented the telephone?", "Wolves are endangered (generic plural)"],
            ["Body parts (with verbs like hit/touch)", "He hit me on the arm.", "my arm (possessive also common)"],
        ],
    ))
    s.append(examples(
        "She plays the oud and the piano.",
        "The smartphone changed consumer behaviour.",
        "We crossed the Atlantic last year.",
    ))

    s.append(h3("Zero article", "p5-zero"))
    s.append(rule(
        "When English uses no article",
        "Zero article is common with plural and uncountable nouns in a general sense, and with many institutional/transport/meal patterns.",
        when=[
            "Plural generics: <em>Engineers need clear requirements.</em>",
            "Uncountable generics: <em>Software evolves quickly.</em>",
            "Abstract concepts: <em>Trust matters in remote teams.</em>",
            "Languages & subjects: <em>She studies Arabic and computer science.</em>",
            "Sports & games: <em>They play football.</em>",
            "Meals (general): <em>after lunch</em> (but <em>the lunch we had with the client</em>)",
            "Transport (by): <em>by train, by bus, by email</em>",
            "Titles with names: <em>Doctor Hassan, President Lee</em> (but <em>the doctor</em> as role)",
            "Home/work/bed patterns: <em>at home, at work, in bed</em>",
        ],
        examples_list=[
            "Privacy is a product requirement.",
            "She goes to school by metro.",
            "Dinner is at eight.",
        ],
        mistakes_list=[
            ("The life is complicated.", "Life is complicated."),
            ["She went to the home.", "She went home."],
            ("I like the music.", "I like music.", "Unless a specific set of music is meant."),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(advanced(
        "<p><strong>Institutions:</strong> <em>in hospital</em> (BrE, as patient) vs <em>in the hospital</em> (AmE or visiting the building). "
        "<em>at university</em> (BrE) vs <em>in college</em> (AmE patterns). Learn collocations; do not overgeneralise.</p>"
        "<p><strong>Geographic the:</strong> <em>the Sudan, the Gambia, the Congo</em> appear in some styles; "
        "modern usage often drops <em>the</em> for country names except established forms (the Netherlands, the United States).</p>"
    ))

    s.append(compare(
        "<p><em>A product manager needs empathy.</em> (any / role classification)<br>"
        "<em>The product manager needs empathy.</em> (our known PM / the role as defined in context)<br>"
        "<em>Product managers need empathy.</em> (generic plural — very natural)</p>"
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_06():
    s = []
    s.append(part_header(6, "Adjectives",
        "Adjectives describe nouns and pronouns. Key issues: position (attributive vs predicative), order before nouns, "
        "gradability, adjective–preposition patterns, and comparison (see also Part 19)."))

    s.append(rule(
        "Attributive vs predicative",
        "Attributive adjectives appear before a noun (<em>a critical bug</em>). "
        "Predicative adjectives appear after linking verbs (<em>The bug is critical</em>). "
        "Some adjectives are mainly one or the other: <em>the main reason</em> (not usually <em>the reason is main</em>); "
        "<em>she is asleep</em> (not <em>an asleep engineer</em>).",
        examples_list=[
            "a reliable service / The service is reliable.",
            "the only solution / This is the only solution.",
            "The baby is awake. (not <em>an awake baby</em> in careful style — prefer <em>a baby who is awake</em>)",
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Adjective order",
        "When several adjectives appear before a noun, English prefers a conventional order. Treat this as a strong tendency, not an absolute law.",
        form="opinion → size → age → shape → colour → origin → material → purpose + NOUN",
        examples_list=[
            "a useful small new square blue Korean metal mounting bracket",
            "a reliable old production server",
            "an innovative young Egyptian software engineer",
        ],
        levels=["B1", "B2"],
    ))
    # Fix - rule() doesn't have note_html - I passed it incorrectly. Let me check - I have note_html="" in the call which would error.
    # Actually looking at my rule() signature, there's no note_html parameter. I need to fix this - I'll remove it by rewriting that section in a fix later, or fix now.

    s.append(note(
        "<p>Native speakers rarely stack more than two or three adjectives. Prefer <em>a small, reliable production server</em>.</p>"
    ))

    s.append(rule(
        "Gradable vs non-gradable / extreme adjectives",
        "Gradable adjectives allow degree (<em>very useful, slightly late</em>). "
        "Non-gradable and extreme adjectives (<em>unique, perfect, freezing, exhausted, enormous</em>) "
        "usually take intensifiers like <em>absolutely, completely, totally</em>, not <em>very</em>.",
        examples_list=[
            "very important / extremely important",
            "absolutely essential (not usually <em>very essential</em>)",
            "completely finished / totally wrong",
        ],
        levels=["B1", "B2"],
    ))

    s.append(table(
        ["Modifier", "Typical with", "Tone"],
        [
            ["very / really", "gradable", "neutral / spoken"],
            ["extremely", "gradable", "strong"],
            ["absolutely / completely / totally / utterly", "non-gradable / extreme", "strong"],
            ["quite", "gradable = fairly (BrE); AmE often = very", "varies by variety"],
            ["rather", "gradable; often unexpected/negative", "BrE common"],
            ["fairly / pretty", "gradable", "pretty = informal"],
        ],
        caption="Degree modifiers",
    ))

    s.append(rule(
        "Compound and participial adjectives",
        "Hyphenate compound adjectives before nouns: <em>a well-known library, a full-time role, a user-friendly UI</em>. "
        "Participial adjectives: <em>interesting / interested, boring / bored, tiring / tired</em> — "
        "<em>-ing</em> often describes the cause; <em>-ed</em> the experiencer.",
        examples_list=[
            "The meeting was boring. I was bored.",
            "a long-term roadmap; an open-source project",
        ],
        mistakes_list=[
            ("I am interesting in Kubernetes.", "I am interested in Kubernetes."),
            ("a well known library", "a well-known library", "Hyphenate before the noun."),
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Adjective + preposition",
        "Many adjectives require a specific preposition. Learn them as chunks.",
        examples_list=[
            "good at testing; responsible for releases; interested in AI; aware of the risk",
            "similar to ours; different from/to/than (AmE often <em>than</em>); keen on; capable of",
            "famous for; proud of; afraid of; used to (accustomed to)",
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Comparative and superlative adjectives (preview)",
        "Short adjectives: <em>-er / -est</em>. Long adjectives: <em>more / most</em>. Irregular: <em>good–better–best, bad–worse–worst, far–farther/further</em>. "
        "Full comparison system: Part 19.",
        examples_list=[
            "faster than the previous build; the most stable release this year",
        ],
        levels=["A2", "B1"],
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_07():
    s = []
    s.append(part_header(7, "Adverbs",
        "Adverbs modify verbs, adjectives, other adverbs, or whole clauses. Position and form cause many learner errors, "
        "especially lookalike pairs (<em>hard/hardly</em>)."))

    s.append(h3("Semantic types", "p7-types"))
    s.append(table(
        ["Type", "Question / role", "Examples"],
        [
            ["Manner", "How?", "carefully, well, fast, clearly"],
            ["Place", "Where?", "here, there, upstairs, abroad"],
            ["Time", "When?", "now, yesterday, recently, soon"],
            ["Frequency", "How often?", "always, often, rarely, never"],
            ["Degree", "How much?", "very, almost, too, enough"],
            ["Focusing", "Highlight", "only, even, also, mainly, just"],
            ["Viewpoint / stance", "Attitude", "frankly, clearly, hopefully, apparently"],
            ["Linking", "Relation", "however, therefore, meanwhile, still"],
        ],
    ))

    s.append(rule(
        "Adverb positions",
        "English allows front, mid, and end positions. Mid-position is typical for frequency and many focusing adverbs: "
        "after <em>be</em>, before main verbs, after the first auxiliary.",
        form="Front: Suddenly, the server stopped.<br>Mid: She has always preferred typed languages.<br>End: She explained the design clearly.",
        examples_list=[
            "We usually deploy on Thursdays.",
            "She is never late to standups.",
            "They can also join remotely.",
        ],
        mistakes_list=[
            ("She comes often late.", "She often comes late. / She comes late often."),
            ("He speaks English very good.", "He speaks English very well."),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(h3("Adjective vs adverb confusion", "p7-adj-adv"))
    s.append(examples(
        "She is a <em>quick</em> learner. (adjective)",
        "She learns <em>quickly</em>. (adverb)",
        "I feel <em>bad</em> about the outage. (adjective after linking verb — natural)",
        "<span class='register'>INFORMAL</span> I feel badly… (often criticised when meaning ‘sorry’)",
    ))

    s.append(h3("Lookalike pairs", "p7-pairs"))
    s.append(table(
        ["Form", "Meaning", "Example"],
        [
            ["hard", "with effort; with force", "She works hard."],
            ["hardly", "almost not", "She hardly sleeps before releases."],
            ["late", "after expected time", "The train arrived late."],
            ["lately", "recently", "Have you seen him lately?"],
            ["near", "close (also preposition/adj)", "Keep the backup near."],
            ["nearly", "almost", "We nearly missed the deadline."],
            ["high", "to a great height / level", "aim high; prices are high"],
            ["highly", "very (opinion)", "highly recommended"],
            ["free", "without payment / not trapped", "enter free; walk free"],
            ["freely", "without restriction", "speak freely"],
            ["wide", "fully (eyes/doors)", "wide awake; open wide"],
            ["widely", "by many people", "widely used"],
            ["deep", "to a great depth", "dig deep"],
            ["deeply", "strongly (emotion)", "deeply concerned"],
        ],
        caption="Adverbs that look like adjectives but differ in meaning",
    ))

    s.append(warning(
        "<p><span class='wrong'>I hardly work</span> means you almost do not work — the opposite of "
        "<span class='correct'>I work hard</span>.</p>"
    ))

    s.append(rule(
        "Sentence adverbs and linking adverbs",
        "Stance adverbs comment on the whole clause: <em>Fortunately, the rollback worked.</em> "
        "Linking adverbs connect ideas across sentences: <em>However, the root cause remains unclear.</em> "
        "In formal writing, avoid overusing <em>However</em> as a conjunction inside a comma splice — use a semicolon or new sentence.",
        examples_list=[
            "Clearly, we need better monitoring.",
            "The feature shipped on time; however, adoption was slow.",
        ],
        levels=["B1", "B2", "C1"],
    ))

    s.append(part_footer())
    return "\n".join(s)


def part_08():
    s = []
    s.append(part_header(8, "Prepositions",
        "Prepositions express relations of time, place, movement, cause, means, and abstract relationships. "
        "They are highly collocational — learn verb/adjective/noun + preposition chunks, not only translation equivalents."))

    s.append(h3("in / on / at — the core system", "p8-inoutat"))
    s.append(table(
        ["", "Time", "Place"],
        [
            ["at", "clock times; at night; at the weekend (BrE); at the moment", "points: at the door, at the airport, at the desk"],
            ["on", "days & dates: on Monday, on 5 May; on weekends (AmE)", "surfaces: on the table, on the screen, on the wall"],
            ["in", "months, years, seasons, parts of day: in July, in 2026, in the morning", "containers/areas: in the room, in Cairo, in the file"],
        ],
        caption="in / on / at — start here",
    ))
    s.append(mistakes(
        ("in Monday", "on Monday"),
        ("at July", "in July"),
        ("in the night", "at night", "But: in the night = during a particular night"),
        ("on the airport", "at the airport"),
    ))

    s.append(h3("Movement and direction", "p8-move"))
    s.append(table(
        ["Preposition", "Idea", "Example"],
        [
            ["to", "destination", "go to the office"],
            ["into", "movement inside", "walk into the meeting room"],
            ["onto", "movement onto a surface", "put the phone onto the charger"],
            ["from", "source", "from Cairo to Berlin"],
            ["towards / toward", "direction (not necessarily arrival)", "walk towards the exit"],
            ["through", "from one side to another", "through the tunnel / through the docs"],
            ["across", "from one side to the other (surface)", "across the street"],
            ["along", "following a line", "along the corridor"],
            ["over / under", "above/below path", "over the bridge"],
            ["up / down", "ascent/descent", "scroll down the page"],
        ],
    ))
    s.append(compare(
        "<p><em>in the room</em> (location) vs <em>into the room</em> (entering).<br>"
        "<em>on the platform</em> vs <em>onto the platform</em>.</p>"
    ))

    s.append(h3("Time prepositions beyond in/on/at", "p8-time"))
    s.append(rule(
        "for / since / during / while / by / until",
        "These mark duration, starting points, periods, and deadlines — and are frequently confused.",
        examples_list=[
            "<em>for</em> + duration: for three hours / for two years",
            "<em>since</em> + starting point: since 2021 / since Monday / since we migrated",
            "<em>during</em> + noun: during the meeting",
            "<em>while</em> + clause: while we were deploying",
            "<em>by</em> = not later than: by Friday",
            "<em>until / till</em> = up to a point: until Friday",
        ],
        mistakes_list=[
            ("I work here since three years.", "I have worked here for three years. / since 2023."),
            ("during I was coding", "while I was coding / during the coding session"),
            ("until Friday means the same as by Friday", "No: <em>by Friday</em> = deadline; <em>until Friday</em> = continuing up to Friday"),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(h3("Relationship, cause, contrast", "p8-rel"))
    s.append(table(
        ["Pair", "Difference"],
        [
            ["between / among", "between: usually two (or clear individual relationships); among: group/mass"],
            ["beside / besides", "beside = next to; besides = in addition to"],
            ["like / as", "like = similar to (preposition); as = in the role of / in the way that (conjunction/preposition)"],
            ["because of / due to / owing to", "because of + noun (safe); due to traditionally after be; owing to = formal"],
            ["despite / in spite of", "same meaning + noun/gerund; not + clause (use although)"],
            ["according to", "+ source: according to the docs (not <em>according to me</em> — say <em>in my opinion</em>)"],
        ],
    ))
    s.append(examples(
        "The difference between staging and production…",
        "Among all the options, this one scales best.",
        "Sit beside Nora. Besides the bugfix, we need tests.",
        "She works as a consultant. She works like a machine. (simile)",
        "Despite the outage, revenue held steady.",
        "According to the postmortem, the timeout was too aggressive.",
    ))

    s.append(h3("Dependent prepositions", "p8-dep"))
    s.append(p("Prepositions are selected by verbs, adjectives, and nouns. A sample of high-frequency patterns:"))
    s.append(table(
        ["Pattern", "Examples"],
        [
            ["Verb + preposition", "depend on, rely on, look for, look after, deal with, consist of, apply for, belong to, apologise for, complain about"],
            ["Adjective + preposition", "afraid of, good at, interested in, responsible for, aware of, capable of, similar to, different from"],
            ["Noun + preposition", "reason for, solution to, effect on, increase in, attitude towards, experience in/with, access to"],
            ["Preposition + gerund", "instead of waiting; good at debugging; look forward to meeting (to = preposition here)"],
        ],
    ))
    s.append(advanced(
        "<p>Phrasal-prepositional verbs take a particle + preposition: <em>put up with, look forward to, get on with, run out of</em>. "
        "See Part 22. Pronouns go after the preposition: <em>look after them</em> (not <em>look them after</em>).</p>"
    ))

    s.append(part_footer())
    return "\n".join(s)


def parts_1_to_8():
    return "\n".join([
        part_01(), part_02(), part_03(), part_04(),
        part_05(), part_06(), part_07(), part_08(),
    ])
