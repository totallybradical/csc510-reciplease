from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import SearchForm
from recipes.models import Recipe
from .utils.recommender import recommend_recipe

def recommend(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if 'recommend' in request.POST:
                search_model = form.save(commit=False)
                print(search_model)
                recipes = Recipe.objects.filter(category=search_model.mealCategory)
            elif 'lucky' in request.POST:
                #recipes = recommend_recipe([], Recipe.objects., feeling_lucky=True)
                # TODO: how can we make this utility function work :(
                recipes = Recipe.objects.all()
                return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
    else:
        form = SearchForm()
    return render(request, 'recommender/search.html', {'form': form})
