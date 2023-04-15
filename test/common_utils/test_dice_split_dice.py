from game_master_toolkit.common_utils.dice import Dice, split_dice


def test_split_dice_number_only():
    assert split_dice("1") == Dice(1, 1, 0)
    assert split_dice("12") == Dice(12, 1, 0)
    assert split_dice("17") == Dice(17, 1, 0)


def test_split_with_dice():
    pass
