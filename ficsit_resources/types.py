from fractions import Fraction

class Rate(Fraction):
    pass

class Recipe:
    def __init__(self, pretty_name: str, inputs: list[tuple["Item", Rate]], outputs: list[tuple["Item", Rate]]) -> None:
        self.pretty_name: str = pretty_name
        self.inputs: list[tuple[Item, Rate]] = inputs
        self.outputs: list[tuple[Item, Rate]] = outputs

class Item:
    def __init__(self, pretty_name: str) -> None:
        self.pretty_name: str = pretty_name
        self.recipes: list[Recipe]
        self.used_in: list[Recipe]

    def _attach_recipes(self, recipes: list[Recipe], used_in: list[Recipe]) -> None:
        self.recipes = recipes
        self.used_in = used_in
