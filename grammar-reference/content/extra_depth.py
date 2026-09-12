"""Additional depth blocks appended into thinner parts before </section>."""
from helpers import (
    h3, p, ul, rule, examples, mistakes, compare, note, warning, advanced, table, box
)


def expand(part_num: int) -> str:
    fn = globals().get(f"x{part_num:02d}")
    return fn() if fn else ""


def x04():
    return "\n".join([
        h3("Quantifier details learners miss", "p4-extra"),
        rule(
            "some / any / no",
            "Some is common in affirmatives and polite offers/requests. Any is common in negatives and many questions. "
            "No + noun is a determiner alternative to not any.",
            examples_list=[
                "We need some more disk space.",
                "Would you like some coffee? (expecting yes)",
                "Do you have any questions? / I don't have any questions.",
                "There is no easy fix.",
                "Any engineer can join the on-call rotation. (any = every / whichever)",
            ],
            levels=["A2", "B1"],
        ),
        rule(
            "enough / too / plenty of",
            "Enough comes after adjectives/adverbs but before nouns: <em>clear enough / enough time</em>.",
            examples_list=[
                "The docs aren't clear enough.",
                "We don't have enough reviewers.",
                "The query is too slow for production.",
                "There's plenty of coffee in the kitchen.",
            ],
            mistakes_list=[
                ("enough clear", "clear enough"),
                ("money enough", "enough money", "Enough usually precedes nouns."),
            ],
            levels=["A2", "B1"],
        ),
        rule(
            "another / other / others / the other / the others",
            "These mark remaining or additional referents and are easy to confuse.",
            examples_list=[
                "Open another ticket. (one more, unspecified)",
                "Other tickets can wait.",
                "Some tests passed; others failed.",
                "We have two options. The other is riskier.",
                "One service is down; the others are healthy.",
            ],
            levels=["A2", "B1", "B2"],
        ),
        table(
            ["Determiner stack example", "Breakdown"],
            [
                ["all the first three urgent tickets", "pre: all · central: the · post: first three · adj: urgent · noun"],
                ["both my last two managers", "pre: both · central: my · post: last two"],
                ["twice the original estimate", "pre: twice · central: the · adj: original"],
                ["such an unusual failure", "pre: such · central: an · adj: unusual"],
            ],
        ),
    ])


def x05():
    return "\n".join([
        h3("Difficult article cases", "p5-hard"),
        table(
            ["Pattern", "Example", "Note"],
            [
                ["the + adjective = group", "the rich, the unemployed, the injured", "plural meaning; formal"],
                ["the + nationality adjective", "the French, the Japanese", "people as a group; compare French people"],
                ["most vs the most", "Most engineers… / the most careful engineer", "most = majority; the most = superlative"],
                ["hospital / school / prison", "in hospital (BrE patient) / in the hospital (AmE or building)", "purpose vs place"],
                ["TV / radio / internet", "watch TV; on the radio; on the internet", "collocations"],
                ["instruments vs music", "play the guitar; listen to music", ""],
                ["seasons", "in summer / in the summer", "both common"],
                ["illnesses", "have flu (BrE) / have the flu (AmE); have a cold; have cancer", "item-specific"],
                ["titles", "Queen Elizabeth; the Queen; President Lee; the president", "name vs role"],
                ["next / last", "next week; the next week (specific relative)", "discourse-sensitive"],
            ],
        ),
        rule(
            "Generic reference: three common systems",
            "English has several generic patterns that are not free variants in every context.",
            examples_list=[
                "A product manager balances trade-offs. (any member of the class)",
                "The product manager balances trade-offs. (the role as a type — formal/academic feel)",
                "Product managers balance trade-offs. (most natural plural generic)",
                "Software eats the world. (uncountable/mass generic)",
            ],
            levels=["B1", "B2", "C1"],
        ),
        advanced(
            "<p>Fixed phrases: <em>to work / go to work / at work</em>; <em>to bed / in bed</em>; "
            "<em>to school / at school / in school (AmE)</em>; <em>by car/bus/train/email</em>; "
            "<em>on foot</em>; <em>in cash / by credit card</em>; <em>in writing</em>; "
            "<em>at first / in the beginning</em> (not always interchangeable).</p>"
        ),
    ])


