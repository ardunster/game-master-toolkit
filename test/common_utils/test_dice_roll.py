import pytest

from game_master_toolkit.common_utils.dice import Dice, InvalidDiceError, Roll


def test_die_roll_number_only():
    roll_1 = Roll("1")
    assert roll_1.dice == Dice(1, 1, 0)
    assert roll_1.rolls == [1]
    assert roll_1.total == 1
    assert roll_1.modifier == 0

    roll_14 = Roll("14")
    assert roll_14.dice == Dice(14, 1, 0)
    assert roll_14.rolls == [14]
    assert roll_14.total == 14
    assert roll_14.modifier == 0

    roll_27 = Roll("27")
    assert roll_27.dice == Dice(27, 1, 0)
    assert roll_27.rolls == [27]
    assert roll_27.total == 27
    assert roll_27.modifier == 0


@pytest.mark.parametrize(
    "input_dice,expected_dice,mock_rolls,expected_total",
    [
        pytest.param("3d6", Dice(3, 6, 0), [3, 4, 5], 12),
        pytest.param("2d4", Dice(2, 4, 0), [2, 4], 6),
        pytest.param("5d20", Dice(5, 20, 0), [1, 2, 3, 5, 8], 19),
        pytest.param("1d10+1", Dice(1, 10, 1), [8], 9),
        pytest.param("3d8-2", Dice(3, 8, -2), [8, 4, 4], 14),
    ],
)
def test_die_roll_with_die(
    mocker, input_dice: str, expected_dice: Dice, mock_rolls, expected_total
):
    mocker.patch("random.choice", side_effect=mock_rolls)
    roll = Roll(input_dice)
    assert roll.dice == expected_dice
    assert roll.rolls == mock_rolls
    assert roll.total == expected_total
    assert roll.modifier == expected_dice.modifier


@pytest.mark.parametrize(
    "dice",
    [Dice(3, 6, 0), Dice(2, 4, 0), Dice(5, 20, 0), Dice(1, 10, 1), Dice(3, 8, -2)],
)
def test_roll_with_dice_class(dice):
    roll = Roll(dice)
    assert roll.dice == dice


def test_roll_invalid_input_type():
    with pytest.raises(InvalidDiceError):
        Roll(17)

    with pytest.raises(InvalidDiceError):
        Roll({"key": "value"})
