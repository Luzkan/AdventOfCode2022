from dataclasses import dataclass
from pathlib import Path
from typing import Type

from aoc2022.day2.rock_paper_scissors_game import RockPaperScissorsGame
from aoc2022.day2.strategy import Strategy
from aoc2022.day2.utils import OpponentChoice, OurChoice


@dataclass
class Input:
    path: Path

    def parse_file_with_strategy(self, strategy: Type[Strategy]) -> list[RockPaperScissorsGame]:
        return [strategy(*self._parse_line(line)).init_game() for line in self.file_contents]

    def _parse_line(self, line: str) -> tuple[OpponentChoice, OurChoice]:
        return line.split(' ')  # type: ignore

    @property
    def file_contents(self) -> list[str]:
        with open(self.path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