def x06():
    return "\n".join([
        h3("Adjective complements and patterns", "p6-extra"),
        rule(
            "Adjective + that-clause / to-infinitive",
            "Many adjectives take clausal complements.",
            examples_list=[
                "I'm glad that you joined.",
                "She was surprised to see the results.",
                "It's important to document edge cases.",
                "The API is easy to use. / The API is easy to use incorrectly. (note: object gaps)",
            ],
            levels=["B1", "B2"],
        ),
        table(
            ["Adjective", "Typical preposition", "Example"],
            [
                ["aware / conscious", "of", "aware of the risk"],
                ["capable / incapable", "of", "capable of scaling"],
                ["dependent", "on", "dependent on caching"],
                ["different", "from / to / than", "different from ours"],
                ["familiar", "with", "familiar with Kafka"],
                ["famous / known", "for", "famous for uptime"],
                ["fond", "of", "fond of refactoring"],
                ["good / bad / weak", "at", "good at estimating"],
                ["interested", "in", "interested in security"],
                ["keen", "on", "keen on typed languages"],
                ["proud", "of", "proud of the launch"],
                ["responsible", "for", "responsible for billing"],
                ["satisfied / pleased", "with", "satisfied with the fix"],
                ["similar", "to", "similar to OAuth"],
                ["worried / excited", "about", "worried about downtime"],
            ],
        ),
        rule(
            "Only / main / mere / living — attributive-leaning adjectives",
            "Some adjectives usually appear before nouns: <em>the only solution, the main reason, a mere prototype, the very person</em>.",
            examples_list=[
                "That's the only blocker. (not usually <em>The blocker is only</em> with this meaning)",
                "The chief advantage is speed.",
            ],
            levels=["B2", "C1"],
        ),
    ])


def x07():
    return "\n".join([
        h3("Focusing adverbs and scope", "p7-extra"),
        rule(
            "only / even / also / just / mainly",
            "Focusing adverbs attach to the following constituent. Move them and the meaning changes.",
            examples_list=[
                "Only Nora reviewed the PR. (nobody else did)",
                "Nora only reviewed the PR. (she didn't approve/merge — depending on stress)",
                "Even the intern spotted it.",
                "We also need load tests.",
                "I just restarted the pod. (recently / merely — ambiguous; context decides)",
            ],
            levels=["B1", "B2", "C1"],
        ),
        rule(
            "still / yet / already / anymore",
            "These time-related adverbs interact with aspect and polarity.",
            examples_list=[
                "Are you still on-call?",
                "Have you finished yet? (questions/negatives)",
                "We've already shipped.",
                "We don't support IE anymore / any more.",
            ],
            mistakes_list=[
                ("I yet finished.", "I haven't finished yet. / I finished already."),
            ],
            levels=["A2", "B1"],
        ),
        compare(
            "<p><em>late</em> vs <em>lately</em>; <em>hard</em> vs <em>hardly</em> — see the lookalike table above. "
            "Also: <em>free</em> (without cost) vs <em>freely</em> (without restriction); "
            "<em>high</em> vs <em>highly recommended</em>.</p>"
        ),
    ])


def x08():
    return "\n".join([
        h3("Extended dependent preposition lists", "p8-extra"),
        table(
            ["Verb + prep", "Example"],
            [
                ["apologise for", "apologise for the delay"],
                ["apply for / to", "apply for a role; apply to a company"],
                ["approve of", "approve of the change (opinion) vs approve the change (authorise)"],
                ["argue with / about", "argue with a colleague about priorities"],
                ["believe in", "believe in the roadmap"],
                ["blame for", "blame the outage on a timeout / blame someone for…"],
                ["care about / for", "care about quality; care for a patient"],
                ["complain about / to", "complain about latency to support"],
                ["concentrate on", "concentrate on the root cause"],
                ["consist of", "consist of three services"],
                ["cope with", "cope with traffic spikes"],
                ["deal with", "deal with incidents"],
                ["decide on", "decide on a vendor"],
                ["focus on", "focus on reliability"],
                ["insist on", "insist on a review"],
                ["object to", "object to the proposal"],
                ["pay for", "pay for cloud spend"],
                ["rely / depend on", "rely on replicas"],
                ["result in", "result in downtime"],
                ["specialise in", "specialise in distributed systems"],
                ["suffer from", "suffer from cold starts"],
                ["wait for", "wait for approval"],
            ],
        ),
        table(
            ["Noun + prep", "Example"],
            [
                ["access to", "access to production"],
                ["alternative to", "alternative to Redis"],
                ["attack on", "attack on the API"],
                ["attitude towards/to", "attitude towards risk"],
                ["cause of", "cause of the failure"],
                ["decrease / increase in", "increase in latency"],
                ["demand for", "demand for features"],
                ["difference between", "difference between envs"],
                ["effect on", "effect on users"],
                ["example of", "example of a race"],
                ["experience in/of/with", "experience with Go"],
                ["influence on", "influence on culture"],
                ["need for", "need for backups"],
                ["reason for", "reason for the delay"],
                ["relationship with/between", "relationship with vendors"],
                ["solution to", "solution to the bug"],
            ],
        ),
        warning(
            "<p>Do not invent prepositions from translation. If unsure, check a collocation dictionary "
            "or rewrite: <em>We discussed the plan</em> (not <em>discussed about</em>).</p>"
        ),
    ])


