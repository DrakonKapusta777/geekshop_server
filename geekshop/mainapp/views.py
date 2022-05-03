from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategories


def index(request):
    content = {
        'title': 'Geekshop'
    }

    return render(request, 'mainapp/index.html', content)


def products(request, id_category=None, page=1):
    if id_category:
        products_ = Product.objects.filter(category_id=id_category)
    else:
        products_ = Product.objects.all()

    pagination = Paginator(products_, per_page=3)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)
    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_pagination
    }

    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'