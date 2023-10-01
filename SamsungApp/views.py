from django.shortcuts import render
from django.http import HttpResponse
from .models import Celular, Post, Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import *


def inicio(req):
    
    return render(req, 'inicio.html')

def sobremi(req):
    return render(req, 'about.html')

def anadircelular(request):
    
    if request.method == 'POST':
        
        miFormulario = Formulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
      
            celular =  Celular(nombre = informacion['nombre'], 
                               serie = informacion['serie'], 
                               precio = informacion['precio'], 
                               memoria = informacion['memoria'], 
                               pantalla = informacion['pantalla'], 
                               camara = informacion['camara'] )
 
            celular.save()
 
            return render(request, "inicio.html", {'mensaje': 'Celular creado con exito!'})
        else:
            return render(request, "inicio.html", {'mensaje': 'No se creó con exito...'})

        
    else:
            miFormulario = Formulario()
 
    return render(request,"anadircelular.html", {'miFormulario': miFormulario})

def busqueda_celular(req):
    
    return render(req, 'busquedacelular.html')
    
class CelularList(ListView):
    
    model = Celular
    template_name = 'celular_list.html'
    
class CelularDetail(DetailView):
    
    model = Celular
    template_name = 'celular_detalle.html'


class CelularCreate(CreateView):
    
    model = Celular
    template_name = 'anadircelular.html'
    success_url = '/SamsungApp/celular/list'
    fields = ('__all__')
    
class CelularUpdate(UpdateView):
    
    model = Celular
    template_name = 'celular_form.html'
    success_url = '/SamsungApp/celular/list'
    fields = ('__all__')
    
        
class CelularDelete(DeleteView):
    
    model = Celular
    template_name = 'celular_confirm_delete.html'
    success_url = '/SamsungApp/celular/list'
    
class Login(LoginView):
    template_name = 'login.html'
    fields = ('__all__')
    success_url = reverse_lazy('inicio.html')

    
class SignUp(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('Inicio')
    
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('Inicio')
    