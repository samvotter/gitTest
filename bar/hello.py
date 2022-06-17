from dataclasses import dataclass
from foo.world import World


@dataclass
class Hello(World):
    value: str = "Hello"