def x11():
    return "\n".join([
        h3("Requests, offers, permission — politeness ladder", "p11-extra"),
        table(
            ["More direct", "More polite / soft"],
            [
                ["Can you review this?", "Could you review this when you have a moment?"],
                ["I want your feedback.", "I'd like your feedback. / I was wondering if you could…"],
                ["Give me access.", "Could I get access to staging?"],
                ["You must restart it.", "You'll need to restart it. / You should restart it."],
                ["Shall I open a ticket? (BrE offer)", "I can open a ticket if that helps."],
            ],
        ),
        rule(
            "shall",
            "In modern AmE, <em>shall</em> is rare except in legal writing. In BrE it remains in offers/suggestions: "
            "<em>Shall we start?</em> For obligation in contracts: <em>The vendor shall provide…</em>",
            levels=["B2", "C1"],
        ),
        rule(
            "need as modal (BrE)",
            "BrE allows modal <em>need</em> mainly in negatives/questions: <em>Need I say more? / You needn't come.</em> "
            "AmE prefers <em>need to / don't need to</em>.",
            examples_list=[
                "You needn't worry. <span class='register'>BrE</span>",
                "You don't need to worry. (general)",
                "You needn't have brought food. (= brought, but unnecessary)",
                "You didn't need to bring food. (wasn't necessary — maybe you didn't)",
            ],
            levels=["B2", "C1"],
        ),
    ])


def x12():
    return "\n".join([
        h3("More verb patterns", "p12-extra"),
        table(
            ["Verb", "Pattern", "Example"],
            [
                ["admit / deny / mention", "+ gerund / that", "She admitted making a mistake."],
                ["advise / encourage / urge", "+ object + to", "They advised us to wait."],
                ["avoid / delay / postpone", "+ gerund", "Avoid shipping on Fridays."],
                ["can't help", "+ gerund", "I can't help worrying."],
                ["consider / imagine", "+ gerund", "Consider using a queue."],
                ["expect", "+ to / object + to", "I expect to finish. / I expect you to finish."],
                ["feel like", "+ gerund", "I feel like quitting Vim."],
                ["finish / keep / practise", "+ gerund", "Keep trying."],
                ["happen", "+ to", "I happened to notice a leak."],
                ["intend / mean", "+ to", "We intend to migrate."],
                ["manage / fail / afford", "+ to", "We managed to recover."],
                ["mind", "+ gerund", "Would you mind waiting?"],
                ["persuade / convince / force", "+ object + to", "We persuaded them to extend."],
                ["pretend / refuse / threaten", "+ to", "They refused to sign."],
                ["recommend / suggest", "+ gerund / that", "I recommend waiting."],
                ["seem / tend / appear", "+ to", "The issue seems to recur."],
                ["spend time", "+ gerund", "We spent hours debugging."],
                ["would rather", "+ bare / than", "I'd rather deploy tomorrow."],
                ["had better", "+ bare", "You'd better encrypt it."],
            ],
        ),
        note(
            "<p>Sense verbs: <em>I saw him leave</em> (complete action) vs <em>I saw him leaving</em> (in progress). "
            "Passive: <em>He was seen to leave</em> (formal) / <em>leaving</em>.</p>"
        ),
    ])


def x13():
    return "\n".join([
        h3("Real vs unreal — decision guide", "p13-extra"),
        ul(
            "Ask: Is the condition possible/open? → Zero/First (real).",
            "Ask: Is it hypothetical now/future? → Second (unreal present/future).",
            "Ask: Are you imagining a different past? → Third (unreal past).",
            "Ask: Does a past unreal condition affect now? → Mixed (had + would).",
        ),
        rule(
            "if + should / happen to",
            "Makes conditions less likely or more tentative — useful in polite instructions.",
            examples_list=[
                "If you should see a Sev-1, page me immediately.",
                "If you happen to find the logs, send them over.",
                "Should the build fail, revert the commit. (inversion)",
            ],
            levels=["C1", "C2"],
        ),
        rule(
            "will / would in if-clauses",
            "Normally avoid <em>will</em> after <em>if</em> for time reference. Exceptions: willingness, polite insistence, or result meaning.",
            examples_list=[
                "If you will wait here, I'll get the key. (willingness)",
                "If you would take a seat… (polite)",
                "If it will make you happier, we can add logging. (result/willingness reading)",
            ],
            levels=["C1"],
        ),
    ])


