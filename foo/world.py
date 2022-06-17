from dataclasses import dataclass


@dataclass
class World:
    value: str = "world"

    def __str__(self):
        return self.value
