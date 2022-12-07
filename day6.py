from dataclasses import dataclass
from pathlib import Path

from aoc2022.day6.input import Input


@dataclass
class Day6:
    input: Input

    def main(self):
        buffer = self.input.get_buffer()
        print(buffer.get_start_of_packet_marker(4))
        print(buffer.get_start_of_packet_marker(14))


if __name__ == "__main__":
    Day6(input=Input(Path("./aoc2022/day6/input.txt"))).main()
