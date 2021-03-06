from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from django.db.models import Sum
from .models import Ingredient, UserIngredient
from .forms import IngredientForm, UserIngredientForm, EditUserIngredientForm
from django.http import JsonResponse

def get_ingredient_units(request, id):
    ingredient = Ingredient.objects.get(pk=id)
    ingredient_dict = {}
    ingredient_dict[id] = ingredient.quantity_units
    return JsonResponse(ingredient_dict)

def ingredient_list(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').values('ingredient', 'ingredient__name', 'ingredient__quantity_units').annotate(sumqty=Sum('quantity')).order_by('ingredient')
    return render(request, 'ingredients/user_ingredient_list.html', {'user_ingredients': user_ingredients})

def delete_user_ingredient(request, id=None):
    user_ingredient = get_object_or_404(UserIngredient, id=id)
    creator = user_ingredient.user
    if request.method == "POST" and request.user.is_authenticated and request.user == creator:
        user_ingredient.delete()
        messages.success(request, "Ingredient successfully deleted!")
        return redirect('expiring_user_ingredient_list')
    
    context= {'user_ingredient': user_ingredient,
              'creator': creator,
              }
    
    return render(request, 'ingredients/delete_user_ingredient.html', context)    

def edit_user_ingredient(request, id=None):
    user_ingredient = get_object_or_404(UserIngredient, id=id)
    creator = user_ingredient.user
    if request.method == "POST" and request.user.is_authenticated and request.user == creator:
        form = EditUserIngredientForm(request.POST, instance=user_ingredient)
        if form.is_valid():
            user_ingredient = form.save(commit=False)
            user_ingredient.user = request.user
            user_ingredient.save()
            return redirect('expiring_user_ingredient_list')
    else:
        form = EditUserIngredientForm(instance=user_ingredient)
    return render(request, 'ingredients/edit_user_ingredient_form.html', {'form': form, 'user_ingredient': user_ingredient})

def expiring_ingredients(request):
    expiring_user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').order_by('exp_date') # Get all ingredients for this user
    return render(request, 'ingredients/expiring_user_ingredient_list.html', {'expiring_user_ingredients': expiring_user_ingredients})

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
