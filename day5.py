from dataclasses import dataclass
from pathlib import Path

from aoc2022.day5.crane import Crane
from aoc2022.day5.input import Input


@dataclass
class Day5:
    input: Input

    def main(self):
        crane = Crane(self.input.get_stacks(9), self.input.get_commands())
        # crane.execute_commands_9000()
        crane.execute_commands_9001()
        print(crane.get_top_block_of_each_stack())


if __name__ == "__main__":
    Day5(input=Input(Path("./aoc2022/day5/input.txt"))).main()
