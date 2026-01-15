from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'portion_size',
        'unit',
    )

    list_filter = ('category', 'unit')
    search_fields = ('name', 'description')
