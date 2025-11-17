from django.urls import path
from . import views # core/views.py-г импортлох
urlpatterns = [
    # Үндсэн хаяг (жишээ нь: /) орж ирвэл
    # views.index функцийг ажиллуул
    path('', views.index, name='home'),
]