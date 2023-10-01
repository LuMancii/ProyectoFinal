from django.urls import path
from SamsungApp import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sobre-mi/', sobremi, name='Sobremi'),
    path('', inicio , name = 'Inicio'),
    path('busqueda-celular/', busqueda_celular , name = 'BusquedaCelular'),
    path('celular/list', CelularList.as_view() , name = 'List'),
    path(r'^(?P<pk>\d+)$', views.CelularDetail.as_view() , name = 'Detail'),
    path(r'^nuevo$', views.CelularCreate.as_view() , name = 'New'),
    path(r'^editar/(?P<pk>\d+)$', views.CelularUpdate.as_view() , name = 'Update'),
    path(r'^borrar/(?P<pk>\d+)$', views.CelularDelete.as_view() , name = 'Delete'),
    path('login/', Login.as_view() , name = 'Login'),
    path('signup/', SignUp.as_view() , name = 'Signup'),
    path('logout/', LogoutView.as_view(template_name ='logout.html' ) , name = 'Logout'),
    path('edicion-perfil/', UsuarioEdicion.as_view , name = 'Edicionperfil'),
]