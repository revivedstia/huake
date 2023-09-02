from django.urls import path
from . import views


urlpatterns = [
    path('', views.ekskavator, name='ekskavator'),
    path('<int:pk>', views.EkskavatorDetailView.as_view(), name='ekskavator_detail')
]
