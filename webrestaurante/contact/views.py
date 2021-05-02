from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')
            #reverse resuelve el irl de forma dinamica

            #send email 
            send_mail(
    'Mensaje Prueba de ' +name, email+' '+content, email,
    ['ivannamarcelle@gmail.com'],
    fail_silently=False,
)

            return redirect(reverse('contact')+'?ok')
    return render(request, "contact/contact.html", {'form': contact_form})
