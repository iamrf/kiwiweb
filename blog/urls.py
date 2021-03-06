from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<slug:slug>/', views.detail, name="detail"),
    path('categories/', views.categories, name="categories"),
    path('categories/<slug:slug>/', views.category, name="category"),
    path('tags/', views.tags, name="tags"),
    path('tags/<slug:slug>/', views.tag, name="tag"),
]