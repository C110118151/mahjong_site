# mahjong_db/urls.py

from django.urls import path
from . import views

app_name = "mahjong_db"

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_record, name='add_record'),
]
