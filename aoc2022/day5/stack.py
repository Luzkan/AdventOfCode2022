from dataclasses import dataclass


@dataclass
class Stack:
    values: list[str]

    def add_block(self, block: str):
        self.values.append(block)

    def remove_block(self, amount: int) -> list[str]:
        removed = [self.values.pop() for _ in range(0, amount)]
        removed.reverse()
        return removed

    @staticmethod
    def from_string(starting_position_definition: list[str], column_idx: int) -> "Stack":
        START_IDX, SPACING = 1, 4
        target_idx: int = START_IDX + ((column_idx-1) * SPACING)
        stack = [line[target_idx] for line in starting_position_definition if line[target_idx] != " "]
        stack.reverse()
        return Stack(stack)
