from django.urls import path

from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, IndexTemplateView, \
    AdminCategoryView, AdminCategoryUpdateView, AdminCategoryDeleteView, AdminCategoryCreateView, AdminProductsShowView, \
    AdminProductCreateView, AdminProductChangeView, AdminProductDeleteView

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='admin_user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_user_delete'),
    path('categories/', AdminCategoryView.as_view(), name='admin_category'),
    path('category_update/<int:pk>/', AdminCategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', AdminCategoryDeleteView.as_view(), name='category_delete'),
    path('category_create/', AdminCategoryCreateView.as_view(), name='category_create'),
    path('admin_products/', AdminProductsShowView.as_view(), name='admin_products'),
    path('admin_product_create/', AdminProductCreateView.as_view(), name='admin_product_create'),
    path('admin_product_update/<int:pk>/', AdminProductChangeView.as_view(), name='admin_product_update'),
    path('admin_product_delete/<int:pk>/', AdminProductDeleteView.as_view(), name='admin_product_delete'),
]
