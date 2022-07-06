from django.contrib import admin
from django.urls import path, include

# Imports to help link MEDIA_ROOT to MEDIA_URLS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
