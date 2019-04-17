import recommender
import unittest


class Recipe:
    name = ""
    ingredients = []

    def __init__(self, name, ingr):
        self.name = name
        self.ingredients = ingr


class Ingredient:
    id = None
    name = ""

    def __init__(self, name, id):
        self.id = id
        self.name = name


class UserIngredient:
    ingredient=None
    quantity = None

    def __init__(self, ing, quant):
        self.ingredient = ing
        self.quantity = quant


class RecipeIngredient:
    ingredient=None
    quantity = None

    def __init__(self, ing, quant):
        self.ingredient = ing
        self.quantity = quant


class TestRecommender(unittest.TestCase):
    def test_recommender(self):
        kale = Ingredient('kale', 1)
        salt = Ingredient('salt', 2)
        pepper = Ingredient('pepper', 3)
        cheese = Ingredient('cheese', 4)

        corn = Ingredient('corn', 5)

        user_ingredient_list = list()
        user_ingredient_list.append(UserIngredient(kale, 3))
        user_ingredient_list.append(UserIngredient(salt, 4))
        user_ingredient_list.append(UserIngredient(pepper, 1))
        user_ingredient_list.append(UserIngredient(cheese, 10))

        recipes = list()
        recipes.append(Recipe('pass_recipe', list([RecipeIngredient(kale, 1), RecipeIngredient(salt, 4)])))
        recipes.append(Recipe('fail', list([RecipeIngredient(corn, 1), RecipeIngredient(salt, 4)])))
        recipes.append(Recipe('fail2', list([RecipeIngredient(pepper, 15), RecipeIngredient(salt, 4)])))

        recommended_recipes = recommender.recommend_recipe(user_ingredient_list, recipes)
        self.assertEqual(len(recommended_recipes), 1)
        self.assertEqual(recommended_recipes[0].name, 'pass_recipe')
        recipes.append(Recipe('pass2', list([RecipeIngredient(pepper, 1), RecipeIngredient(salt, 4)])))
        print(recommender.recommend_recipe(user_ingredient_list, recipes, feeling_lucky=True).name)


if __name__ == '__main__':
    unittest.main()
