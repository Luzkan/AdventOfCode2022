from dataclasses import dataclass

from aoc2022.day1.elf_calories import ElfCalories


@dataclass
class ElfDiets:
    elf_calories: list[ElfCalories]

    def __post_init__(self):
        self.elf_calories.sort(reverse=True)

    def get_highest_calorie_diet_number(self) -> int:
        return max(self.elf_calories).total

    def sum_hungriest_elfs_calories(self, number_of_hungriest_elves: int) -> int:
        return sum(elf.total for elf in self.elf_calories[:number_of_hungriest_elves])
