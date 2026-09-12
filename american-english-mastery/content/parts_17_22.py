"""Parts 17–22: Vocabulary, families, collocations, verbs, phrasals, confusing words."""
import json
from pathlib import Path
from helpers import (
    part_header, part_footer, h3, p, ul, rule, examples, mistakes, compare,
    note, warning, table, badge, vocab_card, expr_card
)

DATA = Path(__file__).resolve().parent.parent / "data" / "vocab.json"


def load_vocab():
    return json.loads(DATA.read_text(encoding="utf-8"))


def compact_card(e):
    wid = e["id"]
    ipa = f"<span class='ipa'>/{e['ipa']}/</span> · " if e.get("ipa") else ""
    ar = f" · <span dir='rtl' lang='ar'>{e['arabic']}</span>" if e.get("arabic") else ""
    cols = ""
    if e.get("collocations"):
        cols = "<p class='label'>Collocations</p><p>" + " · ".join(f"<em>{c}</em>" for c in e["collocations"]) + "</p>"
    return f'''<article class="vocab-card" id="v-{wid}">
  <div class="rule-head">
    <h4 class="vocab-word">{e["word"]} <span class="pos">{e.get("pos","")}</span></h4>
    <div class="vocab-meta">{badge(e.get("level","B1"))}<span class="register">{e.get("register","neutral")}</span></div>
  </div>
  <p>{ipa}{e.get("meaning","")}{ar}</p>
  <p class="ex"><em>{e.get("example","")}</em></p>
  {cols}
</article>'''


def part_17():
    vocab = load_vocab()
    s = [part_header(17, "3000 Core American Vocabulary",
        f"Approximately <strong>{len(vocab)}</strong> high-value lexical items prioritized by frequency, usefulness, "
        "everyday communication, workplace English, and software/professional contexts. "
        "This is not a bilingual dictionary dump — learn words with pronunciation, collocations, and register.")]
    s.append(h3("How to read vocabulary entries", "p17-how"))
    s.append(ul(
        "<strong>Headword / lemma:</strong> the base dictionary form (e.g., decide).",
        "<strong>Word family:</strong> related forms (decision, decisive) — see Part 18.",
        "<strong>Active vocabulary:</strong> words you can use accurately when speaking/writing.",
        "<strong>Passive vocabulary:</strong> words you recognize in listening/reading.",
        "Simple words may have shorter entries; high-value verbs/phrases get collocations.",
        "Arabic glosses appear where especially useful — English meaning remains primary.",
    ))
    s.append(note(
        "<p>Use this section as a lookup while shadowing and reading. Add new words to your active set by writing "
        "one personal example + two collocations.</p>"
    ))

    order = ["A1", "A2", "B1", "B2", "C1"]
    for lvl in order:
        items = sorted([e for e in vocab if e.get("level") == lvl], key=lambda e: e["word"])
        s.append(f'<div class="level-section" id="vocab-{lvl.lower()}">')
        s.append(h3(f"{lvl} core vocabulary ({len(items)} items)", f"vocab-{lvl.lower()}-list"))
        s.append(badge(lvl))
        for e in items:
            if e.get("collocations") or e.get("ipa") or e.get("arabic"):
                s.append(compact_card(e))
            else:
                s.append(compact_card(e))
        s.append("</div>")

    s.append(part_footer())
    return "\n".join(s)


