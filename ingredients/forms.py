from django import forms

from .models import Ingredient, UserIngredient

class UserIngredientForm(forms.ModelForm):

    class Meta:
        model = UserIngredient
        fields = ('ingredient', 'quantity',)

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'quantity_units',)