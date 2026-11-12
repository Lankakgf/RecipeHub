
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Recipe, Category

def home(request):
    recipes = Recipe.objects.select_related(
        'user', 'category'
    ).prefetch_related(
        'ingredients__ingredient'
    ).order_by('-created_at')

    categories = Category.objects.all()

    search = request.GET.get('search', '').strip()
    category_id = request.GET.get('category', '')

    if search:
        recipes = recipes.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(ingredients__ingredient__name__icontains=search)
        ).distinct()

    if category_id.isdigit():
        recipes = recipes.filter(category_id=category_id)

    context = {
        'recipes': recipes,
        'categories': categories,
        'search': search,
        'selected_category': category_id,
    }

    return render(request, 'recipes/home.html', context)



def recipe_detail(request, pk):

    recipe = get_object_or_404(
        Recipe.objects.select_related(
            'user', 'category'
        ).prefetch_related(
            'ingredients__ingredient'
        ),
        pk=pk
    )

    return render(
        request,
        'recipes/detail.html',
        {'recipe': recipe}
    )


@login_required
def create_recipe(request):

    if request.method == 'POST':
        form = RecipeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            return redirect(
                'recipe_detail',
                pk=recipe.pk
            )

    else:
        form = RecipeForm()

    return render(
        request,
        'recipes/create.html',
        {'form': form, 'action': 'Create'}
    )


@login_required
def edit_recipe(request, pk):

    recipe = get_object_or_404(
        Recipe,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe
        )

        if form.is_valid():
            form.save()

            return redirect(
                'recipe_detail',
                pk=recipe.pk
            )

    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        'recipes/create.html',
        {'form': form, 'action': 'Update'}
    )


@login_required
def delete_recipe(request, pk):

    recipe = get_object_or_404(
        Recipe,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    return render(
        request,
        'recipes/delete.html',
        {'recipe': recipe}
    )
