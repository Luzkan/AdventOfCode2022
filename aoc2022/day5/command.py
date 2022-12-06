from dataclasses import dataclass


@dataclass
class Command:
    amount: int
    from_stack_idx: int
    to_stack_idx: int

    @staticmethod
    def from_string(command_string: str) -> "Command":
        _, amount, _, from_idx, _, to_idx = command_string.split(" ")
        return Command(amount=int(amount), from_stack_idx=int(from_idx)-1, to_stack_idx=int(to_idx)-1)
