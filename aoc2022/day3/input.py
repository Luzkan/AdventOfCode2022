from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
from typing import Iterable

from aoc2022.day3.elf_group import ElfGroup
from aoc2022.day3.rucksack import Rucksack


def grouper(iterable: Iterable, group_length: int):
    args = [iter(iterable)] * group_length
    return zip_longest(*args, fillvalue=None)


@dataclass
class Input:
    path: Path

    def parse_file_to_rucksacks_group_of(self, number: int) -> list[ElfGroup]:
        groups = grouper(self.parse_file_to_rucksacks(), number)
        return [ElfGroup(elfs_rucksacks=list(group)) for group in groups if group is not None]

    def parse_file_to_rucksacks(self) -> list[Rucksack]:
        return [Rucksack(items=line) for line in self.file_contents]

    @property
    def file_contents(self) -> list[str]:
        with open(self.path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
