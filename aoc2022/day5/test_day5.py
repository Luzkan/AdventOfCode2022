
from pathlib import Path

from aoc2022.day5.crane import Crane
from aoc2022.day5.input import Input
from pytest import fixture


class TestDay5:
    @fixture
    def test_input(self) -> Input:
        return Input(Path("./aoc2022/day5/test_input.txt"))

    @fixture
    def crane(self, test_input: Input) -> Crane:
        return Crane(test_input.get_stacks(3), test_input.get_commands())

    def test_crane_9000(self, crane: Crane):
        crane.execute_commands_9000()
        assert crane.get_top_block_of_each_stack() == "CMZ"

    def test_crane_9001(self, crane: Crane):
        crane.execute_commands_9001()
        assert crane.get_top_block_of_each_stack() == "MCD"
