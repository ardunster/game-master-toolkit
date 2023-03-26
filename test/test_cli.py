from game_master_toolkit import cli


def test_parse_selection_encounters():
    assert cli.parse_selection("1") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection(1) == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("E") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("e") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("en") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("enc") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("encount") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("encounter") == cli.LoadInterface.ENCOUNTERS
    assert cli.parse_selection("encounters") == cli.LoadInterface.ENCOUNTERS


def test_parse_selection_no_match():
    assert cli.parse_selection("steve") == cli.LoadInterface.ERROR
    assert cli.parse_selection("potato") == cli.LoadInterface.ERROR
    assert cli.parse_selection("no words here") == cli.LoadInterface.ERROR
    assert cli.parse_selection("qwit") == cli.LoadInterface.ERROR
    assert cli.parse_selection("salido") == cli.LoadInterface.ERROR
    assert cli.parse_selection(17) == cli.LoadInterface.ERROR
    assert cli.parse_selection("nyanyanyanya") == cli.LoadInterface.ERROR
