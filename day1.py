from dataclasses import dataclass
from pathlib import Path

from aoc2022.day1.elf_diets import ElfDiets
from aoc2022.day1.input import Input


@dataclass
class Day1:
    input: Input

    def main(self):
        elf_calories: ElfDiets = ElfDiets(self.input.parse_file())
        print(f"Part #1: {elf_calories.get_highest_calorie_diet_number()}")
        print(f"Part #2: {elf_calories.sum_hungriest_elfs_calories(3)}")


if __name__ == "__main__":
    Day1(input=Input(Path("./aoc2022/day1/input.txt"))).main()
