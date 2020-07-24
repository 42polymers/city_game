from django.conf import settings
from django.conf.urls.static import static
from django.contrib.gis import admin
from django.urls import include, path


urlpatterns = [
    path('client/', include('web.client.urls')),
    # path('admin/', include('web.client.admin.site.urls')),
    # path('admin/', admin.site.urls, name='admin'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
