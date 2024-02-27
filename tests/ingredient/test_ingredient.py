from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501

# import pytest


def test_ingredient():

    # hashes diferentes para dois ingredientes iguais
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")

    hash_value1 = hash(ingredient1)
    hash_value2 = hash(ingredient2)

    assert hash_value1 == hash_value2

    # hashes iguais para dois ingredientes diferentes
    ingredient3 = Ingredient("queijo mussarela")
    hash_value3 = hash(ingredient3)

    assert hash_value1 != hash_value3

    # comparação de igualdade de dois ingredientes iguais
    compare_equal_ingredients = ingredient1 == ingredient2
    assert compare_equal_ingredients

    # comparação de igualdade de dois ingredientes diferentes
    compare_diff_ingredients = ingredient1 == ingredient3
    assert not compare_diff_ingredients

    # implementação do método __repr__

    expected_ingredient1_repr = "Ingredient('farinha')"
    assert repr(ingredient1) == expected_ingredient1_repr

    # caso atributo name diferente do que foi passado ao construtor
    assert ingredient1.name == "farinha"

    # caso atributo restrictions não contenha os valores corretos
    assert Restriction.GLUTEN in ingredient1.restrictions
