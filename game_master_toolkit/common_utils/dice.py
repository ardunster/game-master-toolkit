class Roll:
    def __init__(self, dice):
        self.dice = dice
        self.rolls = [int(dice)]
        self.total = int(dice)
        self.modifier = None
