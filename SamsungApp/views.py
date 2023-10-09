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
    
    contexto = {"celulares" : Celular.objects.all()}
    return render(req, 'inicio.html', contexto,)

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


class CelularCreate(LoginRequiredMixin, CreateView):
    
    model = Celular
    template_name = 'celular_creation.html'
    next_page = reverse_lazy('list')
    fields = ('__all__')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CelularUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Celular
    template_name = 'celular_form.html'
    success_url = '/SamsungApp/celular/list'
    fields = ('__all__')
    
        
class CelularDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Celular
    template_name = 'celular_confirm_delete.html'
    success_url = '/SamsungApp/celular/list'
    
class Login(LoginView):
    template_name = 'login.html'
    fields = ('__all__')
    next_page = reverse_lazy('Inicio')

    
class SignUp(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('Inicio')
    
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('Inicio')
    
    def get_object(self):
        return self.request.user

class PostPagina(LoginRequiredMixin, CreateView):
    model = Post
    form_class = FormularioPost
    template_name = 'mensaje.html'
    success_url = reverse_lazy('Mensajeenviado')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def mensajeEnviado(request):
    return render(request, 'mensaje_enviado.html')