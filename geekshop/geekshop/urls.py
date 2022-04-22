from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('mainapp.urls', namespace='mainapp')),
    path('authapp/', include('authapp.urls', namespace='authapp')),
    path('basket/', include('basket.urls', namespace='basket')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
