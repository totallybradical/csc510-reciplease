from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect


def recommender(request):
    return render(request, 'recommender/search.html')