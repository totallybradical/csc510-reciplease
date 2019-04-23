from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import SearchForm
from recipes.models import Recipe, RecipeUserFavorite
from ingredients.models import UserIngredient
from .utils.recommender import recommend_recipe
from django.http import JsonResponse

def recommend(request):
    if request.method == 'POST':
        form = SearchForm(request.user, request.POST)
        if form.is_valid():
            search_model = form.save(commit=False)
            recipes = Recipe.objects.filter(category=search_model.mealCategory)
            selected_ingredients = form.cleaned_data['ingredients']
            ask_a_neighbor = form.cleaned_data['askANeighbor']
            feeling_luck = 'lucky' in request.POST
            recommended_recipes = recommend_recipe(selected_ingredients, recipes, ask_a_neighbor=ask_a_neighbor, feeling_lucky=feeling_luck)
            my_faves = RecipeUserFavorite.objects.filter(user=request.user).values_list('recipe', flat=True)
            return render(request, 'recipes/recipe_list.html', {'recipes': recommended_recipes, 'my_faves': my_faves})
        else:
            return JsonResponse({'formset_errors': form.errors})

    else:
        form = SearchForm(request.user)
    return render(request, 'recommender/search.html', {'form': form})

def load_user_ingredients(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').values('ingredient__name','ingredient__id').order_by('ingredient').distinct()
    return render(request, 'recommender/load_user_ingredients.html', {'user_ingredients': user_ingredients})