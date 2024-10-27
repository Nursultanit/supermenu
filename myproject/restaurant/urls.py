from django.urls import path
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ExtraViewSet,
    DrinksViewSet,
)

urlpatterns = [

    path('', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),


    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product_detail'),


    path('extras/', ExtraViewSet.as_view({'get': 'list', 'post': 'create'}), name='extra_list'),
    path('extras/<int:pk>/', ExtraViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='extra_detail'),


    path('drinks/', DrinksViewSet.as_view({'get': 'list', 'post': 'create'}), name='drink_list'),  # Исправлено
    path('drinks/<int:pk>/', DrinksViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='drink_detail'),  # Исправлено
]
