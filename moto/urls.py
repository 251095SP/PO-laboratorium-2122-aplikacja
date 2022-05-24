
from django.urls import path

from . import views

app_name='moto'
urlpatterns = [
    path('/motocykle/', views.MotoListView.as_view(),name='index'),
    path('/kierowcy/', views.KierowcaListView.as_view(),name='index'),
]