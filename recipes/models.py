from django.db import models

# Create your models here.
from django.conf import settings
from django.core.validators import MinValueValidator
from ingredients.models import Ingredient

# Basic model for a recipe category
class RecipeCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

# Model for a recipe to ingredient mapping
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return (self.recipe.name + ': ' + self.ingredient.name)

# Model for a recipe to user (favorite) mapping
class RecipeUserFavorite(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return (self.recipe.name + ': ' + self.user.username)

# Model for an recipe 
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('RecipeCategory', on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    users_fave = models.ManyToManyField(settings.AUTH_USER_MODEL, through=RecipeUserFavorite, blank=True)

    def __str__(self):
        return self.name
