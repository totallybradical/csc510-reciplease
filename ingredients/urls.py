from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    path('', views.ingredient_list, name='user_ingredient_list'),
    path('add/', views.add_user_ingredient, name='add_user_ingredient'),
    path('new/', views.add_ingredient_type, name='add_ingredient_type'),
    path('expiring/', views.expiring_ingredients, name='expiring_user_ingredient_list'),
    url(r'^(?P<id>\d+)/delete/$', views.delete_user_ingredient, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', views.edit_user_ingredient, name='edit')    

]
