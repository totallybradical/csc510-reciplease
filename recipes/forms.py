from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ()

# IngredientFormset = forms.inlineformset_factory(Recipe, RecipeIngredient, form=IngredientForm, extra=1)