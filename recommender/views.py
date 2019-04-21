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
            if 'recommend' in request.POST:
                recipes = Recipe.objects.filter(category=search_model.mealCategory)
            elif 'lucky' in request.POST:
                recipes = list(Recipe.objects.all())
                ingredients = list(UserIngredient.objects.all())
                recommended_recipes = recommend_recipe(ingredients, recipes, feeling_lucky=True)
            return render(request, 'recipes/recipe_list.html', {'recipes': recommended_recipes})
    else:
        form = SearchForm()
    return render(request, 'recommender/search.html', {'form': form})
