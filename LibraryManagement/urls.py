from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',RedirectView.as_view(url='catalog/',permanent=True)),
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/',include('catalog.api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
