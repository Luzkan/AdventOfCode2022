from dataclasses import dataclass
from functools import reduce

from aoc2022.day3.rucksack import Rucksack


@dataclass
class ElfGroup:
    elfs_rucksacks: list[Rucksack]

    @property
    def shared_item(self) -> str:
        if (common_element := next(iter(reduce(lambda x, y: x & y, [set(r.items) for r in self.elfs_rucksacks])))):
            return common_element
        raise ValueError("Could not find common element in rucksacks.")
