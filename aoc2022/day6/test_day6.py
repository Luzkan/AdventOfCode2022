from dataclasses import dataclass
from pathlib import Path

from aoc2022.day6.buffer import Buffer
from aoc2022.day6.input import Input
from pytest import fixture


@dataclass
class Res:
    length: int
    first_marker_position: int


Sample = tuple[Buffer, Res]


class TestDay6:
    @fixture
    def test_input(self) -> Input:
        return Input(Path("./aoc2022/day6/test_input.txt"))

    @fixture
    def samples(self) -> list[Sample]:
        return [
            (Buffer('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), Res(4, 7)),
            (Buffer('bvwbjplbgvbhsrlpgdmjqwftvncz'), Res(4, 5)),
            (Buffer('nppdvjthqldpwncqszvftbrmjlhg'), Res(4, 6)),
            (Buffer('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), Res(4, 10)),
            (Buffer('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), Res(4, 11))
        ]

    def test_finding_idx_start_of_packet_marker(self, samples: list[Sample]):
        for sample in samples:
            assert sample[0].get_start_of_packet_marker(sample[1].length) == sample[1].first_marker_position
