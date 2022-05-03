from django.urls import path

from adminapp.views import admin_users, index, admin_user_create, admin_user_update, admin_user_delete, \
    admin_category, admin_category_update, admin_category_delete, admin_category_create, admin_products, \
    admin_product_create, admin_product_change, admin_product_delete

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_user_create, name='admin_user_create'),
    path('user-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('user-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('categories/', admin_category, name='admin_category'),
    path('category_update/<int:id>/', admin_category_update, name='category_update'),
    path('category_delete/<int:id>/', admin_category_delete, name='category_delete'),
    path('category_create/', admin_category_create, name='category_create'),
    path('admin_products/', admin_products, name='admin_products'),
    path('admin_product_create/', admin_product_create, name='admin_product_create'),
    path('admin_product_update/<int:id>/', admin_product_change, name='admin_product_update'),
    path('admin_product_delete/<int:id>/', admin_product_delete, name='admin_product_delete'),
]
