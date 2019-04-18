from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    url(r'^(?P<id>\d+)/$', views.recipe_detail, name='detail'),
]