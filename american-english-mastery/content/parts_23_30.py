"""Parts 23–30: Expressions through listening."""
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, table, badge, expr_card
)


def _exprs(items):
    return "\n".join(expr_card(e) for e in items)


def part_23():
    s = [part_header(23, "Daily Expressions",
        "Natural American expressions by situation. Labels show register — do not treat slang as default.")]

    catalog = {
        "Greetings": [
            {"expression": "Hey, how's it going?", "meaning": "Casual hello + how are you", "context": "friends, coworkers", "register": "casual", "example": "Hey, how's it going? — Pretty good.", "alternatives": ["Hi, how are you?", "What's up?"]},
            {"expression": "Good to see you.", "meaning": "Friendly greeting when meeting", "context": "work/social", "register": "neutral", "example": "Good to see you — thanks for joining.", "alternatives": ["Nice to see you."]},
            {"expression": "Long time no see.", "meaning": "Haven't met in a while", "context": "informal reunion", "register": "informal", "example": "Long time no see! How have you been?", "alternatives": ["It's been a while."]},
        ],
        "Small talk": [
            {"expression": "How was your weekend?", "meaning": "Light personal check-in", "context": "Monday mornings", "register": "neutral", "example": "How was your weekend? — Pretty chill.", "alternatives": ["Do anything fun this weekend?"]},
            {"expression": "Crazy weather, huh?", "meaning": "Comment on weather to open talk", "context": "casual", "register": "casual", "example": "Crazy weather, huh? — Tell me about it.", "alternatives": ["Nice day today."]},
        ],
        "Starting conversations": [
            {"expression": "Got a minute?", "meaning": "Ask if someone is free briefly", "context": "office/Slack", "register": "casual", "example": "Got a minute to look at this error?", "alternatives": ["Do you have a second?", "Is now a good time?"], "pron_note": "got a → often linked"},
            {"expression": "Quick question for you.", "meaning": "Soft opener before asking", "context": "work", "register": "professional", "example": "Quick question for you — who owns billing?", "alternatives": ["Can I ask you something quickly?"]},
        ],
        "Ending conversations": [
            {"expression": "I should let you go.", "meaning": "Polite end to a call/chat", "context": "calls", "register": "neutral", "example": "Anyway, I should let you go — thanks.", "alternatives": ["I'll let you get back to it."]},
            {"expression": "Talk soon.", "meaning": "Friendly goodbye", "context": "email/Slack/call", "register": "casual", "example": "Sounds good — talk soon.", "alternatives": ["Catch you later.", "Take care."]},
        ],
        "Asking for help": [
            {"expression": "Could you give me a hand with this?", "meaning": "Ask for help", "context": "work", "register": "neutral", "example": "Could you give me a hand with this query?", "alternatives": ["Can you help me with…?", "Mind helping me…?"]},
            {"expression": "I'm stuck on…", "meaning": "Signal blocker", "context": "standup/work", "register": "professional", "example": "I'm stuck on the auth redirect.", "alternatives": ["I'm blocked by…"]},
        ],
        "Asking for clarification": [
            {"expression": "What exactly do you mean by…?", "meaning": "Ask for precise meaning", "context": "meetings", "register": "professional", "example": "What exactly do you mean by 'soon'?", "alternatives": ["Could you clarify…?", "Do you mean…?"]},
            {"expression": "Just to make sure I understand…", "meaning": "Confirm interpretation", "context": "work", "register": "professional", "example": "Just to make sure I understand, we need this by Friday?", "alternatives": ["So if I'm hearing you right…"]},
        ],
        "Confirming": [
            {"expression": "That makes sense.", "meaning": "Show understanding/agreement with logic", "context": "discussion", "register": "neutral", "example": "Ah, that makes sense.", "alternatives": ["Got it.", "I see."]},
            {"expression": "Sounds good.", "meaning": "Agree with a plan", "context": "planning", "register": "casual", "example": "Let's ship Thursday — sounds good.", "alternatives": ["Works for me.", "I'm good with that."]},
        ],
        "Agreeing": [
            {"expression": "That's a good point.", "meaning": "Validate someone's idea", "context": "meetings", "register": "professional", "example": "That's a good point — we should check edge cases.", "alternatives": ["Fair point.", "I agree."]},
            {"expression": "I'm with you on that.", "meaning": "Side with someone", "context": "discussion", "register": "casual", "example": "I'm with you on that — let's keep it simple.", "alternatives": ["I'm on board."]},
        ],
        "Disagreeing": [
            {"expression": "I'm not sure I agree.", "meaning": "Soft disagreement", "context": "meetings", "register": "professional", "example": "I'm not sure I agree — the risk seems high.", "alternatives": ["I see it differently.", "I have a different take."]},
            {"expression": "I get where you're coming from, but…", "meaning": "Acknowledge then disagree", "context": "debate", "register": "neutral", "example": "I get where you're coming from, but users will notice.", "alternatives": ["I hear you, but…"]},
        ],
        "Giving opinions": [
            {"expression": "From my perspective…", "meaning": "Frame opinion", "context": "work", "register": "professional", "example": "From my perspective, we should ship a smaller MVP.", "alternatives": ["The way I see it…", "I think…"]},
            {"expression": "I feel like…", "meaning": "Softer opinion (very common AmE)", "context": "conversation", "register": "casual", "example": "I feel like this is over-engineered.", "alternatives": ["It seems like…"]},
        ],
        "Uncertainty": [
            {"expression": "I'm not sure.", "meaning": "Express uncertainty", "context": "any", "register": "neutral", "example": "I'm not sure — let me check.", "alternatives": ["I don't know off the top of my head."]},
            {"expression": "It depends.", "meaning": "Answer is conditional", "context": "questions", "register": "neutral", "example": "It depends on the traffic pattern.", "alternatives": ["Hard to say.", "That's context-dependent."]},
        ],
        "Apologies": [
            {"expression": "Sorry about that.", "meaning": "Brief apology", "context": "small mistakes", "register": "neutral", "example": "Sorry about that — wrong link.", "alternatives": ["My bad. (casual)", "Apologies for the delay. (more formal)"]},
            {"expression": "I owe you an apology.", "meaning": "Stronger apology", "context": "serious", "register": "neutral", "example": "I owe you an apology for missing the review.", "alternatives": ["I apologize for…"]},
        ],
        "Thanks": [
            {"expression": "I appreciate it.", "meaning": "Thank someone", "context": "work/social", "register": "neutral", "example": "Thanks for the review — I appreciate it.", "alternatives": ["Thanks a lot.", "Thanks so much."]},
            {"expression": "Thanks for the heads-up.", "meaning": "Thanks for a warning/info", "context": "work", "register": "professional", "example": "Thanks for the heads-up about the outage.", "alternatives": ["Thanks for letting me know."]},
        ],
        "Requests": [
            {"expression": "Would you mind…?", "meaning": "Polite request", "context": "work", "register": "professional", "example": "Would you mind taking a look?", "alternatives": ["Could you…?", "Do you mind…?"]},
            {"expression": "When you get a chance…", "meaning": "Non-urgent request", "context": "Slack/email", "register": "professional", "example": "When you get a chance, can you review this?", "alternatives": ["No rush, but…"]},
        ],
        "Refusing politely": [
            {"expression": "I wish I could, but…", "meaning": "Polite refusal", "context": "invites/asks", "register": "neutral", "example": "I wish I could, but I'm at capacity this week.", "alternatives": ["I'm going to have to pass.", "Not this time."]},
            {"expression": "That's not going to work for me.", "meaning": "Clear decline", "context": "scheduling", "register": "neutral", "example": "Thursday's not going to work for me.", "alternatives": ["I can't make that."]},
        ],
        "Suggestions / advice": [
            {"expression": "What if we…?", "meaning": "Suggest an option", "context": "brainstorm", "register": "neutral", "example": "What if we cached the results?", "alternatives": ["How about we…?", "Maybe we could…"]},
            {"expression": "If I were you, I'd…", "meaning": "Advice frame", "context": "advice", "register": "neutral", "example": "If I were you, I'd write a failing test first.", "alternatives": ["I'd recommend…"]},
        ],
        "Buying time": [
            {"expression": "Let me think.", "meaning": "Need a moment", "context": "questions", "register": "neutral", "example": "Let me think… I'd start with metrics.", "alternatives": ["Give me a second.", "Let me see."]},
            {"expression": "That's a good question.", "meaning": "Buy time + show respect", "context": "meetings/interviews", "register": "professional", "example": "That's a good question — I haven't measured it yet.", "alternatives": ["Interesting question."]},
        ],
        "Showing understanding": [
            {"expression": "I see what you mean.", "meaning": "Show comprehension", "context": "discussion", "register": "neutral", "example": "I see what you mean about the coupling.", "alternatives": ["I get it.", "That tracks. (casual)"]},
            {"expression": "Tell me about it.", "meaning": "Empathy / shared frustration (not literal request)", "context": "casual", "register": "casual", "example": "This build is slow. — Tell me about it.", "alternatives": ["I know, right?"]},
        ],
        "Interrupting politely": [
            {"expression": "Sorry to interrupt…", "meaning": "Polite interruption", "context": "meetings", "register": "professional", "example": "Sorry to interrupt — the timer's up.", "alternatives": ["Can I jump in for a second?"]},
            {"expression": "Quick follow-up on that…", "meaning": "Add related point", "context": "meetings", "register": "professional", "example": "Quick follow-up on that — who owns it?", "alternatives": ["Building on that…"]},
        ],
        "Changing topics": [
            {"expression": "Speaking of which…", "meaning": "Transition via related idea", "context": "conversation", "register": "neutral", "example": "Speaking of which, did we renew the cert?", "alternatives": ["That reminds me…"]},
            {"expression": "Anyway…", "meaning": "Return to main topic / wrap side chat", "context": "conversation", "register": "casual", "example": "Anyway, back to the release plan.", "alternatives": ["Getting back on track…"]},
        ],
        "Frustration / concern / excitement": [
            {"expression": "This is getting out of hand.", "meaning": "Situation becoming unmanageable", "context": "problems", "register": "neutral", "example": "The scope is getting out of hand.", "alternatives": ["This is escalating."]},
            {"expression": "I'm a bit concerned about…", "meaning": "Express worry politely", "context": "work", "register": "professional", "example": "I'm a bit concerned about the timeline.", "alternatives": ["I'm worried that…"]},
            {"expression": "That's awesome!", "meaning": "Excitement/praise", "context": "casual", "register": "casual", "example": "We hit the SLA — that's awesome!", "alternatives": ["That's great!", "Love it. (casual)"]},
        ],
    }

    for cat, items in catalog.items():
        s.append(h3(cat, "expr-" + cat.lower().replace(" ", "-").replace("/", "-")[:40]))
        s.append(_exprs(items))
    s.append(part_footer())
    return "\n".join(s)


