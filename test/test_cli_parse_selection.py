from game_master_toolkit import cli


def test_parse_selection_no_match():
    assert cli.parse_selection("steve") == cli.LoadInterface.ERROR
    assert cli.parse_selection("potato") == cli.LoadInterface.ERROR
    assert cli.parse_selection("no words here") == cli.LoadInterface.ERROR
    assert cli.parse_selection("qwit") == cli.LoadInterface.ERROR
    assert cli.parse_selection("salido") == cli.LoadInterface.ERROR
    assert cli.parse_selection(17) == cli.LoadInterface.ERROR
    assert cli.parse_selection("nyanyanyanya") == cli.LoadInterface.ERROR


def test_parse_selection_quit():
    assert cli.parse_selection("q") == cli.LoadInterface.QUIT
    assert cli.parse_selection("quit") == cli.LoadInterface.QUIT
    assert cli.parse_selection("exit") == cli.LoadInterface.QUIT
    assert cli.parse_selection("EXIT") == cli.LoadInterface.QUIT
    assert cli.parse_selection("QUIT") == cli.LoadInterface.QUIT
    assert cli.parse_selection("Q") == cli.LoadInterface.QUIT
    assert cli.parse_selection("x") == cli.LoadInterface.QUIT


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


def test_parse_selection_something_else():
    assert cli.parse_selection("2") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection(2) == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("S") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("s") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("so") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("some") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("somethi") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("something") == cli.LoadInterface.SOMETHING_ELSE
    assert cli.parse_selection("something else") == cli.LoadInterface.SOMETHING_ELSE
