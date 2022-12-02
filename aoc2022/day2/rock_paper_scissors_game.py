from dataclasses import dataclass

from aoc2022.day2.utils import Outcome, RockPaperScissors


@dataclass
class RockPaperScissorsGame:
    """ Calculates points from the perspective of the player1. """
    player1: RockPaperScissors
    player2: RockPaperScissors

    @property
    def outcome(self) -> Outcome:
        outcomes: dict[tuple[RockPaperScissors, RockPaperScissors], Outcome] = {
            ("Rock", "Scissors"): "Win",
            ("Paper", "Rock"): "Win",
            ("Scissors", "Paper"): "Win",
            ("Rock", "Rock"): "Draw",
            ("Paper", "Paper"): "Draw",
            ("Scissors", "Scissors"): "Draw",
            ("Rock", "Paper"): "Lose",
            ("Paper", "Scissors"): "Lose",
            ("Scissors", "Rock"): "Lose",
        }
        return outcomes[(self.player1, self.player2)]

    @property
    def points_for_outcome(self) -> int:
        points_table: dict[Outcome, int] = {
            "Win": 6,
            "Draw": 3,
            "Lose": 0
        }
        return points_table[self.outcome]

    @property
    def points_for_pick(self) -> int:
        points_table: dict[RockPaperScissors, int] = {
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3
        }
        return points_table[self.player1]