def x14():
    return "\n".join([
        h3("When passive is natural", "p14-extra"),
        ul(
            "Unknown agent: <em>My laptop was stolen.</em>",
            "Obvious agent: <em>The suspect was arrested.</em>",
            "Process focus / scientific style: <em>The sample was heated to 80°C.</em>",
            "Diplomacy: <em>Mistakes were made.</em> (agent hidden — sometimes evasive)",
            "Information structure: put long/new agents at the end with <em>by</em>.",
        ),
        rule(
            "Verbs that rarely passivise",
            "Intransitive verbs have no passive. Some stative/possessive patterns also resist: "
            "<em>*A car is had by me</em> is wrong. Symmetrical verbs and measure expressions need care.",
            examples_list=[
                "The meeting lasted an hour. (no passive)",
                "This cable costs $20. (no passive)",
                "She resembles her mentor. (no passive)",
            ],
            levels=["B2", "C1"],
        ),
        mistakes(
            ("The issue was happened yesterday.", "The issue happened yesterday."),
            ("It was agreed the plan.", "It was agreed that we would follow the plan. / The plan was agreed."),
        ),
    ])


def x15():
    return "\n".join([
        h3("Reporting verb patterns", "p15-extra"),
        table(
            ["Pattern", "Verbs"],
            [
                ["verb + that-clause", "say, admit, claim, argue, confirm, deny, explain, insist, promise, threaten, warn"],
                ["verb + person + that", "tell, convince, persuade, remind, warn"],
                ["verb + to-infinitive", "agree, offer, promise, refuse, threaten"],
                ["verb + person + to-infinitive", "ask, tell, advise, encourage, forbid, invite, order, persuade, remind, warn"],
                ["verb + gerund", "admit, deny, recommend, suggest, propose"],
                ["verb + person + for + -ing", "thank, praise, blame, criticise"],
                ["verb + person + of + -ing", "accuse, suspect"],
                ["verb + on + -ing", "congratulate, insist (insist on)"],
            ],
        ),
        examples(
            "She insisted that we wait. / She insisted on waiting.",
            "They accused him of leaking the key.",
            "He apologised for missing the standup.",
            "We were reminded to rotate tokens.",
        ),
    ])


def x16():
    return "\n".join([
        h3("Special question patterns", "p16-extra"),
        rule(
            "Prepositions in questions",
            "Informal English strands prepositions; formal English may front them with <em>whom/which</em>.",
            examples_list=[
                "Who did you give the keys to?",
                "To whom did you give the keys? <span class='register'>FORMAL</span>",
                "What are you looking at?",
                "Which service does this depend on?",
            ],
            levels=["B1", "B2", "C1"],
        ),
        rule(
            "Negative questions",
            "Express surprise, confirmation, or soft persuasion.",
            examples_list=[
                "Isn't this the same bug as last week?",
                "Why don't we postpone?",
                "Haven't you finished yet?",
            ],
            levels=["B1", "B2"],
        ),
        note(
            "<p>Answer negative questions carefully: in English, <em>Yes</em> affirms the positive fact. "
            "If someone asks <em>Aren't you on-call?</em> and you are, answer <em>Yes (I am)</em>.</p>"
        ),
    ])


def x17():
    return "\n".join([
        h3("Neither / nor / either", "p17-extra"),
        examples(
            "Neither option works. / Neither of the options works/work (singular verb safer in formal AmE).",
            "I don't like either approach.",
            "Neither the API nor the workers were reachable.",
            "I can't deploy, and neither can Sara. / …and Sara can't either.",
        ),
        rule(
            "Transferred negation",
            "With verbs like <em>think, believe, suppose</em>, negation often appears in the main clause in everyday English.",
            examples_list=[
                "I don't think it's ready. (more natural than <em>I think it isn't ready</em> in many contexts)",
                "I don't suppose you have a spare token?",
            ],
            levels=["B2", "C1"],
        ),
    ])


