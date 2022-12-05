from dataclasses import dataclass


@dataclass
class Assigment:
    min: int
    max: int

    @staticmethod
    def from_string(value: str) -> 'Assigment':
        min, max = value.split("-")
        return Assigment(min=int(min), max=int(max))


@dataclass
class ElfPair:
    assigment1: Assigment
    assigment2: Assigment

    def is_fully_overlapping(self) -> bool:
        return (
            self.assigment2.min <= self.assigment1.min and self.assigment1.max <= self.assigment2.max
            or
            self.assigment1.min <= self.assigment2.min and self.assigment2.max <= self.assigment1.max
        )

    def is_overlapping(self) -> bool:
        return not (
            self.assigment1.max < self.assigment2.min
            or
            self.assigment2.max < self.assigment1.min
        )

    @staticmethod
    def from_string(value: str) -> 'ElfPair':
        assigment1, assigment2 = value.split(",")
        return ElfPair(Assigment.from_string(assigment1), Assigment.from_string(assigment2))
