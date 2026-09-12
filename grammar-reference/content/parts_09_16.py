"""Parts 9–16: Verbs through Questions."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, advanced, table, badge, box
)


def part_09():
    s = []
    s.append(part_header(9, "Verbs",
        "Verbs express actions, states, and relations. This part covers verb classes that affect grammar: "
        "auxiliaries, linking verbs, stative vs dynamic verbs, regular/irregular forms, and multi-word verbs (preview)."))

    s.append(h3("Main verbs, auxiliaries, modals", "p9-classes"))
    s.append(table(
        ["Class", "Role", "Examples"],
        [
            ["Main verb", "Lexical meaning", "deploy, decide, need, write"],
            ["Primary auxiliaries", "tense/aspect/voice/questions/negation", "be, have, do"],
            ["Modal auxiliaries", "stance: ability, obligation, probability…", "can, could, may, might, must, shall, should, will, would"],
            ["Semi-modals / modal-like", "similar meanings with fuller verb behaviour", "have to, need to, ought to, be going to, be able to, used to"],
        ],
    ))

    s.append(h3("Stative vs dynamic verbs", "p9-stative"))
    s.append(rule(
        "Stative verbs",
        "Stative verbs describe states (not actions): mental states, emotions, possession, senses, and some relating verbs. "
        "They are not normally used in continuous (-ing) forms when they keep a stative meaning.",
        when=[
            "Cognition: know, believe, understand, remember, forget, mean, realise, suppose, agree, disagree, doubt",
            "Emotion/preference: like, love, hate, prefer, want, need, wish",
            "Possession/relation: have (possession), own, belong, include, contain, consist of, seem, appear, look (=seem), sound, resemble",
            "Senses (involuntary): hear, see, smell, taste (when not deliberate actions)",
        ],
        examples_list=[
            "I agree with the estimate. <span class='correct'>NOT</span> I am agree. / I am agreeing. (usually)",
            "She knows Kubernetes well.",
            "This repo belongs to the platform team.",
            "The plan seems solid.",
        ],
        mistakes_list=[
            ("I am agree.", "I agree.", "Agree is stative; also never <em>am agree</em> — missing adjective/verb form."),
            ("I am knowing the answer.", "I know the answer."),
            ("She is wanting a new laptop.", "She wants a new laptop."),
        ],
        levels=["A2", "B1", "B2"],
    ))
    s.append(advanced(
        "<p>Some normally stative verbs become dynamic when they describe temporary behaviour or deliberate actions:</p>"
        "<ul>"
        "<li><em>I'm seeing the client at 3</em> (meeting) vs <em>I see what you mean</em> (understand).</li>"
        "<li><em>He's having a meeting / having lunch</em> vs <em>He has two laptops</em>.</li>"
        "<li><em>I'm loving this new IDE</em> <span class='register'>INFORMAL</span> advertising style — still marked.</li>"
        "<li><em>What are you thinking about?</em> (active mental process) vs <em>I think you're right</em> (opinion).</li>"
        "</ul>"
    ))

    s.append(h3("Transitivity and linking", "p9-trans"))
    s.append(p("See Part 1 for patterns. Remember: linking verbs take complements (adjectives/nouns), not adverbs of manner."))
    s.append(mistakes(
        ("The design looks well.", "The design looks good.", "Unless referring to eyesight ability."),
        ("She became angrily.", "She became angry."),
    ))

    s.append(h3("Regular and irregular verbs", "p9-forms"))
    s.append(p(
        "Regular verbs form past and past participle with <em>-ed</em> (<em>deploy–deployed–deployed</em>). "
        "Irregular verbs must be memorised. A practical irregular list is in Part 32."
    ))
    s.append(table(
        ["Base", "Past simple", "Past participle", "Note"],
        [
            ["be", "was/were", "been", "auxiliary + main"],
            ["have", "had", "had", ""],
            ["do", "did", "done", ""],
            ["go", "went", "gone", ""],
            ["write", "wrote", "written", ""],
            ["speak", "spoke", "spoken", ""],
            ["break", "broke", "broken", ""],
            ["choose", "chose", "chosen", ""],
            ["lead", "led", "led", "not <em>lead</em> in past"],
            ["read", "read /red/", "read /red/", "spelling same"],
            ["set", "set", "set", "unchanging"],
            ["put", "put", "put", ""],
            ["build", "built", "built", ""],
            ["send", "sent", "sent", ""],
            ["feel", "felt", "felt", ""],
            ["think", "thought", "thought", ""],
            ["bring", "brought", "brought", ""],
            ["buy", "bought", "bought", ""],
            ["catch", "caught", "caught", ""],
            ["teach", "taught", "taught", ""],
            ["leave", "left", "left", ""],
            ["meet", "met", "met", ""],
            ["pay", "paid", "paid", ""],
            ["say", "said", "said", ""],
            ["tell", "told", "told", ""],
            ["win", "won", "won", ""],
            ["lose", "lost", "lost", ""],
            ["lie (recline)", "lay", "lain", "vs lay–laid–laid"],
            ["lay (put)", "laid", "laid", "needs object"],
            ["rise", "rose", "risen", "intransitive"],
            ["raise", "raised", "raised", "transitive"],
        ],
        caption="High-frequency irregular verbs (sample)",
    ))

    s.append(h3("Phrasal and causative verbs (preview)", "p9-preview"))
    s.append(p("Phrasal verbs: Part 22. Causatives (<em>have/get/make/let</em>): Part 21. Modals: Part 11."))
    s.append(part_footer())
    return "\n".join(s)


def _tense_block(name, levels, structure, uses, pos, neg, q, time_expr, ex, mistakes_list, compare_html="", spoken=""):
    bits = [f'<div class="rule-block" id="tense-{name.lower().replace(" ", "-")}">',
            f'<div class="rule-head"><h4>{name}</h4>{badge(*levels)}</div>',
            f'<p class="label">Structure</p><p class="form-pattern">{structure}</p>',
            '<p class="label">Positive / Negative / Question</p>',
            table(["+", "−", "?"], [[pos, neg, q]]),
            '<p class="label">Main uses</p>', ul(*uses),
            '<p class="label">Common time expressions</p>', p(time_expr)]
    bits.append(examples(*ex))
    bits.append(mistakes(*mistakes_list))
    if compare_html:
        bits.append(compare(compare_html))
    if spoken:
        bits.append(note(spoken, "Spoken / register"))
    bits.append("</div>")
    return "\n".join(bits)


def part_10():
    s = []
    s.append(part_header(10, "Complete Tense System",
        "English tense–aspect combinations encode time and viewpoint (simple, continuous, perfect, perfect continuous). "
        "For every form below: structure, polarity, uses, time expressions, mistakes, and comparisons."))

    s.append(h3("Present", "p10-present"))
    s.append(_tense_block(
        "Present Simple", ["A1", "A2", "B1"],
        "V / V-s (he/she/it) · do/does + not + V · Do/Does + S + V?",
        ["Habits and routines", "General truths and facts", "Permanent situations",
         "Scheduled future (timetables)", "Narration in reviews/instructions (sometimes)",
         "Stative verbs in present time"],
        "She works remotely.", "She does not (doesn't) work remotely.", "Does she work remotely?",
        "every day, usually, often, on Mondays, always, never, nowadays (with care)",
        ["Water boils at 100°C.", "We deploy on Thursdays.", "The train leaves at 6:40.", "I agree."],
        [("He work here.", "He works here."),
         ("She doesn't works.", "She doesn't work."),
         ("Does she works?", "Does she work?")],
        "Present Continuous = temporary/happening now; Present Simple = habit/fact/schedule.",
        "<p>In speech, <em>don't/doesn't</em> are normal. Third-person <em>-s</em> is a persistent learner error.</p>",
    ))
    s.append(_tense_block(
        "Present Continuous", ["A1", "A2", "B1"],
        "am/is/are + V-ing",
        ["Actions happening now / around now", "Temporary situations", "Developing trends",
         "Future arrangements (personal plans with time/place)", "Annoying habits with always"],
        "They are testing the API.", "They are not testing the API.", "Are they testing the API?",
        "now, at the moment, currently, this week, today, Look!, these days",
        ["I am writing the postmortem.", "She is staying with a friend this month.",
         "More teams are adopting Rust.", "We are meeting the client tomorrow at 10.",
         "He is always interrupting standups."],
        [("I am agree.", "I agree."),
         ("She working now.", "She is working now."),
         ("They are wanting a raise.", "They want a raise. (stative)")],
        "Future: Present Continuous = arrangement; <em>going to</em> = intention/evidence; <em>will</em> = decision/prediction.",
    ))
    s.append(_tense_block(
        "Present Perfect", ["A2", "B1", "B2"],
        "have/has + past participle",
        ["Past action with present relevance (unspecified time)", "Life experience (ever/never)",
         "Unfinished time periods (today, this week)", "Change over time",
         "With for/since for continuing states (esp. BrE)", "News / recent events (just, already, yet)"],
        "We have shipped the fix.", "We have not shipped the fix.", "Have we shipped the fix?",
        "ever, never, already, yet, just, recently, so far, for, since, this week, today",
        ["I have used this framework before.", "She has already merged the PR.",
         "Have you finished the estimate yet?", "They have lived in Berlin since 2019.",
         "Sales have increased this quarter."],
        [("I have seen him yesterday.", "I saw him yesterday.", "Specific finished past time → Past Simple"),
         ("She has went.", "She has gone."),
         ("I am here since 2020.", "I have been here since 2020.")],
        "AmE often uses Past Simple where BrE prefers Present Perfect for recent news: "
        "<em>Did you eat yet?</em> (AmE) vs <em>Have you eaten yet?</em> (BrE).",
    ))
    s.append(_tense_block(
        "Present Perfect Continuous", ["B1", "B2"],
        "have/has been + V-ing",
        ["Duration of an activity up to now (focus on activity)", "Recently finished activities with present evidence",
         "Repeated activities in a period up to now"],
        "She has been debugging for hours.", "She hasn't been debugging…", "Has she been debugging…?",
        "for, since, all day, lately, recently",
        ["We have been waiting for the approval all morning.",
         "Your eyes are red — have you been staring at logs again?",
         "I have been learning Go this year."],
        [("I have been knowing her for years.", "I have known her for years.", "Stative → perfect simple"),
         ("She is working here for five years.", "She has been working / has worked here for five years.")],
        "Perfect simple often focuses on result/completion; continuous on duration/activity. "
        "Both possible: <em>I have lived / have been living here for years</em>.",
    ))

    s.append(h3("Past", "p10-past"))
    s.append(_tense_block(
        "Past Simple", ["A1", "A2", "B1"],
        "V-ed / irregular · did not + V · Did + S + V?",
        ["Completed actions at a specific past time", "Sequences of past events", "Past habits (also used to)",
         "Narrative storytelling"],
        "They deployed at midnight.", "They did not deploy…", "Did they deploy…?",
        "yesterday, last week, in 2021, ago, when, then, that day",
        ["We launched the product last March.", "I called her, explained the issue, and hung up."],
        [("Did you went?", "Did you go?"), ("I didn't went.", "I didn't go.")],
    ))
    s.append(_tense_block(
        "Past Continuous", ["A2", "B1"],
        "was/were + V-ing",
        ["Action in progress at a past moment", "Background to a past event", "Two parallel past actions",
         "Polite past: <em>I was wondering if…</em>"],
        "I was writing the RFC.", "I wasn't writing…", "Were you writing…?",
        "at 8 p.m., while, when, as",
        ["At 9:15 the server was restarting.", "I was reviewing the PR when Slack crashed.",
         "While she was presenting, I was taking notes."],
        [("When I walked in, he worked.", "When I walked in, he was working.", "Background → continuous")],
    ))
    s.append(_tense_block(
        "Past Perfect", ["B1", "B2"],
        "had + past participle",
        ["An earlier past before another past", "Reported speech backshift", "Conditional type 3 / mixed",
         "With already, just, never, by the time"],
        "They had already left.", "They hadn't left.", "Had they left?",
        "before, after, by the time, already, just, never, until then",
        ["By the time we arrived, the meeting had started.",
         "I realised I had forgotten the token."],
        [("After I have finished, I went home.", "After I had finished, I went home.")],
        "Do not use Past Perfect for every past story — only when the earlier-past relationship matters.",
    ))
    s.append(_tense_block(
        "Past Perfect Continuous", ["B2", "C1"],
        "had been + V-ing",
        ["Duration of an activity before a past point", "Cause of a past result"],
        "She had been coding all night.", "…hadn't been coding…", "Had she been coding…?",
        "for, since, before, all night",
        ["He was tired because he had been on-call all weekend.",
         "They had been negotiating for months before they signed."],
        [("I was working there for five years before I left.", "I had been working / had worked there for five years before I left.")],
    ))

    s.append(h3("Future", "p10-future"))
    s.append(_tense_block(
        "Will future", ["A2", "B1"],
        "will + V (won't) · Will + S + V?",
        ["Instant decisions", "Promises, offers, refusals", "Predictions (opinion)", "Facts about the future"],
        "I will handle the rollback.", "I won't handle…", "Will you handle…?",
        "I think, probably, I'm sure, tomorrow (with prediction)",
        ["The phone's ringing — I'll get it.", "We'll send the invoice today.", "I think the release will slip."],
        [("I will to help.", "I will help.")],
    ))
    s.append(_tense_block(
        "Be going to", ["A2", "B1"],
        "am/is/are going to + V",
        ["Prior intentions/plans", "Predictions based on present evidence"],
        "We are going to refactor the auth module.", "…aren't going to…", "Are you going to…?",
        "tomorrow, next week, tonight",
        ["I'm going to ask for a raise.", "Look at those logs — it's going to fail."],
        [("I going to deploy.", "I'm going to deploy.")],
        "<em>will</em> vs <em>going to</em>: decision-now vs planned; pure opinion vs evidence.",
    ))
    s.append(_tense_block(
        "Present Continuous for future", ["A2", "B1"],
        "am/is/are + V-ing (+ future time)",
        ["Fixed personal arrangements (often with time/place/people)"],
        "I'm flying to Dubai on Monday.", "I'm not flying…", "Are you flying…?",
        "tomorrow, on Monday, at 3, next week",
        ["We're interviewing two candidates tomorrow."],
        [("I meet him tomorrow at 5. (possible but weaker)", "I'm meeting him tomorrow at 5.", "Arrangement → continuous")],
    ))
    s.append(_tense_block(
        "Present Simple for schedules", ["A2", "B1"],
        "V / V-s + future time",
        ["Timetables and fixed schedules (public/institutional)"],
        "The webinar starts at 18:00.", "…doesn't start…", "Does it start…?",
        "at 6, on Friday, tomorrow morning",
        ["Our sprint ends on Thursday.", "The flight leaves at dawn."],
        [],
    ))
    s.append(_tense_block(
        "Future Continuous", ["B1", "B2"],
        "will be + V-ing",
        ["Action in progress at a future moment", "Polite enquiries about plans", "Expected/normal future activity"],
        "This time tomorrow I'll be travelling.", "…won't be travelling.", "Will you be travelling?",
        "this time tomorrow, at 8 p.m., when…",
        ["Don't call at 7 — I'll be putting the kids to bed.",
         "Will you be using the conference room at noon?"],
        [],
    ))
    s.append(_tense_block(
        "Future Perfect", ["B2", "C1"],
        "will have + past participle",
        ["Completed before a future deadline/point"],
        "By Friday we will have finished the migration.", "…won't have finished…", "Will you have finished…?",
        "by this time next week, by 2030, before…",
        ["By the time you arrive, I will have prepared the demo."],
        [],
    ))
    s.append(_tense_block(
        "Future Perfect Continuous", ["C1", "C2"],
        "will have been + V-ing",
        ["Duration up to a future point (often with for)"],
        "In March I will have been working here for five years.", "…", "…",
        "by… for…",
        ["Next month we'll have been negotiating for a year."],
        [],
    ))

    s.append(h3("Future in the past & time clauses", "p10-future-past"))
    s.append(rule(
        "Future in the past",
        "To talk about a future seen from a past viewpoint, English uses past forms of future markers.",
        examples_list=[
            "I knew it would fail.",
            "We were going to launch in May, but we delayed.",
            "She would have joined us if her flight had landed.",
            "The roadmap said we would migrate in Q3.",
        ],
        levels=["B2", "C1"],
    ))
    s.append(rule(
        "Future time clauses (no will after when/after/until…)",
        "In clauses with <em>when, after, before, as soon as, until, while, once, if</em> referring to the future, "
        "use present (or present perfect) — not <em>will</em>.",
        examples_list=[
            "I'll message you when the build finishes. (not <em>will finish</em>)",
            "After we have merged, we can tag a release.",
            "Wait until the tests pass.",
        ],
        mistakes_list=[
            ("I'll call you when I will arrive.", "I'll call you when I arrive."),
        ],
        levels=["B1", "B2"],
    ))
    s.append(rule(
        "Sequence of tenses (overview)",
        "In reported speech and subordinate clauses, verb forms often shift relative to a past reporting verb "
        "(see Part 15). Keep relationships of time clear: earlier past → past perfect; same past time → past simple/continuous.",
        levels=["B2", "C1"],
    ))

    s.append(h3("Master tense comparison", "p10-master"))
    s.append(table(
        ["Form", "Core idea", "Typical signal"],
        [
            ["Present Simple", "habit / fact / schedule", "every day, usually"],
            ["Present Continuous", "now / temporary / arrangement", "now, this week, tomorrow (plan)"],
            ["Present Perfect", "past → present relevance", "ever, already, since, yet"],
            ["Present Perfect Continuous", "duration/activity → now", "for hours, lately"],
            ["Past Simple", "finished past time", "yesterday, ago, in 2020"],
            ["Past Continuous", "past in-progress", "at 8, while"],
            ["Past Perfect", "earlier than past", "before, by the time"],
            ["will", "decision / prediction / promise", "I think, I'll…"],
            ["going to", "intention / evidence", "I'm going to…, Look!"],
            ["Future Perfect", "done before future point", "by Friday"],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_11():
    s = []
    s.append(part_header(11, "Modal Verbs",
        "Modals express ability, permission, obligation, advice, probability, and interpersonal meanings "
        "(requests, offers, criticism). They have no -s in the third person, take a bare infinitive, and form questions/negatives without do."))

    s.append(rule(
        "Core modal form rules",
        "Modals are defective verbs: no infinitive (*to can), no participles (*canning as modal), no do-support.",
        form="Modal + bare infinitive · Modal + not · Modal + subject + bare infinitive?",
        examples_list=[
            "She can ship today. / She can't ship today. / Can she ship today?",
            "He must be joking. (not <em>musts</em>, not <em>must to be</em>)",
        ],
        mistakes_list=[
            ("She cans swim.", "She can swim."),
            ("You must to go.", "You must go."),
            ("Do you can help?", "Can you help?"),
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(h3("Meanings by function", "p11-meanings"))
    s.append(table(
        ["Function", "Common modals", "Examples"],
        [
            ["Ability", "can, could, be able to", "She can write SQL. / I could swim as a child. / I wasn't able to join."],
            ["Permission", "can, could, may (formal)", "Can I leave early? / May I interrupt?"],
            ["Obligation", "must, have to, need to", "You must rotate keys. / I have to be on-call."],
            ["Prohibition", "mustn't, can't, may not", "You mustn't commit secrets."],
            ["No obligation", "don't have to, needn't", "You don't have to attend."],
            ["Advice", "should, ought to, had better", "You should add tests."],
            ["Probability / deduction", "must, might, may, could, can't", "She must be offline. / It can't be true."],
            ["Prediction", "will, should, may, might", "It should be fine. / It might rain."],
            ["Willingness / offers", "will, shall (BrE), can", "I'll help. / Shall I open a ticket?"],
            ["Requests", "can, could, will, would", "Could you review this?"],
            ["Habit (past)", "would, used to", "He would always refactor on Fridays."],
            ["Criticism / regret", "should have, could have, might have", "You should have backed up first."],
        ],
    ))

    s.append(h3("Key contrasts", "p11-contrast"))
    s.append(compare(
        "<p><strong>must vs have to:</strong> Both obligation. <em>must</em> often = speaker authority/internal; "
        "<em>have to</em> = external rule. In AmE <em>have to</em> is very common. Past obligation: <em>had to</em> (not <em>musted</em>). "
        "Deduction: <em>must</em> = almost certain; prohibition: <em>mustn't</em> ≠ <em>don't have to</em>.</p>"
        "<p><strong>should vs ought to:</strong> Near synonyms; <em>ought to</em> slightly more formal/less common in AmE speech.</p>"
        "<p><strong>can vs could:</strong> ability now vs past/ability or more polite requests; also possibility.</p>"
        "<p><strong>may vs might:</strong> both possibility; <em>might</em> often slightly less likely / more tentative; "
        "<em>may</em> also formal permission.</p>"
        "<p><strong>will vs would:</strong> future/willingness vs past future, hypothetical, or more polite softener.</p>"
    ))

    s.append(rule(
        "Semi-modals",
        "<em>have to, need to, ought to, be able to, be supposed to, had better, used to</em> fill gaps modals cannot "
        "(e.g. infinitives, tense marking).",
        examples_list=[
            "We had to postpone. / We'll have to postpone.",
            "You'd better encrypt that file. (strong advice; spoken)",
            "I'm supposed to join the governance call.",
            "I used to write PHP. (past habit — ended)",
            "She was able to recover the data.",
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(h3("Modal perfects (advanced)", "p11-perfect"))
    s.append(table(
        ["Form", "Typical meaning", "Example"],
        [
            ["must have + PP", "strong deduction about past", "The cache must have expired."],
            ["might/may have + PP", "possible past", "She might have missed the ping."],
            ["could have + PP", "possible past / criticism / ability unused", "We could have shipped earlier."],
            ["can't/couldn't have + PP", "impossibility in past", "He can't have finished already."],
            ["should have + PP", "regret / criticism", "You should have asked sooner."],
            ["would have + PP", "hypothetical past result", "I would have joined if I'd known."],
            ["needn't have + PP", "did something unnecessary (BrE)", "You needn't have printed everything."],
            ["didn't need to", "wasn't necessary (may or may not have done)", "I didn't need to print anything."],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_12():
    s = []
    s.append(part_header(12, "Gerunds & Infinitives",
        "English verbs select gerunds (<em>-ing</em>), to-infinitives, or bare infinitives. "
        "Some verbs change meaning depending on the pattern. Learn high-value contrasts as pairs."))

    s.append(rule(
        "Forms",
        "Gerund = verb + -ing used as a noun. To-infinitive = to + base verb. Bare infinitive = base verb after modals, "
        "make/let, help (optional to), sense verbs, and some patterns.",
        examples_list=[
            "Debugging calms me. (gerund subject)",
            "To err is human. (infinitive subject — formal)",
            "She wants to leave. / She enjoys leaving early on Fridays.",
            "Let me explain. / I saw him leave.",
        ],
        levels=["A2", "B1"],
    ))

    s.append(h3("Verb pattern groups", "p12-groups"))
    s.append(table(
        ["Pattern", "Common verbs"],
        [
            ["verb + gerund", "enjoy, finish, avoid, consider, suggest, mind, keep, miss, practise, risk, admit, deny, involve, delay, postpone, give up, put off"],
            ["verb + to-infinitive", "want, need, hope, plan, decide, agree, refuse, promise, offer, learn, afford, manage, fail, arrange, expect, intend"],
            ["verb + object + to-infinitive", "ask, tell, want, expect, advise, encourage, persuade, remind, force, teach, allow, enable"],
            ["verb + bare infinitive", "modals; make, let; (help); see/hear/watch + action complete"],
            ["verb + object + gerund", "catch, find, leave, mind (Do you mind me opening…?)"],
            ["adjective + to-infinitive", "happy to, ready to, likely to, easy to, important to"],
            ["noun + to-infinitive", "a plan to, a decision to, a chance to, permission to"],
            ["preposition + gerund", "interested in learning; instead of waiting; look forward to meeting"],
        ],
    ))

    s.append(h3("Meaning-changing pairs", "p12-pairs"))
    s.append(table(
        ["Pair", "Meaning A", "Meaning B"],
        [
            ["stop doing / stop to do", "end an activity", "pause in order to do something"],
            ["remember doing / to do", "memory of past action", "not forget a duty"],
            ["forget doing / to do", "not recall past action (rare)", "fail to do a duty"],
            ["try doing / to do", "experiment with a method", "attempt (effort/difficulty)"],
            ["regret doing / to do", "sorry about past", "sorry to give bad news (formal)"],
            ["mean doing / to do", "involve / imply", "intend"],
            ["go on doing / to do", "continue same action", "move on to next topic/stage"],
            ["need doing / to do", "passive sense: needs to be done", "require (active)"],
            ["like doing / to do", "enjoy (general)", "choose/prefer as habit or specific occasion (esp. BrE nuance)"],
            ["afraid of doing / to do", "worry about possible result", "don't want to do (unwillingness)"],
        ],
    ))
    s.append(examples(
        "She stopped debugging. / She stopped to take a call.",
        "I remember locking the door. / Remember to lock the door.",
        "Try restarting the service. / I tried to restart it, but I lacked permissions.",
        "I regret saying that. / We regret to inform you that your application was unsuccessful.",
        "The policy means working weekends. / I meant to email you.",
        "She went on talking. / She went on to talk about hiring.",
        "The server needs restarting. / I need to restart the server.",
    ))

    s.append(mistakes(
        ("I look forward to meet you.", "I look forward to meeting you.", "<em>to</em> is a preposition here."),
        ("I suggest to go.", "I suggest going. / I suggest that we go."),
        ("She made me to apologise.", "She made me apologise."),
        ("Let me to help.", "Let me help."),
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_13():
    s = []
    s.append(part_header(13, "Conditionals",
        "Conditionals express real and unreal situations across time. Beyond the classic 0–3 types, English uses "
        "mixed conditionals, inverted forms, and a family of conditional conjunctions."))

    s.append(table(
        ["Type", "If-clause", "Main clause", "Use"],
        [
            ["Zero", "present", "present", "general truths / automatic results"],
            ["First", "present", "will / modal / imperative", "real future possibility"],
            ["Second", "past simple", "would/could/might + V", "unreal present/future"],
            ["Third", "past perfect", "would have + PP", "unreal past"],
            ["Mixed", "various", "various", "past condition → present result (etc.)"],
        ],
        caption="Classic conditional patterns",
    ))

    s.append(examples(
        "Zero: If you heat ice, it melts. / If the tests fail, the pipeline stops.",
        "First: If we merge today, we'll ship tomorrow. / If you see a 500, open a ticket.",
        "Second: If I had more time, I would rewrite the module. / If she were free, she could join. "
        "(Were is formal/subjunctive; was is common in speech.)",
        "Third: If we had backed up, we wouldn't have lost data.",
        "Mixed: If I had taken that job, I would be in Berlin now.",
        "Mixed: If she knew Docker, she would have fixed it yesterday. (less common; present state → past result)",
    ))

    s.append(rule(
        "unless / provided / as long as / in case / even if / only if",
        "These introduce conditions with nuance.",
        examples_list=[
            "Unless we get approval, we can't launch. (= if we do not)",
            "Provided (that) / Providing (that) the tests pass, we deploy.",
            "As long as the API stays stable, clients won't notice.",
            "Take an umbrella in case it rains. (precaution — not the same as if)",
            "Even if we rush, we won't finish tonight. (concession)",
            "Only if we get two approvals can we proceed. (restrictive; may trigger inversion)",
        ],
        levels=["B1", "B2", "C1"],
    ))

    s.append(rule(
        "wish / if only",
        "Wish about present: past simple. Wish about past: past perfect. Wish about annoying habits: would. "
        "Wish + would not for first-person ability wishes (*I wish I would… is usually wrong).",
        examples_list=[
            "I wish we had better monitoring. (present unreal)",
            "I wish I had asked sooner. (past regret)",
            "I wish the alert would stop firing. (others' behaviour)",
            "If only we had known!",
        ],
        mistakes_list=[
            ("I wish I will have more time.", "I wish I had more time."),
            ("I wish I would be taller.", "I wish I were / was taller."),
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Inverted conditionals (formal)",
        "In formal/written English, <em>if</em> can be omitted with inversion: "
        "<em>Had I known…, Were I…, Should you need…</em>",
        examples_list=[
            "Had I known about the outage, I would have joined earlier.",
            "Were I you, I'd postpone the release. (formal)",
            "Should you need help, ping me on Slack.",
            "Were it not for the backup, we would have lost everything.",
        ],
        levels=["C1", "C2"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_14():
    s = []
    s.append(part_header(14, "Passive Voice",
        "Passive voice makes the object of an active clause into the subject. Use it when the doer is unknown, obvious, "
        "or less important — or to control information flow. Overuse sounds bureaucratic."))

    s.append(rule(
        "Basic form",
        "Passive = form of <em>be</em> + past participle (+ by-agent optional).",
        form="Active: S + V + O → Passive: O + be + V-ed (+ by S)",
        examples_list=[
            "Active: The team fixed the bug.",
            "Passive: The bug was fixed (by the team).",
        ],
        levels=["A2", "B1"],
    ))

    s.append(table(
        ["Tense / form", "Passive example"],
        [
            ["Present Simple", "Tickets are triaged daily."],
            ["Present Continuous", "The feature is being tested."],
            ["Present Perfect", "The keys have been rotated."],
            ["Past Simple", "The outage was caused by a bad config."],
            ["Past Continuous", "The system was being upgraded."],
            ["Past Perfect", "The patch had been applied."],
            ["will", "The results will be announced tomorrow."],
            ["going to", "The servers are going to be replaced."],
            ["Modal", "The data must be encrypted. / It can be deferred."],
            ["Modal perfect", "The email might have been deleted."],
        ],
        caption="Passive across major forms",
    ))

    s.append(rule(
        "Get-passive",
        "<em>get</em> + past participle is common in informal English for events (often adverse or change-of-state).",
        examples_list=[
            "Our staging site got hacked. <span class='register'>INFORMAL</span>",
            "She got promoted last year.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Passive with two objects",
        "Either object can usually become the subject: <em>I was sent a link</em> / <em>A link was sent to me</em>.",
        examples_list=[
            "They offered her a role. → She was offered a role. / A role was offered to her.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Reporting / impersonal passive",
        "Common in news and academic style to report beliefs without naming a source.",
        examples_list=[
            "It is believed that the leak came from a vendor.",
            "The CEO is said to be stepping down.",
            "He is believed to have resigned.",
            "It was reported that latency spiked overnight.",
        ],
        levels=["B2", "C1"],
    ))

    s.append(rule(
        "Causative passive (preview)",
        "<em>have/get something done</em> = arrange for someone else to do it (Part 21).",
        examples_list=["We had the servers upgraded. / I need to get my laptop repaired."],
        levels=["B1", "B2"],
    ))

    s.append(compare(
        "<p>Prefer active when the agent matters: <em>Maya designed the API</em> (clear credit).<br>"
        "Prefer passive when the patient/theme matters: <em>The API was redesigned last quarter</em>.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_15():
    s = []
    s.append(part_header(15, "Reported Speech",
        "Reported (indirect) speech restates what someone said without quoting verbatim. "
        "Changes may affect tense, pronouns, and time/place words — but backshift is not always required."))

    s.append(rule(
        "Reported statements",
        "Common pattern: reporting verb + (that) + clause. After a past reporting verb, tenses often shift one step back.",
        form="She said (that) + clause · She told me (that) + clause",
        examples_list=[
            "Direct: \"I am deploying now.\" → She said she was deploying then.",
            "\"We have finished.\" → They said they had finished.",
            "\"I will join later.\" → He said he would join later.",
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(table(
        ["Direct", "Often becomes"],
        [
            ["present simple", "past simple"],
            ["present continuous", "past continuous"],
            ["present perfect", "past perfect"],
            ["past simple", "past perfect (or stays past simple)"],
            ["will", "would"],
            ["can", "could"],
            ["may", "might"],
            ["must (obligation)", "had to (often)"],
        ],
        caption="Typical backshift",
    ))

    s.append(note(
        "<p><strong>Backshift is optional</strong> when the situation is still true: "
        "<em>She said the office is in Downtown</em> (still true) / <em>was</em> also possible. "
        "No backshift after present reporting verbs: <em>She says she is busy.</em></p>"
    ))

    s.append(rule(
        "say vs tell",
        "<em>tell</em> normally needs a person object: tell someone something. "
        "<em>say</em> does not take a person object directly: say something (to someone).",
        examples_list=[
            "She told me the password changed.",
            "She said the password had changed.",
            "She said to me that… (possible but heavier)",
        ],
        mistakes_list=[
            ("She said me the news.", "She told me the news. / She said the news to me."),
            ("She told that she was tired.", "She said that… / She told me that…"),
        ],
        levels=["A2", "B1"],
    ))

    s.append(rule(
        "Reported questions",
        "Use statement word order (no do-support, no auxiliary inversion). Yes/No → if/whether. Wh- → keep wh-word.",
        examples_list=[
            "\"Are you ready?\" → She asked if/whether I was ready.",
            "\"Where do you work?\" → He asked where I worked.",
            "\"Who fixed it?\" → She asked who had fixed it.",
        ],
        mistakes_list=[
            ("He asked where do I work.", "He asked where I work/worked."),
            ("She asked me that was I free.", "She asked me if I was free."),
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Reported commands, requests, advice",
        "Often: tell/ask/advise + object + to-infinitive. Suggest often takes gerund or that-clause.",
        examples_list=[
            "\"Open a ticket.\" → She told me to open a ticket.",
            "\"Please wait.\" → He asked us to wait.",
            "\"You should rest.\" → She advised me to rest.",
            "\"Let's postpone.\" → She suggested postponing. / suggested that we postpone.",
            "\"Don't commit secrets.\" → He warned us not to commit secrets.",
        ],
        levels=["B1", "B2"],
    ))

    s.append(table(
        ["Direct time/place", "Often reported as"],
        [
            ["today / tomorrow / yesterday", "that day / the next day / the day before"],
            ["now / ago / here / this", "then / before / there / that"],
            ["last week / next week", "the week before / the following week"],
        ],
        caption="Deictic shifts (when needed for clarity)",
    ))

    s.append(advanced(
        "<p>Reporting verbs carry attitude: <em>claim, admit, deny, insist, argue, confirm, estimate, promise, threaten, "
        "remind, accuse someone of -ing, apologise for -ing, congratulate someone on -ing</em>. "
        "Learn verb patterns individually.</p>"
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_16():
    s = []
    s.append(part_header(16, "Questions",
        "English questions rely on auxiliary verbs and word order. Subject questions look different from object questions — "
        "a major source of mistakes."))

    s.append(rule(
        "Yes/No questions",
        "Invert auxiliary/modal/be with the subject. If there is no auxiliary, insert do/does/did.",
        examples_list=[
            "Are you on-call? / Can they join? / Have you eaten?",
            "Do you use Vim? / Did the tests pass?",
        ],
        levels=["A1", "A2"],
    ))

    s.append(rule(
        "Wh- questions",
        "Wh-word + auxiliary + subject + main verb… (for object/adverbial questions).",
        examples_list=[
            "Where do you work?",
            "What did she say?",
            "How long have you been waiting?",
            "Why is the pipeline red?",
        ],
        levels=["A1", "A2", "B1"],
    ))

    s.append(rule(
        "Subject vs object questions",
        "If the wh-word is the subject, do not use do-support; keep statement order after the wh-word.",
        examples_list=[
            "Object: Who did you see? (you saw X)",
            "Subject: Who saw you? (X saw you)",
            "Object: What did the alert trigger?",
            "Subject: What triggered the alert?",
            "Which engineer fixed it? (subject)",
            "Which engineer did you call? (object)",
        ],
        mistakes_list=[
            ("Who did see you?", "Who saw you?"),
            ("Who you saw?", "Who did you see?"),
        ],
        levels=["A2", "B1", "B2"],
    ))

    s.append(rule(
        "Indirect / embedded questions",
        "Inside statements or polite requests, use statement order. No do-inversion after the wh-word/if.",
        examples_list=[
            "I wonder where the logs are.",
            "Could you tell me what time it starts?",
            "Do you know if the VPN is down?",
        ],
        mistakes_list=[
            ("Could you tell me where is the office?", "Could you tell me where the office is?"),
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Question tags",
        "Tag matches the auxiliary and reverses polarity. Positive statement → negative tag (usually), and vice versa. "
        "Intonation: falling = expect agreement; rising = genuine check.",
        examples_list=[
            "You're on-call, aren't you?",
            "She can't join, can she?",
            "Let's ship, shall we? (special)",
            "I'm late, aren't I? (special)",
        ],
        levels=["B1", "B2"],
    ))

    s.append(rule(
        "Negative, rhetorical, and echo questions",
        "Negative questions can express surprise or expectation: <em>Isn't that the old endpoint?</em> "
        "Rhetorical questions don't expect answers. Echo questions check what was heard: <em>You deleted what?</em>",
        examples_list=[
            "Haven't we already fixed this?",
            "Who cares about the legacy stylesheet?",
            "She's joining when?",
        ],
        levels=["B2", "C1"],
    ))
    s.append(part_footer())
    return "\n".join(s)


def parts_9_to_16():
    return "\n".join([
        part_09(), part_10(), part_11(), part_12(),
        part_13(), part_14(), part_15(), part_16(),
    ])
