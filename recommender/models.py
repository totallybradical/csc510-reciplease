from django.db import models

# Create your models here.


# Model for a Search for recipes
class SearchModel(models.Model):
    MEAL_TYPE= (
        ('BRFST','Breakfast'),
        ('LNCH','Lunch'),
        ('DNR','Dinner'),
    )

    MEAL_STYLE= (
        ('IT','Italian'),
        ('AM','American'),
        ('AS','Asian'),
        ('FR','French'),
    )

    #ingredients = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)
    mealType =  models.CharField(max_length=5, choices=MEAL_TYPE)
    mealStyle = models.CharField(max_length=2, choices=MEAL_STYLE)
    askANeighbor = models.BooleanField()
    