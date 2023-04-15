from game_master_toolkit.common_utils.dice import Dice, split_dice


def test_split_dice_number_only():
    assert split_dice("1") == Dice(1, 1, 0)
    assert split_dice("12") == Dice(12, 1, 0)
    assert split_dice("17") == Dice(17, 1, 0)


def test_split_with_dice():
    assert split_dice("1d1") == Dice(1, 1, 0)
    assert split_dice("1d6") == Dice(1, 6, 0)
    assert split_dice("4d10") == Dice(4, 10, 0)
    assert split_dice("7d8") == Dice(7, 8, 0)
    assert split_dice("12d4") == Dice(12, 4, 0)
