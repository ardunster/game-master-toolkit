from dataclasses import dataclass

from game_master_toolkit.common_utils.regex_constants import dice_notation


def split_dice(dice: str):
    dice = dice.lower()
    assert dice_notation.match(dice) is not None
    split_d = dice.split("d")
    if len(split_d) > 1:
        quantity = int(split_d[1])
    else:
        quantity = 1
    return Dice(int(split_d[0]), quantity, 0)


@dataclass
class Dice:
    quantity: int
    die: int
    modifier: int


class Roll:
    def __init__(self, dice: str):
        self.dice = dice
        self.rolls = [int(dice)]
        self.total = int(dice)
        self.modifier = None
