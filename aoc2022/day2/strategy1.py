from dataclasses import dataclass

from aoc2022.day2.rock_paper_scissors_game import RockPaperScissorsGame
from aoc2022.day2.strategy import Strategy
from aoc2022.day2.utils import OpponentChoice, OurChoice, RockPaperScissors


@dataclass
class Strategy1(Strategy):
    def init_game(self):
        return RockPaperScissorsGame(
            player1=self.remap_name(self.our),
            player2=self.remap_name(self.opponent)
        )
    
    @staticmethod
    def remap_name(value: OpponentChoice | OurChoice) -> RockPaperScissors:
        remapping: dict[OpponentChoice | OurChoice, RockPaperScissors] = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors",
            "X": "Rock",
            "Y": "Paper",
            "Z": "Scissors"
        }
        return remapping[value]
    