"""HTML helpers for American English Mastery Reference."""


def badge(*levels):
    bits = [f'<span class="badge badge-{lv.lower().replace("/", "-")}">{lv}</span>' for lv in levels]
    return f'<div class="levels">{"".join(bits)}</div>'


def box(kind, title, body):
    return f'''<div class="box box-{kind}">
  <p class="box-title">{title}</p>
  {body}
</div>'''


def examples(*items):
    lis = "\n".join(f"<li>{i}</li>" for i in items)
    return box("example", "Examples", f'<ul class="ex-list">\n{lis}\n</ul>')


def mistakes(*pairs):
    rows = []
    for p in pairs:
        if len(p) == 2:
            w, c = p
            rows.append(f'<p><span class="wrong">{w}</span> → <span class="correct">{c}</span></p>')
        else:
            w, c, n = p
            rows.append(
                f'<p><span class="wrong">{w}</span> → <span class="correct">{c}</span>'
                f'<br><span style="color:var(--muted);font-size:0.9em">{n}</span></p>'
            )
    return box("mistake", "Common mistakes", "\n".join(rows))


def compare(body):
    return box("compare", "Compare", body)


def note(body, title="Note"):
    return box("note", title, body)


def warning(body, title="Warning"):
    return box("warning", title, body)


def advanced(body, title="Advanced note"):
    return box("advanced", title, body)


def pron_box(body, title="Pronunciation"):
    return box("example", title, body)


def rule(title, definition, form="", when=None, examples_list=None, mistakes_list=None,
         compare_html="", advanced_html="", levels=None, extra=""):
    parts = ['<div class="rule-block">']
    head = [f'<div class="rule-head"><h4>{title}</h4>']
    if levels:
        head.append(badge(*levels))
    head.append("</div>")
    parts.append("".join(head))
    parts.append(f"<p>{definition}</p>")
    if form:
        parts.append(f'<p class="label">Form / Pattern</p><p class="form-pattern">{form}</p>')
    if when:
        items = "".join(f"<li>{x}</li>" for x in when)
        parts.append(f'<p class="label">When / How</p><ul>{items}</ul>')
    if examples_list:
        parts.append(examples(*examples_list))
    if mistakes_list:
        parts.append(mistakes(*mistakes_list))
    if compare_html:
        parts.append(compare(compare_html))
    if advanced_html:
        parts.append(advanced(advanced_html))
    if extra:
        parts.append(extra)
    parts.append("</div>")
    return "\n".join(parts)


def table(headers, rows, caption=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = []
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body.append(f"<tr>{tds}</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'''<div class="table-wrap"><table>
{cap}
<thead><tr>{th}</tr></thead>
<tbody>
{"".join(body)}
</tbody>
</table></div>'''


def part_header(num, title, intro):
    return f'''<section class="part" id="part-{num:02d}" data-part="{num}">
<header class="part-header">
  <p class="part-number">Part {num}</p>
  <h2 class="part-title">{title}</h2>
  <p class="part-intro">{intro}</p>
</header>
'''


def part_footer():
    return "</section>\n"


def h3(text, anchor=None):
    if anchor:
        return f'<h3 id="{anchor}">{text}</h3>'
    return f"<h3>{text}</h3>"


def p(text):
    return f"<p>{text}</p>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def vocab_card(e):
    """Render a vocabulary entry dict as an HTML card."""
    wid = e.get("id") or e["word"].lower().replace(" ", "-").replace("/", "-")
    reg = e.get("register", "neutral")
    lvl = e.get("level", "")
    arabic = e.get("arabic", "")
    ipa = e.get("ipa", "")
    stress = e.get("stress", "")
    cols = e.get("collocations") or []
    patterns = e.get("patterns") or []
    related = e.get("related") or []
    mistake = e.get("mistake", "")
    example = e.get("example", "")
    meaning = e.get("meaning", "")
    pos = e.get("pos", "")

    col_html = ""
    if cols:
        col_html = "<p class='label'>Collocations</p><p>" + " · ".join(f"<em>{c}</em>" for c in cols) + "</p>"
    pat_html = ""
    if patterns:
        pat_html = "<p class='label'>Patterns</p><p>" + " · ".join(patterns) + "</p>"
    rel_html = ""
    if related:
        rel_html = "<p class='label'>Related</p><p>" + ", ".join(related) + "</p>"
    mist_html = f"<p class='label'>Common mistake</p><p>{mistake}</p>" if mistake else ""
    ar_html = f"<p><strong>Arabic:</strong> {arabic}</p>" if arabic else ""
    stress_html = f" · stress: <em>{stress}</em>" if stress else ""
    ipa_html = f"<span class='ipa'>/{ipa}/</span>" if ipa else ""
    lvl_html = badge(lvl) if lvl else ""
    ex_html = f"<p class='ex'><em>{example}</em></p>" if example else ""

    return f'''<article class="vocab-card" id="v-{wid}">
  <div class="rule-head">
    <h4 class="vocab-word">{e["word"]} <span class="pos">{pos}</span></h4>
    <div class="vocab-meta">{lvl_html}<span class="register">{reg}</span></div>
  </div>
  <p class="vocab-pron">{ipa_html}{stress_html}</p>
  <p>{meaning}</p>
  {ar_html}
  {ex_html}
  {col_html}
  {pat_html}
  {rel_html}
  {mist_html}
</article>'''


def expr_card(e):
    import re
    eid = e.get("id")
    if not eid:
        eid = re.sub(r"[^a-z0-9]+", "-", e["expression"].lower())
        eid = eid.strip("-")[:48]
    alts = e.get("alternatives") or []
    alt_html = ("<p class='label'>Alternatives</p><p>" + " · ".join(alts) + "</p>") if alts else ""
    pron = e.get("pron_note", "")
    pron_html = f"<p class='label'>Spoken note</p><p>{pron}</p>" if pron else ""
    return f'''<article class="expr-card" id="e-{eid}">
  <div class="rule-head">
    <h4>{e["expression"]}</h4>
    <span class="register">{e.get("register", "neutral")}</span>
  </div>
  <p><strong>Meaning:</strong> {e["meaning"]}</p>
  <p><strong>Context:</strong> {e.get("context", "")}</p>
  <p class="ex"><em>{e.get("example", "")}</em></p>
  {alt_html}
  {pron_html}
</article>'''
