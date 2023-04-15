import re

dice_notation = re.compile(r"^[0-9]+(d([1234568]|10|12|20|100))?(\\+[0-9]+)?$")
"""Matches dice roll notations such as 1, 2d6, 4d4+2, etc."""
