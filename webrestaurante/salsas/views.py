from django.shortcuts import render
from .models import Salsa
from django.views.generic.base import TemplateView

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import PedidoForm

class SalsaCreatePedido(CreateView):
   form_class = PedidoForm
   template_name = "salsas/pedido_cliente.html"
   success_url = reverse_lazy('salsas:success_pedido')
   
   def form_valid(self, form):
      # Guarda los datos del pedido
      pedido_nuevo = form.save(commit=False)
      pedido_nuevo.save()
      return super().form_valid(form)

   def get_form_kwargs(self):
      """Coloca el request disponible, para después obtener la sesión en la forma."""
      kwargs = super(SalsaCreatePedido, self).get_form_kwargs()
      kwargs['request'] = self.request
      return kwargs

class PedidoSuccess(TemplateView):
   template_name = "salsas/pedido_success.html"


def _creaDiccionario(datos_pedido):
   diccionario = {}
   datos_pedido = datos_pedido[:-1]
   productos = datos_pedido.split('|')
   for producto in productos:
      detalle = producto.split("-")
      diccionario[detalle[0]] = int(detalle[1])
   return diccionario

def realizar_pedido(request):
   pedido = list()
   if request.method == 'POST':
      datos_pedido = request.POST['datos_pedido']
      productos = _creaDiccionario(datos_pedido)
      total = 0
      for codigo_barra in productos.keys():
         cantidad = productos[codigo_barra]
         if cantidad > 0:
            dict_producto = {}
            receta = Salsa.objects.get(pk=codigo_barra)
            dict_producto['id'] = receta.id
            dict_producto['descripcion'] = receta.name
            dict_producto['cantidad'] = cantidad
            dict_producto['precio'] = receta.price
            total += cantidad * receta.price
            pedido.append(dict_producto)
      # Coloca en variable de sesión el total y el pedido
      request.session['total_float'] = float(total)
      request.session['detalle_pedido'] = pedido

   return render(request, "salsas/detalle_pedido.html", {"pedido": pedido, "total": total})


class SalsaTemplateView(TemplateView):
    template_name = "salsas/salsas.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salsas'] = Salsa.objects.all()
        return context
