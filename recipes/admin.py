from django.contrib import admin

# Register your models here.
from .models import Recipe
from .models import RecipeCategory
from .models import RecipeIngredient

admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(RecipeIngredient)