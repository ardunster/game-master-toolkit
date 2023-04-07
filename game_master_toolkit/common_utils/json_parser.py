import json
from pathlib import Path

from jsonschema import validate


class JsonParser:
    def __init__(self, tool, dataset, filesystem: Path):
        self.tool = tool
        self.dataset = dataset
        self.filesystem = filesystem

    def read_files(self, filenames: list[str]):
        data = {}
        schema_filename = f"{self.tool}.schema.json"
        schema_path = (
            self.filesystem
            / "game_master_toolkit"
            / "common_utils"
            / f"schemas/{schema_filename}"
        )
        with schema_path.open() as f:
            schema = json.load(f)
        for filename in filenames:
            file_path = (
                self.filesystem
                / "game_master_toolkit"
                / self.tool
                / "data"
                / self.dataset
                / f"{filename}.json"
            )
            with file_path.open() as f:
                file_data = json.load(f)
                validate(instance=file_data, schema=schema)
                data[filename] = file_data
        return data
