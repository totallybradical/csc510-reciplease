from django.db import models

# Create your models here.
from django.conf import settings

# Model for an ingredient (not an instance of ingredient)
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity_units = models.CharField(max_length=200) # Type of units for ingredient (oz, lbs, units, etc)

    def add(self):
        self.save()

    def __str__(self):
        return self.name

# Model for a specific instance (a person's amount of said ingredient)
class UserIngredient(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.id} ({self.ingredient.name})'