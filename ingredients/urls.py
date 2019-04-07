from django.urls import path

from . import views


urlpatterns = [
    path('', views.ingredient_list, name='user_ingredient_list'),
    path('add/', views.add_user_ingredient, name='add_user_ingredient'),
    path('new/', views.add_ingredient_type, name='add_ingredient_type'),
]