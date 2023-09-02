from django.urls import path
from . import views


urlpatterns = [
    path('', views.pogruz, name='pogruz'),
    path('<int:pk>', views.PogruzDetailView.as_view(), name='pogruz_detail')
]
