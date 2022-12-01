from dataclasses import dataclass
from itertools import groupby
from pathlib import Path

from aoc2022.day1.elf_calories import ElfCalories


@dataclass
class Input:
    path: Path

    def parse_file(self) -> list[ElfCalories]:
        return [
            ElfCalories.init_from_list_of_str(calorie_values)
            for line, calorie_values
            in groupby(self.file_contents, key=bool)
            if line
        ]

    @property
    def file_contents(self) -> list[str]:
        with open(self.path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
