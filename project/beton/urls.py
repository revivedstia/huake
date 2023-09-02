from django.urls import path
from . import views


urlpatterns = [
    path('', views.beton, name='beton'),
    path('<int:pk>', views.BetonDetailView.as_view(), name='beton_detail')
]