def part_18():
    s = [part_header(18, "Word Families",
        "Learning families multiplies vocabulary efficiently. Know how suffixes shift part of speech and stress.")]
    s.append(table(
        ["Verb", "Noun", "Adjective", "Adverb"],
        [
            ["decide", "decision", "decisive / indecisive", "decisively"],
            ["develop", "development / developer", "developed / developing", "—"],
            ["communicate", "communication", "communicative", "communicatively"],
            ["create", "creation / creativity / creator", "creative", "creatively"],
            ["analyze", "analysis / analyst", "analytical", "analytically"],
            ["apply", "application / applicant", "applicable", "—"],
            ["succeed", "success", "successful", "successfully"],
            ["fail", "failure", "failed", "—"],
            ["rely", "reliability", "reliable / unreliable", "reliably"],
            ["require", "requirement", "required", "—"],
            ["produce", "product / production / productivity", "productive", "productively"],
            ["inform", "information", "informative", "—"],
            ["employ", "employer / employee / employment", "employed", "—"],
            ["organize", "organization", "organized / organizational", "—"],
            ["identify", "identity / identification", "identifiable", "—"],
        ],
    ))
    s.append(h3("High-value suffixes", "p18-suf"))
    s.append(table(
        ["Suffix", "Usually makes", "Examples"],
        [
            ["-tion / -sion", "noun", "action, decision, permission"],
            ["-ment", "noun", "development, requirement, agreement"],
            ["-ness", "noun", "awareness, darkness, openness"],
            ["-ity", "noun", "reliability, security, complexity"],
            ["-er / -or", "person/device", "developer, manager, processor"],
            ["-ive", "adjective", "active, effective, responsive"],
            ["-al", "adjective", "critical, technical, professional"],
            ["-ous", "adjective", "ambiguous, continuous"],
            ["-ful / -less", "adjective", "useful, careful, useless, careless"],
            ["-ly", "adverb", "clearly, quickly, professionally"],
            ["-ize", "verb", "optimize, prioritize, serialize"],
            ["-able / -ible", "adjective", "scalable, responsible, flexible"],
        ],
    ))
    s.append(warning("<p>Suffixes can move stress (PHOtograph → phoTOgraphy). Recheck stress when the form changes.</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_19():
    s = [part_header(19, "Collocations",
        "Natural American English is collocational. Learn chunks, not isolated translations.")]
    s.append(table(
        ["Pattern", "Natural examples"],
        [
            ["make + noun", "make a decision, make progress, make sense, make a mistake, make time"],
            ["take + noun", "take responsibility, take a break, take place, take notes, take into account"],
            ["do + noun", "do research, do business, do a favor, do well, do harm"],
            ["have + noun", "have a meeting, have trouble, have an impact, have access"],
            ["strong/weak adj+", "strong argument, heavy traffic, high priority, deep concern, soft deadline (casual)"],
            ["adverb + adj", "highly likely, deeply concerned, closely related, widely used"],
            ["verb + prep", "depend on, focus on, consist of, result in, deal with"],
        ],
    ))
    s.append(examples(
        "We need to <em>make a decision</em> by Friday.",
        "There is <em>heavy traffic</em> on the bridge.",
        "It is <em>highly likely</em> that latency will spike.",
        "I'm <em>deeply concerned</em> about the outage window.",
    ))
    s.append(mistakes(
        ("do a decision", "make a decision"),
        ("strong rain", "heavy rain"),
        ("big importance", "great/major importance · high importance"),
    ))
    s.append(part_footer())
    return "\n".join(s)


def part_20():
    s = [part_header(20, "High-Value Verbs",
        "Light verbs and frequent verbs carry huge communicative load. Master patterns, not only dictionary glosses.")]
    verbs = [
        ("GET", ["get a job", "get ready", "get better", "get tired", "get home", "get something",
                 "get someone to do something", "get used to something", "get back to someone", "get rid of"]),
        ("TAKE", ["take a break", "take responsibility", "take notes", "take place", "take over",
                  "take into account", "take time", "take off", "take on"]),
        ("MAKE", ["make a decision", "make sense", "make progress", "make sure", "make up",
                  "make it (succeed/attend)", "make out", "make room"]),
        ("DO", ["do homework", "do research", "do business", "do a favor", "do without", "do over"]),
        ("HAVE", ["have a meeting", "have trouble", "have to", "have someone do something", "have got to"]),
        ("GIVE", ["give a presentation", "give feedback", "give up", "give in", "give someone a hand"]),
        ("KEEP", ["keep in mind", "keep going", "keep track of", "keep up with", "keep someone posted"]),
        ("PUT", ["put off", "put up with", "put together", "put out", "put in (time/effort)"]),
        ("SET", ["set up", "set a deadline", "set aside", "set off", "set out"]),
        ("RUN", ["run tests", "run into", "run out of", "run through", "run a service"]),
        ("HOLD", ["hold a meeting", "hold on", "hold off", "hold accountable"]),
        ("BRING", ["bring up", "bring about", "bring in", "bring back"]),
        ("TURN", ["turn on/off", "turn out", "turn into", "turn down", "turn in"]),
        ("LOOK", ["look for", "look after", "look into", "look forward to", "look like", "look up"]),
        ("COME", ["come up with", "come across", "come from", "come in handy", "come down to"]),
        ("GO", ["go over", "go through", "go ahead", "go live", "go wrong"]),
        ("WORK", ["work on", "work out", "work around", "work with", "it works"]),
        ("MOVE", ["move forward", "move on", "move up", "get moving"]),
        ("LEAVE", ["leave out", "leave behind", "leave a message"]),
        ("MEAN", ["mean to", "mean that", "what do you mean"]),
        ("SEEM", ["seem to", "it seems that", "seem like"]),
        ("FEEL", ["feel like", "feel free", "feel strongly about"]),
        ("BECOME", ["become available", "become clear", "become an issue"]),
        ("REMAIN", ["remain open", "remain unclear", "remain in place"]),
    ]
    for name, pats in verbs:
        s.append(rule(name, f"High-frequency verb patterns for <strong>{name}</strong>.",
                       examples_list=pats, levels=["A1", "A2", "B1", "B2"]))
    s.append(part_footer())
    return "\n".join(s)


def part_21():
    s = [part_header(21, "Phrasal Verbs",
        "High-value phrasal verbs for everyday and workplace American English. "
        "Note separability and register.")]
    rows = [
        ["find out", "discover", "insep.", "neutral", "find out what happened", "Did you find out the owner?"],
        ["figure out", "solve/understand", "sep.", "neutral", "figure it out", "I can't figure out this error."],
        ["work out", "solve / exercise / go well", "sep./intrans", "neutral", "work out the details", "It worked out."],
        ["look into", "investigate", "insep.", "professional", "look into it", "I'll look into the logs."],
        ["set up", "arrange/install", "sep.", "neutral", "set it up", "We set up staging."],
        ["carry out", "perform", "sep.", "formal", "carry out a review", "We carried out testing."],
        ["bring up", "mention; raise", "sep.", "neutral", "bring it up", "Don't bring that up yet."],
        ["point out", "highlight", "sep.", "professional", "point out that…", "She pointed out a risk."],
        ["come up with", "invent/propose", "insep.", "neutral", "come up with a plan", "We came up with a fix."],
        ["deal with", "handle", "insep.", "neutral", "deal with issues", "How do we deal with retries?"],
        ["run into", "encounter", "insep.", "neutral", "run into problems", "I ran into an edge case."],
        ["go over", "review", "insep.", "professional", "go over the plan", "Let's go over the checklist."],
        ["follow up", "continue later", "insep.", "professional", "follow up on X", "I'll follow up tomorrow."],
        ["put off", "postpone", "sep.", "neutral", "put it off", "Don't put it off."],
        ["put up with", "tolerate", "insep.", "neutral", "put up with noise", "I won't put up with flaky tests."],
        ["turn down", "reject; lower", "sep.", "neutral", "turn down an offer", "They turned us down."],
        ["call off", "cancel", "sep.", "neutral", "call off a meeting", "We called it off."],
        ["break down", "stop working; analyze", "intrans/sep", "neutral", "break down costs", "The build broke down."],
        ["fill out", "complete a form (AmE)", "sep.", "neutral", "fill out a form", "Please fill this out."],
        ["check out", "examine; leave hotel", "sep.", "neutral", "check it out", "Check out this PR."],
        ["sign up", "register", "sep./insep patterns", "neutral", "sign up for…", "Sign up for the beta."],
        ["log in / log out", "authenticate session", "often insep. particles", "professional", "log in to…", "Log in to staging."],
        ["shut down", "power off / stop", "sep.", "neutral", "shut it down", "Shut down the instance."],
        ["scale up / down", "increase/decrease capacity", "sep.", "professional", "scale up", "We scaled up overnight."],
        ["roll out", "release gradually", "sep.", "professional", "roll out a feature", "We rolled it out to 10%."],
        ["roll back", "revert release", "sep.", "professional", "roll back a deploy", "Roll it back now."],
        ["ship out / ship", "release (tech slang)", "—", "professional/informal", "ship a feature", "We shipped yesterday."],
        ["catch up", "reach same level; update", "insep.", "neutral", "catch up on slack", "Let's catch up Friday."],
        ["wrap up", "finish", "sep.", "neutral", "wrap up the meeting", "Let's wrap up."],
        ["reach out", "contact (AmE workplace)", "insep.", "professional", "reach out to…", "I'll reach out to legal."],
    ]
    s.append(table(["Phrasal verb", "Meaning", "Sep.", "Register", "Pattern", "Example"], rows))
    s.append(note("<p>Pronoun objects go between verb and particle when separable: <em>figure it out</em> (not <em>figure out it</em>).</p>"))
    s.append(part_footer())
    return "\n".join(s)


def part_22():
    s = [part_header(22, "Confusing Words",
        "Pairs that share translation equivalents or similar forms but differ in American usage.")]
    pairs = [
        ("say / tell", "say something (to someone); tell someone something", "She said hello. / She told me the plan."),
        ("speak / talk", "speak = languages/formal address; talk = conversation", "speak Arabic; talk to a teammate"),
        ("hear / listen", "hear = perceive; listen = pay attention", "Did you hear that? / Listen to the call."),
        ("see / watch / look", "see=perceive; watch=attention over time; look=direct eyes", "see a bug; watch a demo; look at logs"),
        ("bring / take", "bring toward here/listener; take away", "Bring your laptop. / Take an umbrella."),
        ("borrow / lend", "borrow=receive temporarily; lend=give temporarily", "borrow a charger / lend me a charger"),
        ("learn / teach", "learn=acquire; teach=instruct", "learn Go / teach someone Go"),
        ("remember / remind", "remember=have in memory; remind=cause to remember", "I remembered. / Remind me."),
        ("job / work", "job=countable role; work=uncountable activity", "a new job / a lot of work"),
        ("fun / funny", "fun=enjoyable; funny=humorous", "The hackathon was fun. / a funny joke"),
        ("advice / advise", "advice=noun (uncountable); advise=verb", "some advice / I advise waiting"),
        ("affect / effect", "affect=verb; effect=usually noun", "affect latency / the effect"),
        ("especially / specially", "especially=above all; specially=for a special purpose", "especially useful / specially designed"),
        ("actual / current", "actual=real; current=present-time", "the actual root cause / current status"),
        ("eventually / finally", "eventually=after time passed; finally=at the end of a sequence", "It eventually failed. / Finally, we shipped."),
        ("sensible / sensitive", "sensible=reasonable; sensitive=easily affected/confidential", "sensible default / sensitive data"),
        ("historic / historical", "historic=important in history; historical=related to the past", "historic launch / historical data"),
        ("economic / economical", "economic=economy-related; economical=money-saving", "economic impact / economical plan"),
        ("raise / rise", "raise=transitive; rise=intransitive", "raise prices / prices rise"),
        ("lie / lay", "lie=recline; lay=put (object)", "lie down / lay the cable"),
        ("principal / principle", "principal=main/head; principle=rule", "principal engineer / a principle"),
        ("complement / compliment", "complete vs praise", "subject complement / nice compliment"),
        ("ensure / insure / assure", "make certain / insurance / reassure a person", "ensure backups; insure a car; assure the client"),
        ("imply / infer", "speaker hints / listener concludes", "The email implies… / We inferred…"),
        ("practice / practise", "AmE: practice for noun & verb", "practice coding (AmE)"),
        ("maybe / may be", "maybe=adv; may be=verb phrase", "Maybe later. / It may be ready."),
        ("every day / everyday", "every day=each day; everyday=ordinary (adj)", "every day / everyday tasks"),
        ("few / a few", "few=negative; a few=some", "Few tests failed. / A few tests failed."),
        ("in time / on time", "before too late / punctual", "in time to fix it / on time for standup"),
        ("at the end / in the end", "at finishing point / finally", "at the end of the call / in the end we rolled back"),
    ]
    for title, diff, ex in pairs:
        s.append(f'<div class="rule-block"><div class="rule-head"><h4>{title}</h4></div><p>{diff}</p>{examples(ex)}</div>')
    s.append(part_footer())
    return "\n".join(s)


def parts_17_to_22():
    return "\n".join([part_17(), part_18(), part_19(), part_20(), part_21(), part_22()])
