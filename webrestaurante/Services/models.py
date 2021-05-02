
from django.db import models

class Service (models.Model):
   title = models.CharField(max_length=200, verbose_name="Título")
   subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
   description = models.TextField(verbose_name="Descripción")
   image = models.ImageField(verbose_name="Imagen", upload_to='Services')
   created = models.DateTimeField(
   auto_now_add=True, verbose_name="Fecha de creación")
   updated = models.DateTimeField(
   auto_now=True, verbose_name="Fecha de actualizacion")
   class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-created']  # lo ordena de manera descendiente

   def __str__(self):
        return self.title