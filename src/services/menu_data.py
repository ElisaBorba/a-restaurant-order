import csv
from typing import Tuple
from models.ingredient import Ingredient
from models.dish import Dish
import os

dishes = Tuple[float, Ingredient, int]


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = {}

    def __repr__(self) -> str:
        return f"Menu('{self.dishes}')"

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def read_menu_data(self):
        with open(self.source_path, "r", encoding="utf-8", newline="") as file:
            menu_reader = csv.reader(file, delimiter=",")
            next(menu_reader)
            for row in menu_reader:
                dish_name, price, ingredient_name, recipe_amount = row

                ingredient = Ingredient(ingredient_name)
                dish = Dish(dish_name, float(price))

                if dish.name not in self.dishes:
                    self.dishes[dish] = set()

                for existing_dish in self.dishes:
                    if existing_dish.name == dish_name:
                        self.dishes[existing_dish].add(
                            (ingredient, int(recipe_amount))
                        )
                        break
                else:
                    self.dishes[dish].add((ingredient, int(recipe_amount)))
        return self.dishes

    def get_menu(self):
        return set(self.dishes.keys())


# source_path
path = os.path.join("data", "menu_base_data.csv")
menu_obj = MenuData(path)
test = menu_obj.read_menu_data()
# print("MENU DATA", test)

dishesss = menu_obj.dishes
print("GET DISHES", dishesss)
