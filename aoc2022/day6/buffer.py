from dataclasses import dataclass


@dataclass
class Buffer:
    value: str

    def get_start_of_packet_marker(self, length: int) -> int:
        for idx in range(0, len(self.value)):
            if len(self._get_unique_characters(self._get_subbuffer(idx, length))) == length:
                return idx+length
        raise ValueError

    def _get_unique_characters(self, characters: str) -> set:
        return set(list(characters))

    def _get_subbuffer(self, start_idx: int, length: int) -> str:
        return self.value[start_idx:(start_idx+length)]
