from typing import Dict, List

# from models.ingredient import Ingredient, Restriction

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    # def __init__(self, data_path=DATA_PATH):
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):

        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes_list = list()

        for dish in self.menu_data.dishes:
            if not restriction or restriction not in dish.get_restrictions():

                dishes_dict = {
                    "dish_name": dish.name,
                    "ingredients": dish.get_ingredients(),
                    "price": float(dish.price),
                    "restrictions": dish.get_restrictions(),
                }

                dishes_list.append(dishes_dict)

        return dishes_list


# if __name__ == "__main__":
#     instancia = MenuBuilder()
#     menu_data = instancia.menu_data
#     # print("DISHES::::", menu_data.dishes)

#     ingrediente = Ingredient("camarão")
#     print(instancia.get_main_menu(Restriction.ANIMAL_MEAT))
#     # print("deve retornar todos::::", instancia.get_main_menu())