def x18():
    return "\n".join([
        h3("Relative clause pitfalls", "p18-extra"),
        mistakes(
            ("The bug that I fixed it was critical.", "The bug that I fixed was critical.", "No resumptive pronoun."),
            ("People which work here…", "People who work here…"),
            ("The reason why that…", "The reason (why/that)…", "Don't stack why + that."),
        ),
        rule(
            "which referring to a whole clause",
            "In non-defining use, <em>which</em> can comment on the entire preceding clause.",
            examples_list=[
                "The deploy finished early, which surprised everyone.",
                "She declined the offer, which I understand.",
            ],
            levels=["B2", "C1"],
        ),
        advanced(
            "<p>Sentential relatives and connective <em>which</em> are common in formal exposition. "
            "Avoid comma + <em>that</em>. Avoid ambiguous <em>which</em> when multiple nouns could be antecedents — rewrite.</p>"
        ),
    ])


def x19():
    return "\n".join([
        h3("Comparison structures in full", "p19-extra"),
        examples(
            "as many tickets as last week / as much traffic as last week",
            "twice as fast as the old query / half as expensive",
            "the same as / similar to / different from",
            "no sooner… than… / hardly… when… (formal narrative)",
            "She is senior to me. (note: senior/junior/superior + to, not than)",
        ),
        mistakes(
            ("more better", "better"),
            ("superior than", "superior to"),
            ("one of the best engineer", "one of the best engineers"),
        ),
        rule(
            "Absolute adjectives — careful grading",
            "Words like <em>unique, perfect, empty, dead, complete</em> are traditionally non-gradable. "
            "In real usage, people say <em>almost unique / more complete</em>. In careful formal writing, prefer "
            "<em>almost/nearly/unique in X respect</em>.",
            levels=["C1"],
        ),
    ])


def x20():
    return "\n".join([
        h3("Participial clause meanings", "p20-extra"),
        table(
            ["Form", "Typical meaning", "Example"],
            [
                ["V-ing…, S V", "time / reason / result (same time or overlapping)", "Seeing the alert, we scaled up."],
                ["Having V-ed…, S V", "earlier completion", "Having rotated the keys, we redeployed."],
                ["V-ed…, S V", "passive / state", "Built in 2019, the service still runs."],
                ["With + NP + participle", "accompanying circumstance", "With the cache failing, reads slowed."],
            ],
        ),
        examples(
            "Compared with last year, revenue is up.",
            "Given the constraints, this design is reasonable.",
            "Granted, the UI is rough — but the API is solid. (discourse participle/discourse marker)",
        ),
    ])


def x22():
    return "\n".join([
        h3("More multi-word verbs by theme", "p22-extra"),
        table(
            ["Theme", "Examples"],
            [
                ["Starting/stopping", "set up, start up, shut down, break down, call off, give up"],
                ["Continuing", "carry on, keep on, go on, stick with"],
                ["Discovery", "find out, figure out, work out, dig into, look into"],
                ["Relationships", "get on with, look up to, look down on, run into"],
                ["Problems", "run into, come up against, deal with, sort out, mess up"],
                ["Communication", "point out, bring up, speak up, talk over, write up"],
                ["Time/schedule", "put off, hold off, bring forward, drag on"],
            ],
        ),
        note(
            "<p>Particles change meaning: <em>take off</em> (depart / remove / become successful), "
            "<em>make up</em> (invent / reconcile / constitute). Always learn verb + particle as a unit with an example.</p>"
        ),
    ])


def x23():
    return "\n".join([
        h3("Advanced word-order inventory", "p23-extra"),
        rule(
            "Indirect object pronouns",
            "When both objects are pronouns, English prefers DO + to/for + IO.",
            examples_list=[
                "Give it to me. (natural) / Give me it. (heard in some speech, less careful)",
                "Send them to her.",
            ],
            levels=["B1", "B2"],
        ),
        rule(
            "Adverb placement with auxiliaries",
            "Mid-adverbs go after the first auxiliary: <em>She has always preferred… / She will probably join…</em>",
            examples_list=[
                "We have never seen this error.",
                "You must always encrypt tokens at rest.",
                "They are probably deploying now.",
            ],
            mistakes_list=[
                ("We never have seen this.", "We have never seen this.", "Possible for emphasis but marked"),
            ],
            levels=["B1", "B2"],
        ),
        rule(
            "End-weight and information order",
            "English prefers to place heavy/new constituents later. Passives and existential <em>there</em> help.",
            examples_list=[
                "A detailed postmortem written by three engineers was published. (heavy subject — awkward)",
                "There was a detailed postmortem published by three engineers. / A detailed postmortem was published…",
            ],
            levels=["C1", "C2"],
        ),
        rule(
            "Verb–particle–object order",
            "See Part 22. Noun object: optional split. Pronoun object: must split for separable verbs.",
            levels=["B1", "B2"],
        ),
    ])


