
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    list_editable = ('price', 'stock', 'is_active', 'is_featured') # lets you change price and stock straight from the list page.
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}  # fills the slug automatically when we write the name 
