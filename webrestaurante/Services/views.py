from django.shortcuts import render
from .models import Service


def services(request):
    servs = Service.objects.all()
    return render(request, "Services/services.html", {"services": servs})
