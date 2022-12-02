from dataclasses import dataclass

from aoc2022.day2.rock_paper_scissors_game import RockPaperScissorsGame
from aoc2022.day2.utils import OpponentChoice, OurChoice


@dataclass
class Strategy:
    opponent: OpponentChoice
    our: OurChoice
    
    def init_game(self) -> RockPaperScissorsGame:
        raise NotImplementedError
