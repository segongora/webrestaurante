from django.urls import path
from . import views as views_services


urlpatterns = [
   
    path('services/', views_services.services, name="services"),

]
