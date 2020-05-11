from django.urls import include, path

urlpatterns = [
    path('client/', include('web_client.client.urls')),
]
