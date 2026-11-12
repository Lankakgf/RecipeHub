
from django.db import models
from django.contrib.auth.models import User


# 1. Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# 2. Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 3. Recipe Model
class Recipe(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to="recipes/",
        blank=True,
        null=True
    )

    cooking_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 4. RecipeIngredient Model
class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient.name}"
