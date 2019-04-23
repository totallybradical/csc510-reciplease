from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator

def one_month_from_today():
    return timezone.now() + timedelta(days=30)

# Model for an ingredient (not an instance of ingredient)
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity_units = models.CharField(max_length=200) # Type of units for ingredient (oz, lbs, units, etc)

    class Meta:
        ordering = ['name']

    def add(self):
        self.save()

    def __str__(self):
        return self.name

# Model for a specific instance (a person's amount of said ingredient)
class UserIngredient(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    exp_date = models.DateField(default=one_month_from_today, blank=True, null=True)
    
    def __str__(self):
        return self.ingredient.name
