
from django import forms
from .models import Recipe


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
                'placeholder': 'Enter recipe title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'servings': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }
