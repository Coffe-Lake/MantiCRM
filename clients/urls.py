from django.urls import include, path

from .views import validate_client

app_name = "clients"

urlpatterns = [
    path('validate_client', validate_client, name='validate_client')
]
