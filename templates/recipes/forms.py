
from django import forms
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe

        fields = [
            'title',
            'category',
            'description',
            'image',
            'cooking_time',
            'servings',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe your recipe'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),

            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }


class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient

        fields = [
            'ingredient',
            'quantity',
            'unit',
        ]

        widgets = {
            'ingredient': forms.Select(attrs={
                'class': 'form-select'
            }),

            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2'
            }),

            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. cups'
            }),
        }