def part_24():
    s = [part_header(24, "Natural Conversational Patterns",
        "Reusable frames Americans use constantly. Practice them until they are automatic.")]
    frames = [
        "I think…", "I feel like…", "I guess…", "I'm not sure…", "It depends…",
        "As far as I know…", "From my perspective…", "The thing is…", "What I mean is…",
        "The main issue is…", "The problem is…", "That's a good point.", "That makes sense.",
        "I see what you mean.", "I'm not sure I agree.", "Let me think.", "Give me a second.",
        "I'll let you know.", "To be honest…", "Basically…", "More specifically…",
        "At the end of the day…", "Long story short…", "The way I see it…",
        "Correct me if I'm wrong, but…", "If that makes sense.", "Does that make sense?",
        "You know what I mean?", "Kind of / sort of…", "Pretty much…", "Not really.",
        "It turns out…", "It looks like…", "It seems like…", "I'm leaning toward…",
        "I'd rather…", "I'd prefer…", "I'm fine with…", "I'm open to…",
        "Let's assume…", "For example…", "In other words…", "On the other hand…",
        "That said…", "Having said that…", "Worst case…", "Best case…",
        "I'll keep you posted.", "Keep me in the loop.", "No worries.", "All good.",
    ]
    s.append(ul(*[f"<em>{f}</em>" for f in frames]))
    s.append(examples(
        "The thing is, we don't have enough test coverage yet.",
        "What I mean is, we should ship a smaller version first.",
        "As far as I know, the cert renews automatically.",
        "Correct me if I'm wrong, but this endpoint is public.",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_25():
    s = [part_header(25, "Conversation Management",
        "How Americans keep conversations moving: openings, interest signals, repair, and closings.")]
    s.append(table(
        ["Move", "Useful language"],
        [
            ["Start", "Got a minute? / Quick question. / Do you have a second?"],
            ["Show interest", "Oh really? / No way. / How did that go? / What happened next?"],
            ["Follow-up questions", "Why do you think that? / How so? / What would that look like?"],
            ["Interrupt politely", "Sorry to interrupt… / Can I jump in?"],
            ["Disagree politely", "I see it differently. / I'm not sure I agree."],
            ["Self-correct", "Sorry — what I meant was… / Let me rephrase."],
            ["Clarify", "Do you mean X or Y? / Just to clarify…"],
            ["Confirm", "So we're saying…? / If I understand correctly…"],
            ["Change topic", "Speaking of which… / Anyway… / On a related note…"],
            ["End", "I should let you go. / Talk soon. / Thanks — I'll follow up."],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_26():
    s = [part_header(26, "Workplace English",
        "Natural American workplace phrases for meetings, status, feedback, and collaboration.")]
    s.append(table(
        ["Situation", "Phrases"],
        [
            ["Status update", "Quick update:… / Here's where we are:… / We're on track / at risk."],
            ["Priorities", "Top priority is… / Let's prioritize X over Y. / What's the urgency?"],
            ["Deadlines", "Can we push the deadline? / Is Friday firm? / We'll need more runway."],
            ["Blockers", "I'm blocked by… / The dependency is… / Who can unblock this?"],
            ["Asking questions", "Quick clarification:… / Who owns this? / What's the acceptance criteria?"],
            ["Suggestions", "One option would be… / What if we…? / I'd suggest…"],
            ["Disagreement", "I have a concern about… / Have we considered…? / The risk is…"],
            ["Feedback", "One thing that worked well… / One thing to improve… / Appreciate the thoroughness."],
            ["Managers", "I wanted to flag… / Do you have bandwidth to discuss…? / I'd like your input on…"],
            ["Clients", "Thanks for your patience. / We'll follow up in writing. / Just to confirm requirements…"],
            ["Meetings", "Let's take this offline. / Parking lot that for now. / Action item:…"],
            ["Negotiation", "What's negotiable? / We can do X if we drop Y. / That trade-off works for us."],
        ],
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_27():
    s = [part_header(27, "Software Engineering English",
        "Practical language for standups, code review, bugs, architecture, and engineering collaboration.")]
    sections = [
        ("Daily standups", [
            "I'm working on…", "I've finished…", "I'm blocked by…",
            "I ran into an issue with…", "No blockers.", "I'll pick up… next.",
            "I could use a second pair of eyes on…",
        ]),
        ("Code reviews", [
            "I'd suggest…", "Could we…?", "This could be simplified…",
            "Would it make sense to…?", "Nit: … (small style comment)",
            "Blocking vs non-blocking comment…", "LGTM / Looks good to me.",
            "Can you add a test for…?", "I'm not sure this handles…",
        ]),
        ("Bugs & incidents", [
            "I reproduced the issue.", "It seems to be related to…",
            "I found the root cause.", "I'll push a fix.", "We need a hotfix.",
            "Let's roll back.", "Severity looks like a Sev-2.", "I'll write a short postmortem.",
        ]),
        ("Requirements", [
            "Could you clarify…?", "What exactly do you mean by…?",
            "Are we expecting…?", "Is this a must-have or nice-to-have?",
            "What's out of scope?", "Do we have acceptance criteria?",
        ]),
        ("Architecture", [
            "From an architectural perspective…", "This approach would…",
            "The trade-off is…", "This couples X to Y.", "We might want to isolate…",
            "In terms of scalability…", "Failure mode would be…",
        ]),
        ("Collaboration", [
            "I'll sync with…", "Let's pair on this.", "Can we spike it for an hour?",
            "I'll draft an RFC.", "Putting up a WIP PR.", "Please hold off on merging.",
        ]),
    ]
    for title, phrases in sections:
        s.append(h3(title))
        s.append(ul(*[f"<em>{x}</em>" for x in phrases]))
    s.append(part_footer())
    return "\n".join(s)


def part_28():
    s = [part_header(28, "Interview English",
        "Language for technical and behavioral interviews: structure, clarity, and thinking aloud.")]
    s.append(table(
        ["Goal", "Phrases"],
        [
            ["Introduce yourself", "I'm a … based in …. Recently I've been working on…"],
            ["Describe experience", "In my last role… / One project I'm proud of… / I owned…"],
            ["Explain decisions", "I chose X because… / The trade-off was… / We considered Y but…"],
            ["Unknown questions", "I haven't done that exact thing, but I'd approach it by…"],
            ["Thinking time", "Let me think about that. / I'd start by clarifying…"],
            ["Clarify", "Just to confirm, are we optimizing for X or Y? / Can I ask a clarifying question?"],
            ["STAR behavioral", "Situation… Task… Action… Result… / The outcome was…"],
            ["Ask interviewer", "What does success look like in this role? / What does the team roadmap look like?"],
            ["Close", "Thanks — I enjoyed the conversation. / I'm excited about the opportunity."],
        ],
    ))
    s.append(examples(
        "Let me think about that. I'd approach it by first clarifying the constraints.",
        "My reasoning is that consistency matters more than micro-optimizations here.",
        "I'm not entirely sure, but I'd consider a queue to absorb spikes.",
        "In that situation, I communicated early, proposed options, and owned the follow-up.",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_29():
    s = [part_header(29, "American vs Textbook English",
        "Textbook English can be correct but stiff. American conversation prefers contractions, "
        "phrasal verbs, discourse markers, and ellipsis — without becoming slang by default.")]
    s.append(table(
        ["Textbook / formal", "Natural neutral American", "Casual"],
        [
            ["I am going to examine the issue.", "I'm going to look into the issue.", "I'll check it out."],
            ["Would you like to proceed?", "Want to go ahead?", "Ready to go?"],
            ["I do not know.", "I don't know.", "Dunno. / No idea."],
            ["Please inform me when it is completed.", "Let me know when it's done.", "Ping me when it's done."],
            ["I disagree with that proposal.", "I'm not sure I agree.", "Yeah, I'm not buying that."],
        ],
    ))
    s.append(ul(
        "<span class='register'>correct but formal</span> — fine in academic writing / careful email",
        "<span class='register'>natural neutral</span> — best default for work",
        "<span class='register'>casual</span> — friends / informal teammates",
        "<span class='register'>slang</span> — labeled and limited; not your default professional voice",
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_30():
    s = [part_header(30, "Listening Reference",
        "Why American speech can be hard to catch — and a decoding strategy you can reuse.")]
    s.append(ul(
        "Weak forms of function words (to/for/and/can)",
        "Reductions (gonna/wanna/kinda) in casual speech",
        "Linking across word boundaries",
        "Flap T making t/d sound alike",
        "Schwa in unstressed syllables",
        "Sentence stress hiding unstressed material",
        "Intonation carrying attitude",
        "Contractions and elision",
    ))
    s.append(h3("Decoding strategy", "p30-decode"))
    s.append(ul(
        "1. Identify stressed words (content peaks).",
        "2. Identify reduced words (likely function words).",
        "3. Identify linking (C→V / V→V).",
        "4. Identify contractions (I'm / don't / we've).",
        "5. Identify missing/reduced sounds (Flap T, dropped t/d).",
        "6. Reconstruct the full careful sentence.",
    ))
    s.append(examples(
        "Heard: 'Kinda looks like a race.' → Careful: It kind of looks like a race condition.",
        "Heard: 'Lemme see whatcha got.' → Careful: Let me see what you have got / what you've got.",
    ))
    s.append(part_footer())
    return "\n".join(s)


def parts_23_to_30():
    return "\n".join([
        part_23(), part_24(), part_25(), part_26(),
        part_27(), part_28(), part_29(), part_30(),
    ])
