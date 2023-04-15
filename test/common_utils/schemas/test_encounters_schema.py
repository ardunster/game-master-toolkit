import json
from pathlib import Path

import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema_path = Path(
    Path.cwd()
    / "game_master_toolkit"
    / "common_utils"
    / "schemas/encounters.schema.json"
)

with schema_path.open() as f:
    schema = json.load(f)


def test_success():
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
    try:
        validate(instance=dungeon_json, schema=schema)
        validate(instance=forest_json, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Encounter schema validation raised an exception: {e}")


def test_fails_invalid_field():
    fail_invalid_field = [
        {"steve": "gnoll", "frequency": "uncommon", "quantity": "2d6"},
        {"name": "centaur", "frequency": "uncommon", "quantity": "2d6"},
    ]

    with pytest.raises(ValidationError):
        validate(instance=fail_invalid_field, schema=schema)


def test_fails_invalid_object():
    fail_invalid_object = {
        "name": "centaur",
        "frequency": "uncommon",
        "quantity": "2d6",
    }

    with pytest.raises(ValidationError):
        validate(instance=fail_invalid_object, schema=schema)


def test_fails_invalid_value():
    fail_invalid_value = [
        {"name": "steve", "frequency": "pistachio", "quantity": "lemon"}
    ]

    with pytest.raises(ValidationError):
        validate(instance=fail_invalid_value, schema=schema)
