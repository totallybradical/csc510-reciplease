import random
import sys


def recommend_recipe(selected_ingredients, recipe_list, ask_a_neighbor=False, feeling_lucky=False):
    recommended_recipes = []
    for recipe in recipe_list:
        if ingredients_available(recipe, selected_ingredients, ask_a_neighbor):
            recommended_recipes.append(recipe)
    if feeling_lucky and len(recommended_recipes) > 0:
        return [random.choice(recommended_recipes)]
    return recommended_recipes


def ingredients_available(recipe, selected_ingredients, ask_a_neighbor):
    early_exit_threshold = 1 if ask_a_neighbor else 0
    unavailable_ingredient = 0

    ingredients = recipe.ingredients.all()
    for ingredient in ingredients:
        recipe_ingredient = ingredient.recipeingredient_set.all()[0]
        if not compare_ingredients(recipe_ingredient, selected_ingredients):
            unavailable_ingredient += 1
        if unavailable_ingredient > early_exit_threshold:
            return False
    return True


def compare_ingredients(recipe_ingredient, selected_ingredients):
    for selected_ingredient in selected_ingredients:
        # print("Comparing " + selected_ingredient + " and " + recipe_ingredient.ingredient.name, file=sys.stderr)
        if recipe_ingredient.ingredient.name == selected_ingredient.ingredient.name:
            return True
    return False
