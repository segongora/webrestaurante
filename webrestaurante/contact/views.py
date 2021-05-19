from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse
import time
# Create your views here.


def ejecutaAJAX(request):
    if request.method == 'POST':
        opcion = request.POST.get('valor', '')
        respuesta = {}
        if opcion == '1' or opcion == '2':
            respuesta['estado'] = 'correcto'
            opciones = {}
            opciones['1'] = 'Opcion1'
            opciones['2'] = 'Opcion2'
            opciones['3'] = 'Opcion3'
            opciones['4'] = 'Opcion4'
            opciones['5'] = 'Opcion5'
            respuesta['opciones'] = opciones
        else:
            respuesta['estado'] = 'incorrecto'

        time.sleep(5)
        return JsonResponse(respuesta)

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # reverse resuelve el irl de forma dinamica

            # send email
            send_mail(
                'Mensaje Prueba de ' + name, email+' '+content, email,
                ['segongora9@gmail.com'],
                fail_silently=False,
            )

            return redirect(reverse('contact')+'?ok')
    return render(request, "contact/contact.html", {'form': contact_form})
