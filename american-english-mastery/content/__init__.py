"""Assemble all American English Mastery parts."""
from content.parts_01_08 import parts_1_to_8
from content.parts_09_16 import parts_9_to_16
from content.parts_17_22 import parts_17_to_22
from content.parts_23_30 import parts_23_to_30
from content.parts_31_38 import parts_31_to_38


def all_parts():
    return "\n".join(
        [
            parts_1_to_8(),
            parts_9_to_16(),
            parts_17_to_22(),
            parts_23_to_30(),
            parts_31_to_38(),
        ]
    )
