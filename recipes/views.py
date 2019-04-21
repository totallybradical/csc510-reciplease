from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import redirect
from .models import Recipe, RecipeCategory, RecipeIngredient, RecipeUserFavorite
from .forms import RecipeForm
from django.http import JsonResponse

def recipe_list(request):
    recipes = Recipe.objects.all()
    my_faves = RecipeUserFavorite.objects.filter(user=request.user).values_list('recipe', flat=True)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'my_faves': my_faves})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_detail(request, id=None):
    recipe= get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_favorite(request, id=None):
    recipe= get_object_or_404(Recipe, id=id)
    RecipeUserFavorite.objects.create(recipe=recipe, user=request.user)
    return JsonResponse({'success': True})

def delete_favorite(request, id=None):
    recipe= get_object_or_404(Recipe, id=id)
    RecipeUserFavorite.objects.get(recipe=recipe, user=request.user).delete()
    return JsonResponse({'success': True})

