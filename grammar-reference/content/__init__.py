"""Assemble all grammar reference parts."""
import re

from content.parts_01_08 import parts_1_to_8
from content.parts_09_16 import parts_9_to_16
from content.parts_17_26 import parts_17_to_26
from content.parts_27_34 import parts_27_to_34
from content.extra_depth import expand


def _inject_expansions(html: str) -> str:
    def repl(match: re.Match) -> str:
        num = int(match.group(1))
        block = match.group(0)
        extra = expand(num)
        if not extra:
            return block
        if block.endswith("</section>"):
            return block[: -len("</section>")] + extra + "\n</section>"
        return block

    return re.sub(
        r'<section class="part" id="part-(\d\d)"[\s\S]*?</section>',
        repl,
        html,
    )


def all_parts():
    html = "\n".join(
        [
            parts_1_to_8(),
            parts_9_to_16(),
            parts_17_to_26(),
            parts_27_to_34(),
        ]
    )
    return _inject_expansions(html)
