from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, TemplateView
from datetime import datetime

from mainapp.models import Product, ProductCategories


now = datetime.today().strftime('%H:%M')


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'GeekShop'
        context['time'] = now
        return context


class ProductsView(ListView):
    paginate_by = 3
    model = Product
    template_name = 'mainapp/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs.get('category'):
            return qs.filter(category=self.kwargs.get('category'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategories.objects.all()
        context['time'] = now
        context['title'] = 'GeekShop - Каталог'

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
