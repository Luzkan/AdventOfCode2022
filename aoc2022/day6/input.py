from dataclasses import dataclass
from pathlib import Path

from aoc2022.day6.buffer import Buffer


@dataclass
class Input:
    path: Path

    def get_buffer(self) -> Buffer:
        return Buffer(self.file_contents)

    @property
    def file_contents(self) -> str:
        with open(self.path, "r", encoding='utf-8') as file:
            return file.read()
