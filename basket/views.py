from django.urls import path
import basket.view as basket

app_name = 'basket'

urlpatterns = [
    path('', basketapp.index, name='index'),
]
