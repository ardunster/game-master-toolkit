from game_master_toolkit.common_utils.dice import Dice, Roll


def test_die_roll_number_only():
    roll_1 = Roll("1")
    assert roll_1._dice == Dice(1, 1, 0)
    assert roll_1.rolls == [1]
    assert roll_1.total == 1
    assert roll_1.modifier == 0

    roll_14 = Roll("14")
    assert roll_14._dice == Dice(14, 1, 0)
    assert roll_14.rolls == [14]
    assert roll_14.total == 14
    assert roll_14.modifier == 0

    roll_27 = Roll("27")
    assert roll_27._dice == Dice(27, 1, 0)
    assert roll_27.rolls == [27]
    assert roll_27.total == 27
    assert roll_27.modifier == 0


def test_die_roll_with_die(mocker):
    mock_rolls = [3, 4, 5]
    mocker.patch("random.randint", return_values=mock_rolls)
    # assert roll("3d6") == {"rolls": mock_rolls, "total": 11}
    pass
