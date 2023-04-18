from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

from game_master_toolkit.common_utils.dice import Dice
from game_master_toolkit.common_utils.json_parser import JsonParser


@dataclass
class EncounterEntry:
    name: str
    frequency: Literal["common", "uncommon", "rare", "very rare"]
    quantity: Dice
    description: Optional[str] = None


class EncounterTool:
    def __init__(self, filesystem: Path, dataset="default"):
        self.dataset = dataset
        json_parser = JsonParser("encounters", self.dataset, filesystem)
