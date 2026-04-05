import json

t: str = "    "

with open("ficsit_resources/data.json", "r") as f:
    data: dict[str, dict] = json.load(f)

with open("ficsit_resources/items.py", "w") as f:
    f.write("from ficsit_resources.types import Item\n\nclass Items:\n")
    for item_id, item in data["items"].items():
        f.write(f"{t}{item_id} = Item(\"{item['in-game-name']}\")\n")

with open("ficsit_resources/recipes.py", "w") as f:
    f.write("from ficsit_resources.types import Recipe, Rate\n")
    f.write("from ficsit_resources.items import Items\n\nclass Recipes:\n")
    for recipe_id, recipe in data["recipes"].items():
        inputs: str = ", ".join([f"(Items.{input['item']}, Rate({input['rate']}))" for input in recipe["inputs"]])
        outputs: str = ", ".join([f"(Items.{output['item']}, Rate({output['rate']}))" for output in recipe["outputs"]])
        f.write(f"{t}{recipe_id} = Recipe(\n")
        f.write(f"{t * 2}\"{recipe['in-game-name']}\",\n")
        f.write(f"{t * 2}[{inputs}],\n")
        f.write(f"{t * 2}[{outputs}],\n{t})\n")

with open("ficsit_resources/__init__.py", "w") as f:
    f.write("from ficsit_resources.types import Item, Recipe, Rate\n")
    f.write("from ficsit_resources.items import Items\n")
    f.write("from ficsit_resources.recipes import Recipes\n\n")
    for item_id in data["items"]:
        used_in: list[str] = []
        recipes: list[str] = []
        for recipe_id, recipe in data["recipes"].items():
            if item_id in [input["item"] for input in recipe["inputs"]]:
                used_in.append(recipe_id)
            if item_id in [output["item"] for output in recipe["outputs"]]:
                recipes.append(recipe_id)
        used_in_py: str = ", ".join([f"Recipes.{recipe}" for recipe in used_in])
        recipes_py: str = ", ".join([f"Recipes.{recipe}" for recipe in recipes])
        if (len(used_in_py) != 0) or (len(recipes_py) != 0):
            f.write(f"Items.{item_id}._attach_recipes(\n")
            f.write(f"{t}[{recipes_py}],\n")
            f.write(f"{t}[{used_in_py}],\n)\n")
