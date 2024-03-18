# from src.models.dish import Dish
# from src.models.ingredient import Ingredient

from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            dishes_dict = dict()
            for row in reader:
                dish = Dish(row["dish"], float(row["price"]))
                if dish.name not in dishes_dict:
                    dish.add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )
                    dishes_dict[dish.name] = dish
                else:
                    dishes_dict[dish.name].add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )

        self.dishes = set(dishes_dict.values())
