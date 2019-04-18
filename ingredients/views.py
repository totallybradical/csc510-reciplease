from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import redirect
from django.db.models import Sum
from .models import Ingredient, UserIngredient
from .forms import IngredientForm, UserIngredientForm

def ingredient_list(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').values('ingredient', 'ingredient__name', 'exp_date', 'ingredient__quantity_units').annotate(sumqty=Sum('quantity')).order_by('ingredient', '-exp_date')
    return render(request, 'ingredients/user_ingredient_list.html', {'user_ingredients': user_ingredients})

def delete_user_ingredient(request, id=None):
    user_ingredient = get_object_or_404(UserIngredient, id=id)
    creator = user_ingredient.user
    if request.method == "POST" and request.user.is_authenticated and request.user == creator:
        user_ingredient.delete()
        messages.success(request, "Ingredient successfully deleted!")
        return HttpResponseRedirect("ingredients/list")
    
    context= {'user_ingredient': user_ingredient,
              'creator': creator,
              }
    
    return render(request, 'ingredients/delete_user_ingredient.html', context)    

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
