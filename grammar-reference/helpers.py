"""HTML helpers for grammar reference content."""


def badge(*levels):
    bits = [f'<span class="badge badge-{lv.lower()}">{lv}</span>' for lv in levels]
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


def rule(title, definition, form="", when=None, examples_list=None, mistakes_list=None,
         compare_html="", advanced_html="", levels=None, extra=""):
    parts = ['<div class="rule-block">']
    head = [f'<div class="rule-head"><h4>{title}</h4>']
    if levels:
        head.append(badge(*levels))
    head.append("</div>")
    parts.append("".join(head))
    parts.append(f'<p>{definition}</p>')
    if form:
        parts.append(f'<p class="label">Form</p><p class="form-pattern">{form}</p>')
    if when:
        items = "".join(f"<li>{x}</li>" for x in when)
        parts.append(f'<p class="label">When to use it</p><ul>{items}</ul>')
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
