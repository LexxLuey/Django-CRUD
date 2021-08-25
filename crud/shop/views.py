from django.shortcuts import get_object_or_404, render
from .models import Category, Meal

# Create your views here.

def meal_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    meals = Meal.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        meals = meals.filter(category=category)
    
    return render(
        request, 'shop/meal/list.html',{
            'category': category,
            'categories': categories,
            'meals': meals,
            }
        )

def meal_detail(request, id, slug):
    meal = get_object_or_404(Meal, id=id, slug=slug, available=True)

    return render(request, 'shop/meal/detail.html', {'meal': meal})
