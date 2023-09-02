from django.urls import path
from . import views


urlpatterns = [
    path('', views.svayboy, name='svayboy'),
    path('<int:pk>', views.SvayboyDetailView.as_view(), name='svayboy_detail')
]
