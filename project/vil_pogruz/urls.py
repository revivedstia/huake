from django.urls import path
from . import views


urlpatterns = [
    path('', views.vil_pogruz, name='vil_pogruz'),
    path('<int:pk>', views.Vil_pogruzDetailView.as_view(), name='vil_pogruz_detail')
]
