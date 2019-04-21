from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<int:id>/', views.recipe_detail, name='detail'),
    path('<int:id>/favorite', views.add_favorite, name='add_favorite'),
    path('<int:id>/unfavorite', views.delete_favorite, name='delete_favorite'),
]