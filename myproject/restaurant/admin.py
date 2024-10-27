from django.contrib import admin
from .models import Category, Product, Extra, Drinks, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at', 'telegram', 'instagram',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'product']
    list_filter = ['product']
    search_fields = ['name']

@admin.register(Drinks)
class DrinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'product']
    list_filter = ['product']
    search_fields = ['name']




