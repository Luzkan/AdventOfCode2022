class Prioritizer:
    @staticmethod
    def prioritize(value: str) -> int:
        # Lowercase item types a through z have priorities 1 through 26.
        # Uppercase item types A through Z have priorities 27 through 52.
        if value.islower():
            return ord(value) - 96
        if value.isupper():
            return ord(value) - 64 + 26
        raise ValueError(f"Invalid value: {value}")
