import pytest

from game_master_toolkit.common_utils.json_parser import JsonParser
from game_master_toolkit.encounters.encounter_tool import EncounterTool


class TestEncounterTool:
    dungeon_json = [
        {"name": "goblin", "frequency": "common", "quantity": "2d4"},
        {"name": "roper", "frequency": "rare", "quantity": "1"},
    ]
    forest_json = [
        {"name": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
        {
            "name": "centaur",
            "frequency": "uncommon",
            "quantity": "2d6",
            "description": "A small herd of centaurs canters into view, "
            "clearly dressed as a scouting party.",
        },
    ]

    @pytest.fixture
    def mock_json_parser(self, mocker):
        mock = mocker.MagicMock(spec=JsonParser)
        mock.read_files.return_value = [
            {"dungeon": self.dungeon_json},
            {"forest": self.forest_json},
        ]
        return mock

    def test_encounter_tool_loads_default_encounters(self, mock_json_parser, tmp_path):
        encounter_tool = EncounterTool(tmp_path)
        mock_json_parser.assert_called_once_with("encounters", "default", "tmp_path")
