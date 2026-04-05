from ficsit_resources.types import Item, Recipe, Rate
from ficsit_resources.items import Items
from ficsit_resources.recipes import Recipes

Items.IronPlate._attach_recipes(
    [Recipes.IronPlate, Recipes.SteelCastPlate],
    [Recipes.ReinforcedIronPlate],
)
