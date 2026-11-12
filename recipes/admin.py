
from django.contrib import admin

from .models import (
    Category,
    Ingredient,
    Recipe,
    RecipeIngredient
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'user',
        'category',
        'cooking_time',
        'servings',
        'created_at'
    )

    list_filter = ('category', 'created_at')

    search_fields = (
        'title',
        'description',
        'user__username'
    )

    list_per_page = 10
    ordering = ('-created_at',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'recipe',
        'ingredient',
        'quantity',
        'unit'
    )
