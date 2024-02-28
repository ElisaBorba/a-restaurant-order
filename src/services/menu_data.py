import csv
import os
from models.ingredient import Ingredient
from models.dish import Dish


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
            menu_reader = csv.DictReader(file)

            for row in menu_reader:
                dish = row["dish"]
                price = row["price"]
                ingredient = row["ingredient"]
                recipe_amount = row["recipe_amount"]

                ingredient_instance = Ingredient(ingredient)
                dish_instance = Dish(dish, float(price))

                if dish_instance.name not in self.dishes:
                    self.dishes[dish_instance.name] = {
                        "price": price,
                        "ingredients": {},
                    }

                self.dishes[dish_instance.name]["ingredients"][
                    ingredient_instance.name
                ] = recipe_amount
        return set(self.dishes)

    # def get_menu(self):
    #     return set(self.dishes.keys())


# source_path
path = os.path.join("data", "menu_base_data.csv")
menu_obj = MenuData(path)
test = menu_obj.read_menu_data()
# test_get = menu_obj.get_menu()
print("MENUUUU", test)

dishesss = menu_obj.dishes
print("GET_DISHES", dishesss)
