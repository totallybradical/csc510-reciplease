from django import forms

from .models import Ingredient, UserIngredient

class UserIngredientForm(forms.ModelForm):

    class Meta:
        model = UserIngredient
        fields = ('ingredient', 'quantity', 'exp_date')

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'quantity_units',)

class EditUserIngredientForm(forms.ModelForm):

    class Meta:
        model = UserIngredient
        fields = ('quantity', 'exp_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ingredient_id = self.instance.ingredient.id
        ingredient = Ingredient.objects.get(id=ingredient_id)
        self.fields['quantity'].label = 'Quantity (' + ingredient.quantity_units + ')'