def x24():
    return "\n".join([
        h3("More emphasis devices", "p24-extra"),
        examples(
            "It is reliability that customers pay for.",
            "What went wrong was the timeout configuration.",
            "The person who approved it was the tech lead. (also focusing)",
            "Do sit down. / I do apologise. (emphatic do)",
            "So carefully did they test that no regressions appeared. (literary/formal)",
            "Away ran the process with all our CPU. (directional fronting — rare/narrative)",
        ),
        rule(
            "Restrictive focusing with clefts vs only",
            "Clefts and <em>only</em> both restrict focus but interact with presupposition differently.",
            examples_list=[
                "Only Maya can approve production changes.",
                "It is Maya who can approve production changes.",
            ],
            levels=["C1"],
        ),
    ])


def x25():
    return "\n".join([
        h3("Cohesion beyond connectives", "p25-extra"),
        ul(
            "Lexical cohesion: repeat key nouns; use controlled synonyms (<em>outage → incident → downtime</em>).",
            "Reference chains: <em>a bug → the bug → it → this issue</em>.",
            "Substitution: <em>do so, one, so/not</em>.",
            "Ellipsis in coordination: <em>We tested the API and [we] fixed three defects</em>.",
            "Parallel structure for lists and comparisons.",
        ),
        rule(
            "Given → new principle",
            "Start with known information; place new information toward the end. This improves readability more than adding adverbs like <em>moreover</em>.",
            examples_list=[
                "We use Redis. It stores session tokens for 24 hours.",
                "Session tokens are stored for 24 hours in Redis. (also fine — choose based on prior sentence)",
            ],
            levels=["B2", "C1", "C2"],
        ),
        warning(
            "<p>Avoid vague <em>this/that</em> without a clear noun: "
            "<span class='wrong'>This caused problems.</span> → "
            "<span class='correct'>This delay caused problems.</span></p>"
        ),
    ])


def x26():
    return "\n".join([
        h3("Comma rules that encode grammar", "p26-extra"),
        ul(
            "Do not join two independent clauses with only a comma (comma splice).",
            "Use commas around non-defining relative clauses and non-essential appositives.",
            "After introductory adverbials: optional for short ones, helpful for long ones.",
            "Serial (Oxford) comma: style choice — be consistent (<em>auth, billing, and search</em>).",
            "No comma after although-clause incorrectly paired with but.",
        ),
        examples(
            "When the build finished, we tagged the release.",
            "Maya, our on-call engineer, responded in three minutes.",
            "We wanted to ship; however, QA found a blocker.",
        ),
        mistakes(
            ("Its a bug.", "It's a bug."),
            ("The engineers's laptops", "The engineers' laptops"),
            ("We can ship, however we should wait.", "We can ship; however, we should wait. / We can ship. However, we should wait."),
        ),
    ])


def x27():
    return "\n".join([
        h3("Channel-based grammar choices", "p27-extra"),
        table(
            ["Channel", "Typical grammar"],
            [
                ["Slack / chat", "fragments, contractions, phrasal verbs, emoji-adjacent brevity"],
                ["Standup speech", "Present Perfect for updates: I've finished X; I'm blocked on Y"],
                ["Email to stakeholders", "full clauses, polite modals, clearer reference"],
                ["RFC / design doc", "nominalizations, passives for process, careful modality (may/should/must)"],
                ["Incident report", "Past Simple narrative + Past Perfect for earlier causes; precise time stamps"],
                ["Academic paper", "impersonal passives, cautious modals (may/might suggest), few contractions"],
            ],
        ),
    ])


def x28():
    return "\n".join([
        h3("More high-frequency mistakes", "p28-extra"),
        mistakes(
            ("I very like it.", "I like it very much."),
            ("How long time…?", "How long…?"),
            ("He doesn't can come.", "He can't come."),
            ("I no understand.", "I don't understand."),
            ("She suggested me to wait.", "She suggested that I wait / suggested waiting."),
            ("We discussed about hiring.", "We discussed hiring."),
            ("According to my opinion", "In my opinion"),
            ("I'm agree", "I agree"),
            ("The meeting will be tomorrow", "fine · also: We have a meeting tomorrow"),
            ("Please do the needful", "Please take the necessary steps / Please handle this.", "South Asian office calque — opaque globally"),
            ("Kindly revert", "Please reply / Please get back to me.", "Revert ≠ reply in standard Int'l English"),
            ("I have a doubt", "I have a question.", "Doubt ≠ question in this context"),
        ),
    ])


