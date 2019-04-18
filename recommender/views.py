from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import SearchForm
from recipes.models import Recipe

def recommend(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_model = form.save(commit=False)
            print(search_model)
            recipes = Recipe.objects.filter(category=search_model.mealCategory)
            return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
    else:
        form = SearchForm()
    return render(request, 'recommender/search.html', {'form': form})
