from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():

    # hashes diferentes para dois ingredientes iguais
    ingredient_1 = Ingredient("farinha")
    ingredient_2 = Ingredient("farinha")

    hash_value_1 = hash(ingredient_1)
    hash_value_2 = hash(ingredient_2)
    assert hash_value_1 == hash_value_2

    # hashes iguais para dois ingredientes diferentes
    ingredient_3 = Ingredient("queijo mussarela")
    hash_value_3 = hash(ingredient_3)
    assert hash_value_1 != hash_value_3

    # comparação de igualdade de dois ingredientes iguais
    compare_equal_ingredients = ingredient_1 == ingredient_2
    assert compare_equal_ingredients

    # comparação de igualdade de dois ingredientes diferentes
    compare_diff_ingredients = ingredient_1 == ingredient_3
    assert not compare_diff_ingredients

    # implementação do método __repr__
    expected_repr_ingredient_1 = "Ingredient('farinha')"
    assert repr(ingredient_1) == expected_repr_ingredient_1

    # caso atributo name diferente do que foi passado ao construtor
    assert ingredient_1.name == "farinha"

    # caso atributo restrictions não contenha os valores corretos
    assert Restriction.GLUTEN in ingredient_1.restrictions
