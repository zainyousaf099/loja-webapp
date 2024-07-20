from django.shortcuts import render, get_object_or_404
from .models import Product,Product_appliances,Product_Accesories
from category.models import Category,Category_appliances,Category_Accessories
# Create your views here.


def store(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:

        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)

    else:

        products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,

    }

    return render(request, 'store/store.html', context)


def store_appliances(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:

        categories = get_object_or_404(Category_appliances, slug=category_slug)
        products = Product_appliances.objects.filter(
            category=categories, is_available=True)

    else:

        products = Product_appliances.objects.all().filter(is_available=True)

    context = {
        'products': products,

    }

    return render(request, 'store/appliances.html', context)



def store_accesories(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:

        categories = get_object_or_404(Category_Accessories, slug=category_slug)
        products = Product_Accesories.objects.filter(
            category=categories, is_available=True)

    else:

        products = Product_Accesories.objects.all().filter(is_available=True)

    context = {
        'products': products,

    }

    return render(request, 'store/accesories.html', context)


def product_details(request,category_slug , product_slug):
    
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        
        raise e
    
    context = {
        
        'single_product': single_product,
        
    }
    return render(request, 'store/product_details.html',context)


def product_details_accesories(request,category_slug , product_slug):
    
    try:
        single_product = Product_Accesories.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        
        raise e
    
    context = {
        
        'single_product': single_product,
        
    }
    return render(request, 'store/product_details.html',context)


def product_details_appliances(request,category_slug , product_slug):
    
    try:
        single_product = Product_appliances.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        
        raise e
    
    context = {
        
        'single_product': single_product,
        
    }
    return render(request, 'store/product_details.html',context)