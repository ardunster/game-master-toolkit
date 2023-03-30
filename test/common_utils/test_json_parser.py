from game_master_toolkit.common_utils import json_parser


def test_validate_schema_encounter_valid():
    assert json_parser.validate_schema("filename", "encounter")


def test_validate_schema_encounter_invalid():
    assert not json_parser.validate_schema("bad_filename", "encounter")
