import random
import re
from dataclasses import dataclass

from game_master_toolkit.common_utils.regex_constants import dice_notation


def split_dice(dice: str):
    dice = dice.lower()
    assert dice_notation.match(dice) is not None
    split_d = dice.split("d")
    if len(split_d) == 1:
        quantity = int(split_d[0])
        die = 1
        modifier = 0
    else:
        split_plus = re.split(r"[+-]", split_d[1])
        die = int(split_plus[0])
        quantity = int(split_d[0])
        if len(split_plus) == 1:
            modifier = 0
        else:
            modifier = int(split_plus[1])
            if "-" in split_d[1]:
                modifier = -modifier
    return Dice(quantity, die, modifier)


@dataclass
class Dice:
    quantity: int
    die: int
    modifier: int


class Roll:
    # TODO: Make this take a Dice as an argument too
    def __init__(self, dice: str):
        self._dice = split_dice(dice)
        self.modifier = self._dice.modifier
        self.rolls = []
        self.total = self.roll()

    def roll(self):
        self.rolls = []
        if self._dice.die == 1:
            self.rolls.append(self._dice.quantity)
        else:
            for roll in range(self._dice.quantity):
                self.rolls.append(random.choice(range(1, self._dice.die)))
        return sum(self.rolls) + self.modifier
