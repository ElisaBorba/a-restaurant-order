import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# noqa: F401, E261, E501


def test_dish():
    #  caso atributo name seja diferente
    dish_1 = Dish("Feijoada", 25.00)
    assert dish_1.name == "Feijoada"

    # caso hashes de dois pratos iguais sejam diferentes
    dish_2 = Dish("Feijoada", 25.00)

    hash_value_1 = hash(dish_1)
    hash_value_2 = hash(dish_2)
    assert hash_value_1 == hash_value_2

    # caso hashes de dois pratos diferentes sejam iguais;
    dish_3 = Dish("Macarronada", 20.00)
    hash_value_3 = hash(dish_3)
    assert hash_value_1 != hash_value_3

    # caso a comparação de igualdade de dois pratos iguais seja falsa
    compare_equal_dishes = dish_1 == dish_2
    assert compare_equal_dishes

    # caso a comparação de igualdade de dois pratos diferentes seja verdadeira
    compare_diff_dishes = dish_1 == dish_3
    assert not compare_diff_dishes

    # implementação do método __repr__
    expected_repr_ingredient_1 = "Dish('Feijoada', R$25.00)"
    assert repr(dish_1) == expected_repr_ingredient_1

    # caso um TypeError não seja levantado ao
    # criar um prato com um valor de tipo inválido

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Feijoada", "20.00")

    # caso um ValueError não seja levantado ao
    # criar um prato com um valor inválido
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Feijoada", -1)

    # testa o método add_ingredient_dependency()
    ingredient_1 = Ingredient("caldo de carne")
    dish_1.add_ingredient_dependency(ingredient_1, 5)

    expected_recipe = {Ingredient("caldo de carne"): 5}
    assert dish_1.recipe == expected_recipe

    # testa o método get_restrictions()
    get_restrictions = dish_1.get_restrictions()

    expected_restrictions = {Restriction.ANIMAL_DERIVED}
    assert get_restrictions == expected_restrictions

    # testa o método get_ingredients()
    get_ingredients = dish_1.get_ingredients()

    expected_ingredients = {Ingredient("caldo de carne")}
    assert get_ingredients == expected_ingredients
