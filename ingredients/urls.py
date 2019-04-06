from django.urls import path

from . import views


urlpatterns = [
    path('', views.ingredient_list, name='user_ingredient_list'),
    path('ingredients/add/', views.add_user_ingredient, name='add_user_ingredient'),
]