from aoc2022.day3.elf_group import ElfGroup
from aoc2022.day3.prioritizer import Prioritizer
from aoc2022.day3.rucksack import Rucksack


class TestDay3:
    def run_all(self) -> None:
        for attr in dir(self):
            _ = getattr(self, attr)() if attr.startswith("test_") else None

    @staticmethod
    def test_finds_shared_item():
        for value, expected in [
            ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p'),
            ('PmmdzqPrVvPwwTWBwg', 'P'),
            ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v')
        ]:
            assert Rucksack(items=value).shared_item == expected

    @staticmethod
    def test_prioritizes_correctly():
        for value, expected in [('a', 1), ('z', 26), ('A', 27), ('Z', 52), ('p', 16), ('L', 38)]:
            assert Prioritizer.prioritize(value) == expected

    @staticmethod
    def test_finds_group_badge():
        for value, expected in [
            (ElfGroup(elfs_rucksacks=[
                Rucksack(items='vJrwpWtwJgWrhcsFMMfFFhFp'),
                Rucksack(items='jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),
                Rucksack(items='PmmdzqPrVvPwwTWBwg')
            ]), 'r'),
            (ElfGroup(elfs_rucksacks=[
                Rucksack(items='wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'),
                Rucksack(items='ttgJtRGJQctTZtZT'),
                Rucksack(items='CrZsJsPPZsGzwwsLwLmpwMDw')
            ]), 'Z'),
        ]:
            assert value.shared_item == expected
