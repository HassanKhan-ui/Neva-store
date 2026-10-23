from django.db.models import Count, Q
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product

def home(request):
    categories = Category.objects.annotate(
        product_count=Count('products', filter=Q(products__is_active=True))
    )
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


def catalogue(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()

    search_query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query)
            | Q(short_description__icontains=search_query)
        )

    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = request.GET.copy()
    params.pop('page', None)
    query_string = params.urlencode()

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
        'query_string': query_string,
    }

    return render(request, 'store/catalogue.html', context)