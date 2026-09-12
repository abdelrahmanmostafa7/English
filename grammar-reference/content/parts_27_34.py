"""Parts 27–34: Register, mistakes, indexes, CEFR, quick reference."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, box
)


def part_27():
    s = []
    s.append(part_header(27, "Formal vs Informal English",
        "Grammar choices shift with audience and channel. The same idea can be grammatical in several registers; "
        "choose forms that fit meetings, emails, documentation, or academic writing."))

    s.append(table(
        ["Feature", "Informal / spoken", "Formal / written"],
        [
            ["Contractions", "I'm, don't, we've, who's", "I am, do not, we have, who is (often preferred in academic prose)"],
            ["Questions", "Got a minute? / You coming?", "Do you have a minute? / Are you coming?"],
            ["Relative pronouns", "the bug we found", "the bug that/which we found"],
            ["Modals", "Can you send…?", "Could/Would you please send…? / I would be grateful if…"],
            ["Multi-word verbs", "look into, put off, find out", "investigate, postpone, determine"],
            ["Negatives", "No idea. / Can't help.", "I have no idea. / I am unable to assist."],
            ["Discourse", "So yeah, basically…", "In summary, … / Therefore, …"],
            ["Passives / nominalizations", "We broke prod.", "A production incident was caused by…"],
        ],
        caption="Register tendencies (not absolute rules)",
    ))

    s.append(examples(
        "<span class='register'>SPOKEN</span> Wanna join the call?",
        "<span class='register'>INFORMAL</span> I'll ping you when it's done.",
        "<span class='register'>STANDARD</span> I'll message you when it is finished.",
        "<span class='register'>FORMAL</span> Please let me know once the process has been completed.",
        "<span class='register'>ACADEMIC</span> The results suggest that caching significantly reduced latency.",
    ))

    s.append(note(
        "<p>Professional tech English often sits between informal and formal: contractions are fine in Slack; "
        "RFCs and incident reports prefer clearer, slightly more formal grammar without sounding stiff.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_28():
    s = []
    s.append(part_header(28, "Common English Mistakes",
        "A cross-topic error bank. Many items also appear in Parts 1–26; this section gathers high-frequency mistakes "
        "for quick scanning, including patterns common among Arabic-speaking learners."))

    s.append(h3("Articles, countability, agreement", "p28-art"))
    s.append(mistakes(
        ("She is engineer.", "She is an engineer."),
        ("I need informations.", "I need information / some information."),
        ("The life is hard.", "Life is hard."),
        ("He go to work by the foot.", "He goes to work on foot."),
        ("The news are bad.", "The news is bad."),
        ("There is many reasons.", "There are many reasons."),
    ))

    s.append(h3("Tenses and aspects", "p28-tense"))
    s.append(mistakes(
        ("I live here since 2019.", "I have lived / have been living here since 2019."),
        ("Yesterday I have seen her.", "Yesterday I saw her."),
        ("I am agree with you.", "I agree with you."),
        ("If I will see him, I will tell him.", "If I see him, I will tell him."),
        ("When I will finish, I call you.", "When I finish, I'll call you."),
    ))

    s.append(h3("Prepositions and word order", "p28-prep"))
    s.append(mistakes(
        ("discuss about the plan", "discuss the plan"),
        ("depend of", "depend on"),
        ("arrive to Cairo", "arrive in Cairo / arrive at the airport"),
        ("married with", "married to"),
        ("explain me the bug", "explain the bug to me"),
        ("She asked to me where is the office.", "She asked me where the office was."),
    ))

    s.append(h3("Pronouns, adjectives, adverbs", "p28-misc"))
    s.append(mistakes(
        ("Me and him fixed it.", "He and I fixed it."),
        ("I am interesting in AI.", "I am interested in AI."),
        ("She speaks English very good.", "She speaks English very well."),
        ("I hardly work every day.", "I work hard every day.", "Unless you mean you almost don't work."),
    ))

    s.append(h3("Notes for Arabic-speaking learners", "p28-ar"))
    s.append(box("warning", "Transfer patterns", """
