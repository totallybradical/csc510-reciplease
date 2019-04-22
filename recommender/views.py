from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import SearchForm
from recipes.models import Recipe
from ingredients.models import UserIngredient
from .utils.recommender import recommend_recipe

def recommend(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_model = form.save(commit=False)
            recipes = Recipe.objects.filter(category=search_model.mealCategory)
            ingredients = UserIngredient.objects.filter(user=request.user)
            feeling_luck = 'lucky' in request.POST
            recommended_recipes = recommend_recipe(ingredients, recipes, feeling_lucky=feeling_luck)
            return render(request, 'recipes/recipe_list.html', {'recipes': recommended_recipes})
    else:
        form = SearchForm()
    return render(request, 'recommender/search.html', {'form': form})

def load_user_ingredients(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').values('ingredient__name',).order_by('ingredient',)
    return render(request, 'recommender/load_user_ingredients.html', {'user_ingredients': user_ingredients})