def x02():
    return "\n".join([
        h3("Agreement and special noun issues", "p2-extra"),
        table(
            ["Noun", "Agreement / note"],
        [
            ["news / mathematics / physics / economics", "singular verb: The news is…"],
            ["scissors / trousers / glasses / headphones", "plural (a pair of…)"],
            ["police / cattle", "plural"],
            ["the United States / the United Nations", "usually singular verb in modern use"],
            ["data", "plural historically; often singular mass in tech: the data is…"],
            ["criteria / phenomena / analyses", "plurals; singular criterion/phenomenon/analysis"],
            ["staff / team / government", "collective — AmE singular common"],
            ["means / series / species", "same singular/plural form"],
        ],
        ),
        mistakes(
            ("The scissor is sharp.", "The scissors are sharp. / This pair of scissors is sharp."),
            ("This data are… (forced) / These datas", "This data is… / These data are… (choose a system and stay consistent)"),
        ),
    ])


def x03():
    return "\n".join([
        h3("Advanced pronoun reference", "p3-extra"),
        rule(
            "Ambiguity, cataphora, and implied antecedents",
            "Pronouns may point forward (cataphora) in skilled writing, but clarity comes first.",
            examples_list=[
                "When she finally spoke, Maya rejected the proposal. (cataphora — OK if stylistic)",
                "They should update the docs. (Who? Prefer a noun if unclear)",
                "This is frustrating. (Prefer: This delay is frustrating.)",
            ],
            levels=["B2", "C1", "C2"],
        ),
        rule(
            "one as generic pronoun",
            "<span class='register'>FORMAL</span> Especially BrE academic: <em>One should save one's work.</em> "
            "AmE often finds this stiff; prefer <em>you</em> or rephrase.",
            levels=["C1"],
        ),
    ])


def x09():
    return "\n".join([
        h3("Light verbs and collocations", "p9-extra"),
        p("English often uses light verbs <em>make, take, have, do, give</em> + noun instead of a single verb."),
        table(
            ["Light verb pattern", "Near-synonym"],
            [
                ["make a decision", "decide"],
                ["make an improvement", "improve"],
                ["take a break", "break (verb)"],
                ["take responsibility", "—"],
                ["have a meeting / look / shower", "meet / look / shower"],
                ["do research / damage", "research / damage (verbs)"],
                ["give a presentation / permission", "present / permit"],
            ],
        ),
        note("<p>These are collocations — translating word-by-word often fails (<em>do a decision</em>).</p>"),
    ])


def x01():
    return "\n".join([
        h3("Finite clauses need tense marking", "p1-extra"),
        p("Every full declarative/interrogative sentence needs a finite verb (tense-marked), except imperatives with an implied <em>you</em>."),
        examples(
            "Ship the fix. (imperative — subject understood)",
            "Please be careful with production credentials.",
            "It is essential that she be present. (subjunctive — advanced; see formal AmE/BrE)",
        ),
        rule(
            "Complement vs object — quick test",
            "If you can turn the sentence into a passive with the same noun as subject, it was likely an object: "
            "<em>They fixed the bug → The bug was fixed</em>. Subject complements do not passivise that way: "
            "<em>She became lead</em> ↛ <em>*Lead was become by her</em>.",
            levels=["B1", "B2"],
        ),
        table(
            ["Pattern", "Label", "Example"],
            [
                ["S V", "intransitive", "Costs rose."],
                ["S V O", "monotransitive", "We fixed the bug."],
                ["S V C", "linking", "The fix was incomplete."],
                ["S V IO DO", "ditransitive", "She sent us logs."],
                ["S V O C", "complex-transitive", "They appointed her lead."],
                ["S V O A", "object + adverbial", "She put the key on the vault."],
            ],
        ),
    ])


