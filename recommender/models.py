from django.db import models
from recipes.models import RecipeCategory
from ingredients.models import UserIngredient
from django.conf import settings


# Model for a Search for recipes
class SearchModel(models.Model):

    current_user = settings.AUTH_USER_MODEL
    print(current_user)
    #ingredients = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)
    #mealCategory =  models.CharField(max_length=5, choices=MEAL_CATEGORY)
    mealCategory = models.ForeignKey('recipes.RecipeCategory', on_delete=models.SET_NULL, null=True)
    askANeighbor = models.BooleanField()
    #ingredients = models.ForeignKey(UserIngredient, on_delete=models.SET_NULL, null=True, limit_choices_to={'user': views.ingredient_list})
    ingredients = models.ForeignKey(UserIngredient, on_delete=models.SET_NULL, null=True, )