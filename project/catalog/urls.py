from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('pogruz/', include('pogruz.urls')),
    path('svayboy/', include('svayboy.urls')),
    path('ekskavator/', include('ekskavat.urls')),
    path('beton/', include('beton.urls')),
    path('vil_pogruz/', include('vil_pogruz.urls'))
]
