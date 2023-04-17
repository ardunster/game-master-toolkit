import random
import re
from dataclasses import dataclass
from typing import Union

from game_master_toolkit.common_utils.regex_constants import dice_notation


class InvalidDiceError(Exception):
    pass


def split_dice(dice_str: str):
    dice_str = dice_str.lower()
    if not dice_notation.match(dice_str):
        raise InvalidDiceError(
            f"Invalid Dice string: {dice_str}. Accepted values include numbers, "
            f"such as '1', rolls such as '2d4', and rolls with modifier such as "
            f"'3d6+1'."
        )
    split_d = dice_str.split("d")
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
    def __init__(self, dice: Union[str, Dice]):
        if isinstance(dice, Dice):
            self.dice = dice
        elif isinstance(dice, str):
            self.dice = split_dice(dice)
        else:
            raise InvalidDiceError()
        self.modifier = self.dice.modifier
        self.rolls = []
        self.total = self.roll()

    def roll(self):
        self.rolls = []
        if self.dice.die == 1:
            self.rolls.append(self.dice.quantity)
        else:
            for roll in range(self.dice.quantity):
                self.rolls.append(random.choice(range(1, self.dice.die)))
        return sum(self.rolls) + self.modifier
