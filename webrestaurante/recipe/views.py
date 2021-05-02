from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Recipe


# Create your views here

class RecipeUpdateView(UpdateView):
   model = Recipe
   fields= ['title','content','order']
   template_name_suffix = '_update_form'
   def get_success_url(self):
      return reverse_lazy("recipes:update", args=[self.object.id])+'?ok'

class RecipesDeleteView(DeleteView):
   model = Recipe
   success_url = reverse_lazy('recipes:recipes')

class RecipesCreateView(CreateView):
   model = Recipe
   fields= ['title','content','order']
   success_url = reverse_lazy('recipes:recipes')
   
class RecipesListView(ListView):
   model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe
