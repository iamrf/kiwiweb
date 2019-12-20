from django.urls import path
from . import views


app_name = 'newsletter'
urlpatterns = [
    path('', views.get_newsletter, name="newsletter"),
    path('success/', views.success_newsletter, name="success"),
]