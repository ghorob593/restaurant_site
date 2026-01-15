from django.shortcuts import render, get_object_or_404
from .models import Category, Dish
from django.db.models import Q

def home(request):
    dishes = Dish.objects.all()[:3] 
    return render(request, 'menu/home.html', {'dishes': dishes})

def menu_index(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    dishes = Dish.objects.all()
    categories = Category.objects.all()

    if query:
        dishes = dishes.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        dishes = dishes.filter(category_id=category_id)

    return render(request, 'menu/menu_index.html', {
        'dishes': dishes,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    })

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/categories_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    dishes = Dish.objects.filter(category=category)

    return render(request, 'menu/category_detail.html', {
        'category': category,
        'dishes': dishes
    })


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'menu/dish_detail.html', {
        'dish': dish
    })