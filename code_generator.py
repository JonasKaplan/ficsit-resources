import json

t: str = "    "

with open("data.json", "r") as f:
    data: dict[str, dict] = json.load(f)

with open("ficsit_resources/items.py", "w") as f:
    f.write("from ficsit_resources.types import Item\n\nclass Items:\n")
    for item_id, item in data["items"].items():
        f.write(f"{t}{item_id} = Item(\"{item['in-game-name']}\")\n")
    f.write(f"\n{t}__all = [\n")
    for item_id in data["items"]:
        f.write(f"{t * 2}{item_id},\n")
    f.write(f"{t}]\n\n")
    f.write(f"{t}@staticmethod\n{t}def all() -> list[Item]:\n{t * 2}return Items.__all\n")

with open("ficsit_resources/recipes.py", "w") as f:
    f.write("from ficsit_resources.types import Recipe, Rate\n")
    f.write("from ficsit_resources.items import Items\n\nclass Recipes:\n")
    for recipe_id, recipe in data["recipes"].items():
        inputs: str = ", ".join([f"(Items.{input['item']}, Rate({input['rate']}))" for input in recipe["inputs"]])
        outputs: str = ", ".join([f"(Items.{output['item']}, Rate({output['rate']}))" for output in recipe["outputs"]])
        f.write(f"{t}{recipe_id} = Recipe(\n")
        f.write(f"{t * 2}\"{recipe['in-game-name']}\",\n")
        f.write(f"{t * 2}[{inputs}],\n")
        f.write(f"{t * 2}[{outputs}],\n")
        if recipe["hand-craftable"]:
            f.write(f"{t * 2}hand_craftable=True,\n")
        if recipe["workshop-craftable"]:
            f.write(f"{t * 2}workshop_craftable=True,\n")
        if recipe["machine-craftable"]:
            f.write(f"{t * 2}machine_craftable=True,\n")
        f.write(f"{t})\n")
    f.write(f"\n{t}__all = [\n")
    for recipe_id in data["recipes"]:
        f.write(f"{t * 2}{recipe_id},\n")
    f.write(f"{t}]\n\n")
    f.write(f"{t}@staticmethod\n{t}def all() -> list[Recipe]:\n{t * 2}return Recipes.__all\n")

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
