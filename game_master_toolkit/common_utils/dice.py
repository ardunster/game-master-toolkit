from dataclasses import dataclass


def split_dice(dice: str):
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
