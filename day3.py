from dataclasses import dataclass
from pathlib import Path

from aoc2022.day3.elf_group import ElfGroup
from aoc2022.day3.input import Input
from aoc2022.day3.prioritizer import Prioritizer
from aoc2022.day3.rucksack import Rucksack
from aoc2022.day3.test_day3 import TestDay3


@dataclass
class Day3:
    input: Input

    def main(self):
        rucksacks: list[Rucksack] = self.input.parse_file_to_rucksacks()
        rucksacks_groups: list[ElfGroup] = self.input.parse_file_to_rucksacks_group_of(3)
        print(self.sum_of_shared_item_priorities(rucksacks))
        print(self.sum_of_shared_item_priorities(rucksacks_groups))

    @staticmethod
    def sum_of_shared_item_priorities(rucksacks: list[Rucksack] | list[ElfGroup]) -> int:
        return sum(Prioritizer.prioritize(r.shared_item) for r in rucksacks)


if __name__ == "__main__":
    TestDay3().run_all()
    Day3(input=Input(Path("./aoc2022/day3/input.txt"))).main()
