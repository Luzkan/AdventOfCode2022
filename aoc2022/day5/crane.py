

from dataclasses import dataclass

from aoc2022.day5.command import Command
from aoc2022.day5.stack import Stack


@dataclass
class Crane:
    stacks: list[Stack]
    commands: list[Command]

    def execute_commands_9000(self):
        for command in self.commands:
            for move in range(0, command.amount):
                self.stacks[command.to_stack_idx].add_block(self.stacks[command.from_stack_idx].remove_block(1)[0])
        return self.stacks

    def execute_commands_9001(self):
        for command in self.commands:
            for block in self.stacks[command.from_stack_idx].remove_block(command.amount):
                self.stacks[command.to_stack_idx].add_block(block)
        return self.stacks

    def get_top_block_of_each_stack(self) -> str:
        return ''.join([stack.values[-1] for stack in self.stacks])
