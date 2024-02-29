import csv
import os
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = {}
        self.menu_data = self.read_menu_data()

    # def __repr__(self) -> str:
    #     return f"Menu('{self.dishes}')"

    # def __eq__(self, other) -> bool:
    #     return self.__repr__() == other.__repr__()

    # def __hash__(self) -> int:
    #     return hash(self.__repr__())

    def read_menu_data(self):
        with open(self.source_path, "r") as file:
            menu_reader = csv.DictReader(file)

            for row in menu_reader:
                dish = Dish(row["dish"], float(row["price"]))
                print(dish.name)
                if dish.name not in self.dishes:
                    dish.add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )
                    # print(dish.get_ingredients())
                    self.dishes[dish.name] = dish
                else:
                    # print(self.dishes)
                    self.dishes[dish.name].add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )
                    # print(self.dishes[dish.name].get_ingredients())
        return set(self.dishes)

        #     self.dishes[dish_instance.name] = {
        #         "price": price,
        #         "ingredients": {},
        #     }

        # self.dishes[dish_instance.name]["ingredients"][
        #     ingredient_instance.name
        # ] = recipe_amount


# source_path
path = os.path.join("data", "menu_base_data.csv")
menu_obj = MenuData(path)
test = menu_obj.read_menu_data()
print("MENUUUU", test)

dishesss = menu_obj.dishes
print("GET_DISHES", dishesss)
