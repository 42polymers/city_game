from django.urls import include, path
from django.contrib.gis import admin

urlpatterns = [
    path('client/', include('web_client.client.urls')),
    # path('admin/', include('web_client.client.admin.site.urls')),
    # path('admin/', admin.site.urls, name='admin'),
    path('admin/', admin.site.urls),
]
