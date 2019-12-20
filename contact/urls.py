from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    path('', views.get_contact, name="contact"),
    path('success/', views.success_contact, name="success")
]