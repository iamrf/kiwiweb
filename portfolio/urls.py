from django.urls import path
from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:slug>/', views.item, name="item"),
]