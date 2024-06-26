from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name=''),
    path('places/<id>/', views.get_place, name='places'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
