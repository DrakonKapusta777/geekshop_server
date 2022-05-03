from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryChange, AdminProductCreate
from adminapp.mixin import BaseClassContextMixin, SuperuserDispatchMixin, AuthorisationDispatchMixin
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView

from mainapp.models import ProductCategories, Product


class IndexTemplateView(TemplateView, BaseClassContextMixin, SuperuserDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главня страница'


class UserListView(ListView, BaseClassContextMixin, SuperuserDispatchMixin, AuthorisationDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'


class UserCreateView(CreateView, BaseClassContextMixin, SuperuserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


class UserUpdateView(UpdateView, BaseClassContextMixin, SuperuserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


class UserDeleteView(DeleteView, SuperuserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminCategoryView(ListView, SuperuserDispatchMixin, BaseClassContextMixin):
    template_name = 'adminapp/admin_category_read.html'
    title = 'GeekShop | Админка'
    model = ProductCategories
    context_object_name = 'categories'
    success_url = reverse_lazy('adminapp:admin_category')


class AdminCategoryUpdateView(UpdateView, SuperuserDispatchMixin, BaseClassContextMixin):
    model = ProductCategories
    template_name = 'adminapp/admin_category_update-delete.html'
    form_class = AdminCategoryChange
    title = 'Обновление категории'
    context_object_name = 'product_cat_select'
    success_url = reverse_lazy('adminapp:admin_category')


class AdminCategoryDeleteView(DeleteView, SuperuserDispatchMixin, BaseClassContextMixin):
    model = ProductCategories
    template_name = 'adminapp/admin_category_update-delete.html'
    success_url = reverse_lazy('adminapp:admin_category')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.success_url)


class AdminCategoryCreateView(CreateView, SuperuserDispatchMixin, BaseClassContextMixin):
    model = ProductCategories
    title = 'Создание категории'
    template_name = 'adminapp/admin_category_create.html'
    form_class = AdminCategoryChange
    success_url = reverse_lazy('adminapp:admin_category')


class AdminProductsShowView(ListView, SuperuserDispatchMixin, BaseClassContextMixin):
    title = 'Товары'
    model = Product
    context_object_name = 'products'
    template_name = 'adminapp/admin_products_show.html'


class AdminProductCreateView(CreateView, SuperuserDispatchMixin, BaseClassContextMixin):
    title = 'Создание товара'
    template_name = 'adminapp/admin_products_create.html'
    form_class = AdminProductCreate
    model = Product


class AdminProductChangeView(UpdateView, SuperuserDispatchMixin, BaseClassContextMixin):
    template_name = 'adminapp/admin_products_update-delete.html'
    title = 'Изменение товара'
    form_class = AdminProductCreate
    model = Product
    context_object_name = 'product_select'
    success_url = reverse_lazy('adminapp:admin_products')


class AdminProductDeleteView(DeleteView, SuperuserDispatchMixin, BaseClassContextMixin):
    model = Product
    success_url = reverse_lazy('adminapp:admin_products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.success_url)
