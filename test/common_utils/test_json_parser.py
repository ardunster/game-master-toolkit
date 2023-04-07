import json
import shutil
from pathlib import Path

import pytest

from game_master_toolkit.common_utils.json_parser import JsonParser


class TestJsonParser:
    @pytest.fixture
    def mock_file_system(self, tmp_path):
        gmtk_dir = tmp_path / "game_master_toolkit"
        gmtk_dir.mkdir(parents=True)
        data_dir = gmtk_dir / "encounters" / "data" / "default"
        data_dir.mkdir(parents=True, exist_ok=True)
        schema_dir = gmtk_dir / "common_utils" / "schemas"
        schema_dir.mkdir(parents=True, exist_ok=True)
        (data_dir / "dungeon.json").write_text(
            json.dumps(
                [
                    {"name": "goblin", "frequency": "common", "quantity": "2d4"},
                    {"name": "roper", "frequency": "rare", "quantity": "1"},
                ]
            )
        )
        (data_dir / "forest.json").write_text(
            json.dumps(
                [
                    {"name": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
                    {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
                ]
            )
        )
        (data_dir / "fail1.json").write_text(
            json.dumps(
                [
                    {"steve": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
                    {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
                ]
            )
        )
        (data_dir / "fail2.json").write_text(
            json.dumps(
                {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
            )
        )
        actual_path_of_encounters_schema = Path(
            "./game_master_toolkit/common_utils/schemas/encounters.schema.json"
        )
        shutil.copy(actual_path_of_encounters_schema, schema_dir)
        yield tmp_path

    def test_json_parser(self, mock_file_system):
        biome = "dungeon"
        parser = JsonParser("encounters", "default", mock_file_system)
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[biome] == [
            {"name": "goblin", "frequency": "common", "quantity": "2d4"},
            {"name": "roper", "frequency": "rare", "quantity": "1"},
        ]
        biome = "forest"
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[biome] == [
            {"name": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
            {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
        ]

    # TODO: write this test correctly for expected validation failure output
    @pytest.mark.xfail(reason="Incorrect test implementation, TODO")
    def test_json_parser_schema_failure(self, mock_file_system):
        parser = JsonParser("encounters", "default", mock_file_system)
        biome = "fail1"
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[biome] == [
            {"name": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
            {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
        ]
        biome = "fail2"
        data = parser.read_files([biome])
        assert len(data) == 1
        assert data[biome] == [
            {"name": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
            {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
        ]

    # TODO: write this test correctly for expected validation failure output
    @pytest.mark.xfail(reason="Incorrect test implementation, TODO")
    def test_read_files_with_invalid_tool(mock_file_system):
        parser = JsonParser("invalid_tool", "default", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["dungeon"])

    # TODO: write this test correctly for expected validation failure output
    @pytest.mark.xfail(reason="Incorrect test implementation, TODO")
    def test_read_files_with_invalid_dataset(mock_file_system):
        parser = JsonParser("encounters", "invalid_dataset", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["dungeon"])

    # TODO: write this test correctly for expected  failure output
    @pytest.mark.xfail(reason="Incorrect test implementation, TODO")
    def test_read_files_with_invalid_filename(mock_file_system):
        parser = JsonParser("encounters", "default", mock_file_system)
        with pytest.raises(FileNotFoundError):
            parser.read_files(["invalid_filename"])

    def test_json_parser_constructor_params(self):
        pass
