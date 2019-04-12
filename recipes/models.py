from django.db import models

# Create your models here.
from django.conf import settings
from django.core.validators import MinValueValidator
from ingredients.models import Ingredient

# Basic model for a recipe category
class RecipeCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Model for a recipe to ingredient mapping
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return (self.recipe.name + ': ' + self.ingredient.name)

# Model for an recipe 
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('RecipeCategory', on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()

    def __str__(self):
        return self.name