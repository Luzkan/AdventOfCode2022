from dataclasses import dataclass
from pathlib import Path

from aoc2022.day4.elf_pair import ElfPair


@dataclass
class Input:
    path: Path

    def parse_file_to_elf_pair_assigments(self) -> list[ElfPair]:
        return [ElfPair.from_string(line) for line in self.file_contents]

    @property
    def file_contents(self) -> list[str]:
        with open(self.path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
