import random


def recommend_recipe(user_ingredient_list, recipe_list, ask_a_neighbor=False, feeling_lucky=False):
    recommended_recipes = []
    for recipe in recipe_list:
        if ingredients_available(recipe, user_ingredient_list, ask_a_neighbor):
            recommended_recipes.append(recipe)
    if feeling_lucky:
        return random.choice(recommended_recipes)
    return recommended_recipes


def ingredients_available(recipe, ingredient_list, ask_a_neighbor):
    early_exit_threshold = 1 if ask_a_neighbor else 0
    unavailable_ingredient = 0
    for ingredient in recipe.ingredients:
        if compare_ingredients(ingredient, ingredient_list):
            unavailable_ingredient += 1
        if unavailable_ingredient > early_exit_threshold:
            return False
    return True


def compare_ingredients(recipe_ingredient, ingredient_list):
    for user_ingredient in ingredient_list:
        if recipe_ingredient.ingredient.id == user_ingredient.ingredient.id:
            if recipe_ingredient.quantity <= user_ingredient.quantity:
                return False
    return True
