from django.contrib import admin

# Register your models here.
from .models import Ingredient
from .models import UserIngredient

admin.site.register(Ingredient)
admin.site.register(UserIngredient)