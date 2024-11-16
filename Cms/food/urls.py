from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/store',views.add_store, name='add_store'),
    path('add/food',views.add_food, name='add_food'),
    path('edit/store/<int:id>',views.edit_store, name='edit_store'),
    path('delete/store/<int:id>',views.delete_store, name='delete_store'),

]
