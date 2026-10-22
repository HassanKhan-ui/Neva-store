from django.shortcuts import render
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    featured_products = (
        Product.objects.filter(is_active=True, is_featured=True)
        .select_related('category')[:8]
    )
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    
    return render(request, 'index.html', context)
    

def product(request):
    return render(request, 'product.html')