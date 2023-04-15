from dataclasses import dataclass


def split_dice(dice: str):
    return Dice(int(dice), 1, 0)


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
