import json
import shutil
from pathlib import Path

import pytest
from jsonschema.exceptions import ValidationError

from game_master_toolkit.common_utils.json_parser import JsonParser


class TestJsonParser:
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
    def mock_file_system(self, tmp_path):
        gmtk_dir = tmp_path / "game_master_toolkit"
        gmtk_dir.mkdir(parents=True)
        data_dir = gmtk_dir / "encounters" / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        default_data_dir = data_dir / "default"
        default_data_dir.mkdir(parents=True, exist_ok=True)
        (default_data_dir / "dungeon.json").write_text(json.dumps(self.dungeon_json))
        (default_data_dir / "forest.json").write_text(json.dumps(self.forest_json))
        (default_data_dir / "fail1.json").write_text(
            json.dumps(
                [
                    {"steve": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
                    {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
                ]
            )
        )
        (default_data_dir / "fail2.json").write_text(
            json.dumps(
                {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
            )
        )
        actual_path_of_encounters_schema = Path(
            "./game_master_toolkit/encounters/data/encounters.schema.json"
        )
        shutil.copy(actual_path_of_encounters_schema, data_dir)
        yield tmp_path

    def test_json_parser(self, mock_file_system):
        biome = "dungeon"
        parser = JsonParser("encounters", "default", mock_file_system)
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[0][biome] == self.dungeon_json
        biome = "forest"
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[0][biome] == self.forest_json
        biomes = ["forest", "dungeon"]
        data = parser.read_files(biomes)
        assert len(data) == 2
        assert data[0][biomes[0]] == self.forest_json
        assert data[1][biomes[1]] == self.dungeon_json

    def test_json_parser_schema_failure(self, mock_file_system):
        parser = JsonParser("encounters", "default", mock_file_system)
        biome = "fail1"
        with pytest.raises(ValidationError):
            parser.read_files([biome])

        biome = "fail2"
        with pytest.raises(ValidationError):
            parser.read_files([biome])

    def test_read_files_with_invalid_tool(self, mock_file_system):
        parser = JsonParser("invalid_tool", "default", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["dungeon"])

    def test_read_files_with_invalid_dataset(self, mock_file_system):
        parser = JsonParser("encounters", "invalid_dataset", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["dungeon"])

    def test_read_files_with_invalid_filename(self, mock_file_system):
        parser = JsonParser("encounters", "default", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["invalid_filename"])
