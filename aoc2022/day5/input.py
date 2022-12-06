from dataclasses import dataclass
from pathlib import Path

from aoc2022.day5.command import Command
from aoc2022.day5.stack import Stack


@dataclass
class Input:
    path: Path

    def get_stacks(self, number_of_stacks: int) -> list[Stack]:
        return [
            Stack.from_string(
                starting_position_definition=self.file_contents[:self._first_empty_line_index-1],
                column_idx=column_idx
            )
            for column_idx in range(1, number_of_stacks+1)
        ]

    def get_commands(self) -> list[Command]:
        return [
            Command.from_string(command_string)
            for command_string in self.file_contents[self._first_empty_line_index+1:]
        ]

    @property
    def _first_empty_line_index(self) -> int:
        return self.file_contents.index("\n")

    @property
    def file_contents(self) -> list[str]:
        with open(self.path, "r", encoding='utf-8') as file:
            return [line for line in file.readlines()]
