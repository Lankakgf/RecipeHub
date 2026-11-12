
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'recipe/<int:pk>/',
        views.recipe_detail,
        name='recipe_detail'
    ),

    path(
        'recipe/create/',
        views.create_recipe,
        name='create_recipe'
    ),

    path(
        'recipe/<int:pk>/edit/',
        views.edit_recipe,
        name='edit_recipe'
    ),

    path(
        'recipe/<int:pk>/delete/',
        views.delete_recipe,
        name='delete_recipe'
    ),
]
