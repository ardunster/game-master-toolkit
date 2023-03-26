from game_master_toolkit.encounters import encounters


def test_sample_encounter():
    assert encounters.sample_encounters() == "Encounter"
