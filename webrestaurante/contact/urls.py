from django.urls import path
from . import views as views


urlpatterns = [
    path('', views.contact, name="contact"),
    path('ejecutaAJAX/', views.ejecutaAJAX, name="ejecutaAJAX"),
    
]
