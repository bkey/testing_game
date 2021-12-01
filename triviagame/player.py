from dataclasses import dataclass


@dataclass
class Player:
    name: str
    pop_culture_skill_level: int
    science_skill_level: int
    witchcraft_skill_level: int
    fashion_skill_level: int

    def __init__(
            self,
            name,
            pop_culture_skill_level=5,
            science_skill_level=5,
            witchcraft_skill_level=5,
            fashion_skill_level=5
    ):
        self.name = name
        self.pop_culture_skill_level = pop_culture_skill_level
        self.science_skill_level = science_skill_level
        self.witchcraft_skill_level = witchcraft_skill_level
        self.fashion_skill_level = fashion_skill_level

    def __repr__(self) -> str:
        return self.name
