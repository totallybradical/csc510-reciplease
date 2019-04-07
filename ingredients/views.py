from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import Ingredient, UserIngredient
from .forms import IngredientForm, UserIngredientForm

def ingredient_list(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient') # Get all ingredients for this user
    return render(request, 'ingredients/user_ingredient_list.html', {'user_ingredients': user_ingredients})

def add_user_ingredient(request):
    if request.method == "POST":
        form = UserIngredientForm(request.POST)
        if form.is_valid():
            user_ingredient = form.save(commit=False)
            user_ingredient.user = request.user
            user_ingredient.save()
            return redirect('user_ingredient_list')
    else:
        form = UserIngredientForm()
    return render(request, 'ingredients/user_ingredient_form.html', {'form': form})

def add_ingredient_type(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('add_user_ingredient')
    else:
        form = IngredientForm()
    return render(request, 'ingredients/ingredient_form.html', {'form': form})