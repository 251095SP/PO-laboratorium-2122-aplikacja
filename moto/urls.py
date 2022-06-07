
from django.urls import path

from . import views

app_name='moto'
urlpatterns = [
    path('', views.form_view),
    path('motocykle/', views.MotoListView.as_view(),name='index'),
    path('kierowcy/', views.KierowcaListView.as_view(),name='index'),
    path('zawody/', views.ZawodyListView.as_view(),name='index'),
]