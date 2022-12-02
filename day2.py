from dataclasses import dataclass
from pathlib import Path

from aoc2022.day2.input import Input
from aoc2022.day2.rock_paper_scissors_game import RockPaperScissorsGame
from aoc2022.day2.strategy1 import Strategy1
from aoc2022.day2.strategy2 import Strategy2


@dataclass
class StrategyEvaluator:
    games: list[RockPaperScissorsGame]

    @property
    def total_points(self) -> int:
        return sum(game.points_for_outcome + game.points_for_pick for game in self.games)


@dataclass
class Day2:
    input: Input

    def main(self):
        print(f"{StrategyEvaluator(self.input.parse_file_with_strategy(Strategy1)).total_points}")
        print(f"{StrategyEvaluator(self.input.parse_file_with_strategy(Strategy2)).total_points}")


if __name__ == "__main__":
    Day2(input=Input(Path("./aoc2022/day2/input.txt"))).main()
