from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    path('', views.ingredient_list, name='user_ingredient_list'),
    path('add/', views.add_user_ingredient, name='add_user_ingredient'),
    path('new/', views.add_ingredient_type, name='add_ingredient_type'),
    path('expiring/', views.expiring_ingredients, name='expiring_user_ingredient_list'),
    path('<int:id>/delete/', views.delete_user_ingredient, name='delete_user_ingredient'),
    path('<int:id>/edit/', views.edit_user_ingredient, name='edit_user_ingredient')    

]
