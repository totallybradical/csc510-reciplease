from django.db import models
from recipes.models import RecipeCategory


# Model for a Search for recipes
class SearchModel(models.Model):
    MEAL_CATEGORY= (
        ('BRFST','Breakfast'),
        ('LNCH','Lunch'),
        ('DNR','Dinner'),
    )

    #ingredients = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)
    #mealCategory =  models.CharField(max_length=5, choices=MEAL_CATEGORY)
    mealCategory = models.ForeignKey('recipes.RecipeCategory', on_delete=models.SET_NULL, null=True)
    askANeighbor = models.BooleanField()
