from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryChange, AdminProductCreate
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

from mainapp.models import ProductCategories, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form': form
    }

    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админка | Обновление пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategories.objects.all(),
    }

    return render(request, 'adminapp/admin_category_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    product_cat_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = AdminCategoryChange(instance=product_cat_select, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
        else:
            print(form.errors)
    else:
        form = AdminCategoryChange(instance=product_cat_select)

    context = {
        'title': 'Обновление категории',
        'form': form,
        'product_cat_select': product_cat_select
    }
    return render(request, 'adminapp/admin_category_update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    category_select = ProductCategories.objects.get(id=id)
    category_select.is_active = False
    category_select.save()

    return HttpResponseRedirect(reverse('adminapp:categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = AdminCategoryChange(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
        else:
            errors = [error for error in form.errors.values()]
            messages.error(request, *errors)
    else:
        form = AdminCategoryChange()

    context = {
        'title': 'Создание категории',
        'form': form,
    }

    return render(request, 'adminapp/admin_category_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'Товары',
        'products': Product.objects.all(),
    }

    return render(request, 'adminapp/admin_products_show.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products_show'))
        else:
            errors = [error for error in form.errors.values()]
            messages.error(request, *errors)
    else:
        form = AdminProductCreate()

    context = {
        'title': 'Создание товара',
        'form': form,
    }

    return render(request, 'adminapp/admin_products_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_change(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductCreate(instance=product_select, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products_show'))
        else:
            print(form.errors)
    else:
        form = AdminProductCreate(instance=product_select)

    context = {
        'title': 'Изменение товара',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin_products_update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    product_select = Product.objects.get(id=id)
    product_select.is_active = False
    product_select.save()

    return HttpResponseRedirect(reverse('adminapp:admin_products_show'))