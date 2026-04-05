from fractions import Fraction
from enum import Enum

class Rate(Fraction):
    pass

class Recipe:
    def __init__(
            self,
            pretty_name: str,
            inputs: list[tuple["Item", Rate]],
            outputs: list[tuple["Item", Rate]],
            hand_craftable: bool=False,
            workshop_craftable: bool=False,
            machine_craftable: bool=False,
            ) -> None:
        self.pretty_name: str = pretty_name
        self.inputs: list[tuple[Item, Rate]] = inputs
        self.outputs: list[tuple[Item, Rate]] = outputs
        self.hand_craftable: bool = hand_craftable
        self.workshop_craftable: bool = workshop_craftable
        self.machine_craftable: bool = machine_craftable

class Item:
    def __init__(self, pretty_name: str) -> None:
        self.pretty_name: str = pretty_name
        self.recipes: list[Recipe]
        self.used_in: list[Recipe]

    def _attach_recipes(self, recipes: list[Recipe], used_in: list[Recipe]) -> None:
        self.recipes = recipes
        self.used_in = used_in
