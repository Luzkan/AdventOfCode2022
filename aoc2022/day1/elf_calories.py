from dataclasses import dataclass
from typing import Iterable


@dataclass
class ElfCalories:
    values: list[int]

    @property
    def total(self) -> int:
        return sum(self.values)

    def __lt__(self, other: 'ElfCalories') -> bool:
        return self.total < other.total

    @staticmethod
    def init_from_list_of_str(values: Iterable[str]) -> 'ElfCalories':
        return ElfCalories([int(value) for value in values])
