from aoc2022.day4.elf_pair import Assigment, ElfPair
from pytest import fixture

Overlapping = bool
FullyOverlapping = bool


class TestDay4:
    @fixture
    def sample(self) -> list[tuple[ElfPair, FullyOverlapping, Overlapping]]:
        return [
            (ElfPair(Assigment(min=2, max=4), Assigment(min=6, max=8)), False, False),
            (ElfPair(Assigment(min=2, max=3), Assigment(min=4, max=5)), False, False),
            (ElfPair(Assigment(min=5, max=7), Assigment(min=7, max=9)), False, True),
            (ElfPair(Assigment(min=2, max=8), Assigment(min=3, max=7)), True, True),
            (ElfPair(Assigment(min=6, max=6), Assigment(min=4, max=6)), True, True),
            (ElfPair(Assigment(min=2, max=6), Assigment(min=4, max=8)), False, True),
        ]

    @staticmethod
    def test_finds_fully_overlapping(sample: list[tuple[ElfPair, FullyOverlapping, Overlapping]]):
        value: ElfPair
        for value, is_fully_overlapping, _ in sample:
            assert value.is_fully_overlapping() == is_fully_overlapping

    @staticmethod
    def test_finds_overlapping(sample: list[tuple[ElfPair, FullyOverlapping, Overlapping]]):
        value: ElfPair
        for value, _, is_overlapping in sample:
            assert value.is_overlapping() == is_overlapping