def x10():
    return "\n".join([
        h3("Tense choice workshops", "p10-extra"),
        table(
            ["Situation", "Prefer", "Avoid / less natural"],
            [
                ["Life experience, no time", "Present Perfect: Have you used Rust?", "Did you use Rust? (needs time or sounds finished-story)"],
                ["Finished time named", "Past Simple: I saw it yesterday.", "I have seen it yesterday."],
                ["Duration to now", "Perfect (cont.): I have been waiting for an hour.", "I am waiting for an hour."],
                ["Habit now", "Present Simple: We deploy on Thursdays.", "We are deploying on Thursdays. (unless temporary)"],
                ["Arrangement", "Present Continuous: I am meeting them at 3.", "I will meet them at 3. (possible, less arrangement-like)"],
                ["Evidence-based prediction", "going to: It is going to crash.", "will crash (possible as opinion)"],
                ["Offer/decision now", "will: I will handle it.", "I am going to handle it. (sounds pre-planned)"],
                ["Earlier past in a story", "Past Perfect when order unclear", "Past Simple if sequence words already clarify"],
            ],
        ),
        rule(
            "State vs habit with for/since",
            "With stative verbs, Present Perfect Simple is preferred: <em>I have known her for years</em> "
            "(not usually <em>have been knowing</em>). With dynamic verbs, both simple and continuous perfects occur, "
            "with continuous highlighting activity/duration.",
            levels=["B1", "B2"],
        ),
        note(
            "<p><strong>American vs British:</strong> AmE uses Past Simple more freely with <em>already/yet/just</em>: "
            "<em>Did you eat yet?</em> BrE strongly prefers Present Perfect: <em>Have you eaten yet?</em> "
            "Both are widely understood.</p>"
        ),
    ])


def x21():
    return "\n".join([
        h3("Causative vs passive vs reflexive", "p21-extra"),
        compare(
            "<p><em>My phone was repaired</em> — fact (agent unknown/unimportant).<br>"
            "<em>I had my phone repaired</em> — I arranged the service.<br>"
            "<em>I repaired my phone</em> — I did it myself.<br>"
            "<em>I got my phone repaired</em> — similar to have; often more informal.</p>"
        ),
        examples(
            "The company had all laptops encrypted before the audit.",
            "We got the contractor to rewrite the scraper.",
            "Do not make the intern deploy alone on day one.",
            "Let the build finish before you cancel it.",
        ),
    ])


def x29():
    return "\n".join([
        h3("More confusing pairs", "p29-extra"),
        table(
            ["Pair", "Difference", "Example"],
            [
                ["in time vs on time", "in time = before too late; on time = punctual schedule", "We arrived in time to stop it. / The train is on time."],
                ["at the end vs in the end", "at the end = at the finishing point; in the end = finally", "At the end of the call… / In the end we rolled back."],
                ["beside vs besides", "next to vs in addition", "beside the desk / besides the cost"],
                ["interested vs interesting", "experiencer vs cause", "I am interested / The talk is interesting"],
                ["classic vs classical", "iconic/typical vs arts-historical", "a classic bug / classical music"],
                ["principal vs principle", "main / school head vs moral rule", "principal engineer / a principle"],
                ["complement vs compliment", "complete vs praise", "subject complement / nice compliment"],
                ["ensure vs insure vs assure", "make certain / insurance / reassure someone", "ensure backups; insure a car; assure the client"],
                ["imply vs infer", "speaker hints / listener concludes", "The email implies… / We inferred…"],
                ["replace with vs by", "with = new thing; by = agent often", "replace Redis with Memcached"],
                ["Rob vs steal", "rob a person/place; steal a thing", "rob a bank / steal a laptop"],
                ["say vs tell vs talk vs speak", "see earlier + Part 15", "tell someone; say something; talk to; speak Arabic"],
                ["wait vs await", "wait for + NP; await + NP (formal, no for)", "wait for approval / await approval"],
                ["price vs prize vs worth", "cost / award / value", "price tag / prize / worth doing"],
            ],
        ),
    ])


def x30():
    return "\n".join([
        h3("Ellipsis and fragments that sound native", "p30-extra"),
        examples(
            "<span class='register'>SPOKEN</span> Ready? — Almost.",
            "<span class='register'>SPOKEN</span> Coffee? — Please.",
            "<span class='register'>SPOKEN</span> Serves me right for skipping tests.",
            "<span class='register'>INFORMAL</span> Long story short, we rolled back.",
            "<span class='register'>STANDARD</span> Looking forward to your feedback.",
            "<span class='register'>FORMAL</span> Please find attached the revised proposal.",
        ),
        note(
            "<p>Native speakers omit recoverable subjects/auxiliaries in notes and chat. "
            "In essays, interviews, and documentation, write full clauses unless the genre expects brevity.</p>"
        ),
    ])
