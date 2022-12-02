from dataclasses import dataclass

from aoc2022.day2.rock_paper_scissors_game import RockPaperScissorsGame
from aoc2022.day2.strategy import Strategy
from aoc2022.day2.utils import (OpponentChoice, OurChoice, Outcome,
                                RockPaperScissors)


@dataclass
class Strategy2(Strategy):
    def init_game(self):
        return RockPaperScissorsGame(
            player1=self.choose_our_hand(),
            player2=self.remap_to_rock_paper_scissors(self.opponent)
        )

    def choose_our_hand(self) -> RockPaperScissors:
        strategy: dict[tuple[Outcome, RockPaperScissors], RockPaperScissors] = {
            ("Win", "Rock"): "Paper",
            ("Draw", "Rock"): "Rock",
            ("Lose", "Rock"): "Scissors",
            ("Win", "Paper"): "Scissors",
            ("Draw", "Paper"): "Paper",
            ("Lose", "Paper"): "Rock",
            ("Win", "Scissors"): "Rock",
            ("Draw", "Scissors"): "Scissors",
            ("Lose", "Scissors"): "Paper"
        }
        return strategy[
            (self.remap_to_outcome(self.our), self.remap_to_rock_paper_scissors(self.opponent))
        ]

    @staticmethod
    def remap_to_rock_paper_scissors(value: OpponentChoice) -> RockPaperScissors:
        remapping: dict[OpponentChoice, RockPaperScissors] = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors"
        }
        return remapping[value]

    @staticmethod
    def remap_to_outcome(value: OurChoice) -> Outcome:
        remapping: dict[OurChoice, Outcome] = {
            "X": "Lose",
            "Y": "Draw",
            "Z": "Win"
        }
        return remapping[value]
