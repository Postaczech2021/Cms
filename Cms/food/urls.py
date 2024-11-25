from django.urls import path
from . import views
from .food_filters import *

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('list',views.food_list,name='food_list'),

    path('add',views.add_food, name='add_food'),
    path('edit/<int:id>',views.edit_food, name='edit_food'),
    path('delete/<int:id>',views.delete_food, name='delete_food'),

    path('store/add', views.add_store, name='add_store'),
    path('store/edit/<int:id>',views.edit_store, name='edit_store'),
    path('store/delete/<int:id>',views.delete_store, name='delete_store'),

    path('filter/category/<int:category_id>', filter_by_category, name='filter_by_category'),
    path('filter/store/<int:store_id>',filter_by_store,name='filter_by_store'),

    path('search', views.search_food, name='search_food'),
]
