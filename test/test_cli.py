from game_master_toolkit import cli


def test_parse_selection_encounters():
    assert cli.parse_selection("1") == 1
    assert cli.parse_selection(1) == 1
    assert cli.parse_selection("E") == 1
    assert cli.parse_selection("e") == 1
    assert cli.parse_selection("en") == 1
    assert cli.parse_selection("enc") == 1
    assert cli.parse_selection("encount") == 1
    assert cli.parse_selection("encounter") == 1
    assert cli.parse_selection("encounters") == 1


def test_parse_selection_no_match():
    assert cli.parse_selection("steve") == -1
    assert cli.parse_selection("potato") == -1
    assert cli.parse_selection("no words here") == -1
    assert cli.parse_selection("qwit") == -1
    assert cli.parse_selection("salido") == -1
    assert cli.parse_selection(17) == -1
    assert cli.parse_selection("nyanyanyanya") == -1
