from dataclasses import dataclass
from pathlib import Path

from aoc2022.day4.elf_pair import ElfPair
from aoc2022.day4.input import Input


@dataclass
class Day4:
    input: Input

    def main(self):
        elf_pairs: list[ElfPair] = self.input.parse_file_to_elf_pair_assigments()
        print(sum(1 for elf_pair in elf_pairs if elf_pair.is_fully_overlapping()))
        print(sum(1 for elf_pair in elf_pairs if elf_pair.is_overlapping()))


if __name__ == "__main__":
    Day4(input=Input(Path("./aoc2022/day4/input.txt"))).main()
