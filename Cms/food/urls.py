from django.urls import path
from . import views
from .food_filters import filter_by_category

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('list',views.food_list,name='food_list'),
    path('add/store',views.add_store, name='add_store'),
    path('add',views.add_food, name='add_food'),
    path('edit/food/<int:id>',views.edit_food, name='edit_food'),
    path('edit/store/<int:id>',views.edit_store, name='edit_store'),
    path('delete/store/<int:id>',views.delete_store, name='delete_store'),
    path('filter/category/<int:category_id>', filter_by_category, name='filter_by_category'),
    path('search', views.search_food, name='search_food'),
]
