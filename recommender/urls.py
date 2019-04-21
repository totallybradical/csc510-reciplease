from django.urls import path

from . import views


urlpatterns = [
    path('', views.recommend, name='search'),
    
    path('ajax/load-ingredients', views.load_user_ingredients, name='ajax_load_ingredients'),
]
