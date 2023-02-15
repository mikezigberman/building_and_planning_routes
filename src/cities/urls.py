from django.urls import path

from cities.views import *

from cities.views import CityCreateView, CityUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('add/', CityCreateView.as_view(), name='create'),
]