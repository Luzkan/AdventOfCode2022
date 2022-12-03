from dataclasses import dataclass


@dataclass
class Rucksack:
    items: str

    @property
    def shared_item(self) -> str:
        return list(set(self.first_compartment) & set(self.second_compartment))[0]

    @property
    def first_compartment(self) -> str:
        return self.items[:len(self.items) // 2]

    @property
    def second_compartment(self) -> str:
        return self.items[len(self.items) // 2:]