<p>Arabic and English differ in articles, copula (<em>be</em>), gender/number agreement, and question formation. Watch especially for:</p>
<ul>
<li>Missing <em>be</em>: <span class="wrong">She engineer</span> → <span class="correct">She is an engineer</span></li>
<li>Article overuse/underuse with generics and proper nouns</li>
<li>Using <em>the</em> with general abstract nouns: <span class="wrong">the happiness</span> → <span class="correct">happiness</span> (generic)</li>
<li>Present Perfect avoidance: preferring Past Simple with <em>since/for</em></li>
<li>Preposition calques after verbs like <em>discuss, marry, arrive</em></li>
<li>Double subjects or resumptive pronouns in relatives: <span class="wrong">the bug that I fixed it</span> → <span class="correct">the bug that I fixed</span></li>
<li>Adjective agreement (English adjectives do not pluralise): <span class="wrong">importants files</span> → <span class="correct">important files</span></li>
</ul>
"""))
    s.append(part_footer())
    return "\n".join(s)


def part_29():
    s = []
    s.append(part_header(29, "Confusing Structures",
        "Side-by-side contrasts for pairs that look similar or translate to the same word in other languages."))

    pairs = [
        ("say vs tell", "say something (to someone); tell someone something",
         "She said hello. / She told me the password."),
        ("do vs make", "do = tasks/activities; make = create/produce (many collocations)",
         "do homework / make a decision / make a mistake / do the dishes"),
        ("speak vs talk", "speak = languages/formal address; talk = conversation (overlap exists)",
         "speak Arabic; talk to the client; speak with (AmE)"),
        ("borrow vs lend", "borrow = take temporarily; lend = give temporarily",
         "Can I borrow your charger? / Can you lend me your charger?"),
        ("bring vs take", "bring = towards here/listener; take = away from here (viewpoint matters)",
         "Bring the laptop to the meeting. / Take an umbrella with you."),
        ("learn vs teach", "learn = acquire; teach = instruct",
         "I learned Go. / She taught me Go."),
        ("remember vs remind", "remember = have in memory; remind = make someone remember",
         "I remembered the deadline. / Remind me to send the invoice."),
        ("rise vs raise", "rise = go up (no object); raise = lift/increase (object)",
         "Prices rose. / They raised prices."),
        ("lie vs lay", "lie/lay/lain = recline; lay/laid/laid = put (object)",
         "He lay down. / Lay the cable carefully."),
        ("affect vs effect", "affect = verb; effect = usually noun (result); effectuate rare",
         "This change affects latency. / the effect of caching"),
        ("advice vs advise", "advice = uncountable noun; advise = verb",
         "some advice / I advise you to wait"),
        ("practice vs practise", "AmE: practice for both; BrE: practise verb, practice noun",
         "practise the piano (BrE) / practice medicine"),
        ("job vs work", "job = countable role; work = uncountable activity/place",
         "a new job / a lot of work / at work"),
        ("fun vs funny", "fun = enjoyable; funny = humorous",
         "The hackathon was fun. / His joke was funny."),
        ("used to vs be used to vs get used to", "past habit / be accustomed / become accustomed",
         "I used to code in Perl. / I'm used to on-call. / You'll get used to the timezone."),
        ("agree vs accept", "agree = share opinion / consent; accept = receive/approve something offered",
         "I agree with you. / I accept the offer. (not <em>I am agree</em>)"),
        ("especially vs specially", "especially = above all; specially = for a special purpose",
         "especially useful for APIs / specially designed hardware"),
        ("another / other / others / the other", "another = one more; other + noun; others = plural pronoun; the other = specific remaining",
         "another ticket; other tickets; others agreed; the other option"),
        ("few vs a few / little vs a little", "few/little = negative; a few/a little = some (positive)",
         "Few tests failed. / A few tests failed."),
        ("each vs every", "each = individuals; every = members of a set (often interchangeable)",
         "each service has an owner; every day"),
        ("some vs any", "some = offers/affirmatives; any = negatives/questions (with many exceptions)",
         "Would you like some tea? / We don't have any tea."),
        ("much vs many", "much + uncountable; many + plural",
         "much time / many meetings"),
        ("since vs for", "since + point; for + duration",
         "since Monday / for three days"),
        ("during vs while", "during + noun; while + clause",
         "during the outage / while the outage continued"),
        ("despite vs although", "despite + noun/gerund; although + clause",
         "despite the risk / although it was risky"),
        ("because vs because of", "because + clause; because of + noun",
         "because it failed / because of the failure"),
        ("listen vs hear", "listen = intentional; hear = perceive",
         "Listen to the call. / Did you hear that alert?"),
        ("watch vs see vs look", "watch = attention over time; see = perceive; look = direct eyes",
         "watch the demo / see a bug / look at the chart"),
        ("hope vs wish", "hope = possible; wish = unreal/regret often",
         "I hope we ship. / I wish we had shipped earlier."),
        ("in the end vs at the end", "in the end = finally/result; at the end = at the finishing point",
         "In the end we rolled back. / At the end of the meeting…"),
        ("actually vs currently", "actually = in fact; currently = at present",
         "Actually, it's fixed. / Currently, it's broken."),
        ("economic vs economical", "economic = economy-related; economical = money-saving",
         "economic policy / an economical plan"),
        ("historic vs historical", "historic = important in history; historical = related to the past",
         "a historic launch / historical data"),
        ("sensible vs sensitive", "sensible = reasonable; sensitive = easily affected / confidential",
         "a sensible default / sensitive data"),
    ]

    rows = []
    for title, diff, ex in pairs:
        rows.append(f'<div class="rule-block"><h4>{title}</h4><p>{diff}</p>{examples(ex)}</div>')
    s.extend(rows)

    s.append(part_footer())
    return "\n".join(s)


def part_30():
    s = []
    s.append(part_header(30, "Natural English Grammar",
        "Some forms are grammatical but odd in context; others are 'incorrect' in school grammar but normal in speech. "
        "Labels below mark register so you can choose deliberately."))

    s.append(table(
        ["Pattern", "Label", "Comment"],
        [
            ["I'm / don't / we've", "STANDARD in speech; often OK in email", "Avoid heavy contraction density in formal essays"],
            ["Wanna / gonna / gotta", "SPOKEN / INFORMAL", "Don't write in professional docs"],
            ["There's + plural", "SPOKEN", "Write There are"],
            ["Me and Sara went…", "non-standard subject case", "Use Sara and I in careful English"],
            ["If I was…", "SPOKEN / INFORMAL", "If I were… more formal/subjunctive"],
            ["Who did you give it to?", "STANDARD modern", "To whom… is formal"],
            ["The reason is because…", "common; often edited", "Prefer The reason is that…"],
            ["Hopefully, we'll ship", "STANDARD for many", "Some still prefer It is to be hoped that…"],
            ["Sentence fragments in replies", "SPOKEN", "On my way. / Can't today."],
            ["They as singular generic", "STANDARD modern", "Preferred over he/she in many style guides"],
            ["Less + plural", "SPOKEN", "Fewer in careful writing"],
            ["Can I… for permission", "STANDARD modern", "May I… more formal"],
        ],
    ))

    s.append(examples(
        "<span class='register'>SPOKEN</span> You free at 5?",
        "<span class='register'>INFORMAL</span> Just shipped. Looks good on my side.",
        "<span class='register'>STANDARD</span> I've just shipped the fix. It looks good on my side.",
        "<span class='register'>FORMAL</span> The fix has been deployed, and initial checks appear satisfactory.",
        "<span class='register'>RARE</span> Seldom have we encountered such a failure mode.",
    ))

    s.append(note(
        "<p>Naturalness is about collocation and information packaging, not only correctness. "
        "Read native professional writing in your field and notice repeated patterns.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_31():
    s = []
    s.append(part_header(31, "CEFR Reference",
        "Approximate CEFR mapping for major grammar topics. Levels show when learners typically meet and expand a topic — "
        "not a hard ceiling. Many structures begin early and deepen through C2."))

    s.append(table(
        ["Topic", "A1", "A2", "B1", "B2", "C1", "C2"],
        [
            ["Word order SVO / be / basic questions", "●", "●", "●", "●", "●", "●"],
            ["Articles a/an/the basics", "●", "●", "●", "deepen", "nuance", "nuance"],
            ["Zero article / generics", "", "○", "●", "●", "●", "●"],
            ["Present Simple / Continuous", "●", "●", "●", "●", "●", "●"],
            ["Past Simple / Continuous", "○", "●", "●", "●", "●", "●"],
            ["Present Perfect", "", "○", "●", "●", "●", "●"],
            ["Present Perfect Continuous", "", "", "○", "●", "●", "●"],
            ["Past Perfect (+ continuous)", "", "", "○", "●", "●", "●"],
            ["Future forms (will/going to/continuous)", "○", "●", "●", "●", "●", "●"],
            ["Future Perfect forms", "", "", "", "○", "●", "●"],
            ["Modals (core)", "○", "●", "●", "●", "●", "●"],
            ["Modal perfects / subtle deduction", "", "", "○", "●", "●", "●"],
            ["Conditionals 0–1", "", "○", "●", "●", "●", "●"],
            ["Conditionals 2–3 / mixed", "", "", "○", "●", "●", "●"],
            ["Inverted conditionals", "", "", "", "", "○", "●"],
            ["Passive (basic → advanced)", "", "○", "●", "●", "●", "●"],
            ["Reported speech", "", "○", "●", "●", "●", "●"],
            ["Relative clauses (defining)", "", "○", "●", "●", "●", "●"],
            ["Non-defining / reduced relatives", "", "", "○", "●", "●", "●"],
            ["Gerunds & infinitives (patterns)", "", "○", "●", "●", "●", "●"],
            ["Phrasal verbs (high frequency)", "", "○", "●", "●", "●", "●"],
            ["Causatives", "", "", "○", "●", "●", "●"],
            ["Clefts / inversion / fronting", "", "", "", "○", "●", "●"],
            ["Discourse markers / cohesion", "", "○", "●", "●", "●", "●"],
            ["Register control", "", "", "○", "●", "●", "●"],
        ],
        caption="● typically established · ○ typically introduced · deepen/nuance = continue refining",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_32():
    s = []
    s.append(part_header(32, "Master Quick Reference",
        "Dense lookup tables for revision and printing as a cheat-deck inside the full reference."))

    s.append(h3("Tenses (summary)", "p32-tense"))
    s.append(table(
        ["", "Simple", "Continuous", "Perfect", "Perfect Continuous"],
        [
            ["Present", "work(s)", "am/is/are working", "have/has worked", "have/has been working"],
            ["Past", "worked", "was/were working", "had worked", "had been working"],
            ["Future", "will work", "will be working", "will have worked", "will have been working"],
        ],
    ))

    s.append(h3("Modals (summary)", "p32-modals"))
    s.append(table(
        ["Modal", "Ability", "Permission", "Obligation", "Possibility"],
        [
            ["can", "yes", "yes", "—", "yes"],
            ["could", "past/polite", "polite", "—", "yes"],
            ["may", "—", "formal", "—", "yes"],
            ["might", "—", "rare", "—", "yes"],
            ["must", "—", "—", "yes / deduction", "deduction"],
            ["should", "—", "—", "advice", "expectation"],
            ["will", "—", "—", "—", "prediction"],
            ["would", "—", "polite", "—", "hypothetical"],
        ],
    ))

    s.append(h3("Articles (summary)", "p32-art"))
    s.append(table(
        ["Choose", "When"],
        [
            ["a/an", "singular countable, not uniquely identified"],
            ["the", "identifiable / unique / second mention / superlatives"],
            ["∅", "plural/uncountable generics; many institutions/meals/languages/sports patterns"],
        ],
    ))

    s.append(h3("Conditionals (summary)", "p32-cond"))
    s.append(table(
        ["Type", "Pattern"],
        [
            ["0", "If + present, present"],
            ["1", "If + present, will/modal/imperative"],
            ["2", "If + past, would + V"],
            ["3", "If + past perfect, would have + PP"],
            ["Mixed", "If + past perfect, would + V (etc.)"],
        ],
    ))

    s.append(h3("Passive (summary)", "p32-pass"))
    s.append(p("be (in the right tense) + past participle · modal + be + PP · modal + have been + PP"))

    s.append(h3("Reported speech (summary)", "p32-rep"))
    s.append(p("Backshift after past reporting verbs when needed · statement order in reported questions · tell + person · say (+ that)"))

    s.append(h3("Gerund / infinitive (summary)", "p32-gi"))
    s.append(p("enjoy/avoid/suggest + -ing · want/decide/hope + to · make/let + bare infinitive · look forward to + -ing"))

    s.append(h3("Prepositions (summary)", "p32-prep"))
    s.append(p("in/on/at (time & place) · for/since · by/until · during/while · between/among · despite + noun · although + clause"))

    s.append(h3("Questions (summary)", "p32-q"))
    s.append(p("Auxiliary inversion · do-support · subject questions without do · embedded questions in statement order"))

    s.append(h3("Comparison (summary)", "p32-comp"))
    s.append(p("-er/-est or more/most · as…as · much/far + comparative · the more…, the more…"))

    s.append(h3("Pronouns (summary)", "p32-pron"))
    s.append(p("I/me/my/mine/myself · they singular generic · there is/are · dummy it"))

    s.append(h3("Determiners (summary)", "p32-det"))
    s.append(p("predet (all/both/half) → central (a/the/this/my) → post (two/many/other) → adjectives → noun"))

    s.append(h3("Irregular verbs (extended sample)", "p32-irr"))
    s.append(table(
        ["Base", "Past", "PP"],
        [
            ["arise", "arose", "arisen"],
            ["awake", "awoke", "awoken"],
            ["bear", "bore", "borne"],
            ["beat", "beat", "beaten"],
            ["become", "became", "become"],
            ["begin", "began", "begun"],
            ["bend", "bent", "bent"],
            ["bet", "bet", "bet"],
            ["bind", "bound", "bound"],
            ["bite", "bit", "bitten"],
            ["bleed", "bled", "bled"],
            ["blow", "blew", "blown"],
            ["broadcast", "broadcast", "broadcast"],
            ["burn", "burnt/burned", "burnt/burned"],
            ["burst", "burst", "burst"],
            ["cast", "cast", "cast"],
            ["choose", "chose", "chosen"],
            ["cling", "clung", "clung"],
            ["come", "came", "come"],
            ["cost", "cost", "cost"],
            ["creep", "crept", "crept"],
            ["cut", "cut", "cut"],
            ["deal", "dealt", "dealt"],
            ["dig", "dug", "dug"],
            ["draw", "drew", "drawn"],
            ["dream", "dreamt/dreamed", "dreamt/dreamed"],
            ["drink", "drank", "drunk"],
            ["drive", "drove", "driven"],
            ["eat", "ate", "eaten"],
            ["fall", "fell", "fallen"],
            ["feed", "fed", "fed"],
            ["fight", "fought", "fought"],
            ["find", "found", "found"],
            ["fly", "flew", "flown"],
            ["forbid", "forbade", "forbidden"],
            ["forecast", "forecast", "forecast"],
            ["forget", "forgot", "forgotten"],
            ["forgive", "forgave", "forgiven"],
            ["freeze", "froze", "frozen"],
            ["get", "got", "got/gotten (AmE)"],
            ["give", "gave", "given"],
            ["grow", "grew", "grown"],
            ["hang", "hung/hanged", "hung/hanged"],
            ["hide", "hid", "hidden"],
            ["hit", "hit", "hit"],
            ["hold", "held", "held"],
            ["hurt", "hurt", "hurt"],
            ["keep", "kept", "kept"],
            ["know", "knew", "known"],
            ["lay", "laid", "laid"],
            ["lead", "led", "led"],
            ["lean", "leant/leaned", "leant/leaned"],
            ["leap", "leapt/leaped", "leapt/leaped"],
            ["learn", "learnt/learned", "learnt/learned"],
            ["leave", "left", "left"],
            ["lend", "lent", "lent"],
            ["let", "let", "let"],
            ["lie", "lay", "lain"],
            ["light", "lit/lighted", "lit/lighted"],
            ["lose", "lost", "lost"],
            ["make", "made", "made"],
            ["mean", "meant", "meant"],
            ["meet", "met", "met"],
            ["overcome", "overcame", "overcome"],
            ["prove", "proved", "proved/proven"],
            ["quit", "quit", "quit"],
            ["ride", "rode", "ridden"],
            ["ring", "rang", "rung"],
            ["rise", "rose", "risen"],
            ["run", "ran", "run"],
            ["saw", "sawed", "sawn/sawed"],
            ["say", "said", "said"],
            ["see", "saw", "seen"],
            ["seek", "sought", "sought"],
            ["sell", "sold", "sold"],
            ["send", "sent", "sent"],
            ["set", "set", "set"],
            ["shake", "shook", "shaken"],
            ["shine", "shone", "shone"],
            ["shoot", "shot", "shot"],
            ["show", "showed", "shown/showed"],
            ["shrink", "shrank", "shrunk"],
            ["shut", "shut", "shut"],
            ["sing", "sang", "sung"],
            ["sink", "sank", "sunk"],
            ["sit", "sat", "sat"],
            ["sleep", "slept", "slept"],
            ["slide", "slid", "slid"],
            ["smell", "smelt/smelled", "smelt/smelled"],
            ["speak", "spoke", "spoken"],
            ["spend", "spent", "spent"],
            ["spill", "spilt/spilled", "spilt/spilled"],
            ["spin", "spun", "spun"],
            ["spit", "spat/spit", "spat/spit"],
            ["split", "split", "split"],
            ["spoil", "spoilt/spoiled", "spoilt/spoiled"],
            ["spread", "spread", "spread"],
            ["stand", "stood", "stood"],
            ["steal", "stole", "stolen"],
            ["stick", "stuck", "stuck"],
            ["sting", "stung", "stung"],
            ["strike", "struck", "struck/stricken"],
            ["swear", "swore", "sworn"],
            ["sweep", "swept", "swept"],
            ["swim", "swam", "swum"],
            ["swing", "swung", "swung"],
            ["take", "took", "taken"],
            ["teach", "taught", "taught"],
            ["tear", "tore", "torn"],
            ["tell", "told", "told"],
            ["think", "thought", "thought"],
            ["throw", "threw", "thrown"],
            ["understand", "understood", "understood"],
            ["wake", "woke", "woken"],
            ["wear", "wore", "worn"],
            ["weave", "wove", "woven"],
            ["weep", "wept", "wept"],
            ["win", "won", "won"],
            ["wind", "wound", "wound"],
            ["withdraw", "withdrew", "withdrawn"],
            ["write", "wrote", "written"],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_33():
    s = []
    s.append(part_header(33, "Common Error Index",
        "Alphabetical WRONG → CORRECT → EXPLANATION entries for rapid correction lookup."))

    entries = [
        ("A", [
            ("I am agree.", "I agree.", "Agree is a verb; no progressive be + agree in this meaning."),
            ("according to me", "in my opinion / I think", "According to + external source."),
            ("an advice", "some advice / a piece of advice", "Advice is uncountable."),
            ("although… but…", "although… / …but…", "Use one contrast marker, not both."),
            ("arrive to Cairo", "arrive in Cairo", "Arrive in + city; arrive at + point."),
        ]),
        ("B", [
            ("because of he was late", "because he was late / because of his lateness", "Because + clause; because of + noun."),
            ("been to / gone to confusion", "She's gone to Paris (still there) / She's been to Paris (visited)", "Gone vs been."),
        ]),
        ("C", [
            ("Can you tell me where is it?", "Can you tell me where it is?", "Embedded question = statement order."),
            ("discuss about", "discuss", "Discuss takes a direct object."),
            ("despite of", "despite / in spite of", "No of after despite."),
        ]),
        ("D", [
            ("depend of", "depend on", "Fixed preposition."),
            ("didn't went", "didn't go", "After did, use base form."),
            ("do a mistake", "make a mistake", "Collocation."),
        ]),
        ("E", [
            ("every people", "everyone / every person / all people", "Every + singular noun."),
            ("explain me", "explain to me", "Explain something to someone."),
        ]),
        ("F", [
            ("for get used", "get used to", "Be/get used to + noun/gerund."),
            ("from my side, I think", "I think (drop filler)", "Wordy non-native filler."),
        ]),
        ("G", [
            ("go to home", "go home", "No to/the with home in this pattern."),
            ("good in English", "good at English", "Good at + skill."),
        ]),
        ("H", [
            ("hardly work (meaning 'effort')", "work hard", "Hardly = almost not."),
            ("have reason", "be right / have a reason", "Calque; prefer you're right."),
        ]),
        ("I", [
            ("I have 25 years", "I am 25 (years old)", "Age with be."),
            ("if I will see him", "if I see him", "No will in future time/if-clauses."),
            ("in the night (habit)", "at night", "At night = habitual."),
            ("informations", "information", "Uncountable."),
        ]),
        ("J", [
            ("job as a work", "job / work", "Job countable; work uncountable."),
        ]),
        ("K", [
            ("know to swim", "know how to swim", "Know how + infinitive."),
        ]),
        ("L", [
            ("lay down (recline)", "lie down", "Lie = recline; lay needs object."),
            ("listen the music", "listen to the music", "Listen to."),
            ("look forward to meet", "look forward to meeting", "To = preposition."),
        ]),
        ("M", [
            ("married with", "married to", "Fixed preposition."),
            ("must to go", "must go", "Modal + bare infinitive."),
        ]),
        ("N", [
            ("news are", "news is", "News is singular."),
            ("no one don't know", "no one knows", "Already negative."),
        ]),
        ("O", [
            ("one of my friend", "one of my friends", "One of + plural."),
            ("open the light", "turn on the light", "Collocation."),
        ]),
        ("P", [
            ("people is", "people are", "People is plural."),
            ("prefer than", "prefer X to Y", "Prefer to, not than."),
        ]),
        ("Q", [
            ("quiet / quite mix", "quiet = silent; quite = fairly/completely", "Spelling/meaning."),
        ]),
        ("R", [
            ("recommend me a book → *recommend me that", "recommend a book (to me) / recommend that I…", "Pattern care."),
            ("return back", "return / go back", "Return already includes back."),
        ]),
        ("S", [
            ("said me", "told me / said to me", "Say vs tell."),
            ("sheeps", "sheep", "Zero plural."),
            ("since two years", "for two years / since 2024", "For duration; since point."),
            ("succeed to do", "succeed in doing", "Succeed in + gerund."),
            ("suggest to go", "suggest going / suggest that we go", "Suggest + gerund/that."),
        ]),
        ("T", [
            ("take a decision", "make a decision (also take in some varieties)", "Make is safest internationally."),
            ("the both options", "both options / both of the options", "Determiner order."),
            ("there have", "there are / they have", "Existential is/are."),
        ]),
        ("U", [
            ("until / by mix", "by = deadline; until = continuing up to", "See Part 8."),
            ("used to do vs be used to doing", "past habit vs accustomed", "See Part 29."),
        ]),
        ("V", [
            ("very better", "much/far better", "Don't use very + comparative."),
        ]),
        ("W", [
            ("when I will arrive", "when I arrive", "Present in future time clause."),
            ("worth to see", "worth seeing", "Worth + gerund."),
            ("Who did see you?", "Who saw you?", "Subject question."),
        ]),
        ("Y", [
            ("yesterday night", "last night", "Collocation."),
        ]),
    ]

    s.append('<div class="error-index">')
    for letter, items in entries:
        s.append(f'<h3 id="err-{letter}">{letter}</h3>')
        for w, c, e in items:
            s.append(
                f'<div class="entry"><div><span class="w">{w}</span> → <span class="c">{c}</span></div>'
                f'<div class="e">{e}</div></div>'
            )
    s.append("</div>")
    s.append(part_footer())
    return "\n".join(s)


def part_34():
    s = []
    s.append(part_header(34, "Grammar Index",
        "Alphabetical topic index with links to parts. Use this when you remember the name of a structure but not its chapter."))

    index = {
        "A": [
            ("Adjectives", "part-06"),
            ("Adjective order", "part-06"),
            ("Adverbs", "part-07"),
            ("Articles", "part-05"),
            ("as… as", "part-19"),
            ("Auxiliary verbs", "part-01"),
        ],
        "B": [
            ("be going to", "part-10"),
            ("because / because of", "part-29"),
        ],
        "C": [
            ("Causatives", "part-21"),
            ("CEFR map", "part-31"),
            ("Clauses", "part-18"),
            ("Cleft sentences", "part-24"),
            ("Comparatives", "part-19"),
            ("Conditionals", "part-13"),
            ("Countable nouns", "part-02"),
        ],
        "D": [
            ("Determiners", "part-04"),
            ("Discourse markers", "part-25"),
            ("do vs make", "part-29"),
        ],
        "E": [
            ("Ellipsis", "part-24"),
            ("Emphasis (do)", "part-24"),
            ("Error index", "part-33"),
            ("Existential there", "part-03"),
        ],
        "F": [
            ("Formal vs informal", "part-27"),
            ("Future forms", "part-10"),
            ("Future in the past", "part-10"),
        ],
        "G": [
            ("Gerunds", "part-12"),
            ("get-passive", "part-14"),
        ],
        "H": [
            ("have something done", "part-21"),
            ("hard / hardly", "part-07"),
        ],
        "I": [
            ("if only / wish", "part-13"),
            ("Indefinite pronouns", "part-03"),
            ("Infinitives", "part-12"),
            ("Inversion", "part-24"),
            ("Irregular verbs", "part-32"),
        ],
        "L": [
            ("Linking verbs", "part-01"),
        ],
        "M": [
            ("Modals", "part-11"),
            ("Modal perfects", "part-11"),
            ("Multi-word verbs", "part-22"),
        ],
        "N": [
            ("Negation", "part-17"),
            ("Nouns", "part-02"),
            ("Noun clauses", "part-18"),
        ],
        "P": [
            ("Participles", "part-20"),
            ("Passive voice", "part-14"),
            ("Phrasal verbs", "part-22"),
            ("Possessives", "part-02"),
            ("Prepositions", "part-08"),
            ("Present Perfect", "part-10"),
            ("Pronouns", "part-03"),
            ("Punctuation", "part-26"),
        ],
        "Q": [
            ("Quantifiers", "part-04"),
            ("Questions", "part-16"),
            ("Question tags", "part-16"),
        ],
        "R": [
            ("Reciprocal pronouns", "part-03"),
            ("Reduced clauses", "part-18"),
            ("Reflexive pronouns", "part-03"),
            ("Relative clauses", "part-18"),
            ("Reported speech", "part-15"),
        ],
        "S": [
            ("Sentence patterns", "part-01"),
            ("Stative verbs", "part-09"),
            ("Subject questions", "part-16"),
            ("Superlatives", "part-19"),
        ],
        "T": [
            ("Tenses", "part-10"),
            ("tell vs say", "part-15"),
        ],
        "U": [
            ("Uncountable nouns", "part-02"),
            ("used to / be used to", "part-29"),
        ],
        "W": [
            ("will vs going to", "part-10"),
            ("Word order", "part-23"),
        ],
        "Z": [
            ("Zero article", "part-05"),
            ("Zero conditional", "part-13"),
        ],
    }

    s.append('<div class="index-alpha">')
    for letter, items in index.items():
        s.append(f'<div class="letter"><h4>{letter}</h4><ul>')
        for name, anchor in items:
            s.append(f'<li><a href="#{anchor}">{name}</a></li>')
        s.append("</ul></div>")
    s.append("</div>")
    s.append(part_footer())
    return "\n".join(s)


def parts_27_to_34():
    return "\n".join([
        part_27(), part_28(), part_29(), part_30(),
        part_31(), part_32(), part_33(), part_34(),
    ])
