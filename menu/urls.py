from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_index, name='menu_index'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
]
