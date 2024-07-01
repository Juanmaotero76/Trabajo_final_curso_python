from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('loguin/', views.loguin, name='loguin'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('bienvenida/', views.Bienvenida, name='bienvenida'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/ver/', views.Verperfil, name='ver_perfil'),
    path('perfil/editar/cambiarpass', views.cambiarpass.as_view(), name='cambiar_pass'),
    path('enviar/', views.send_message, name="enviar"),
    path('mensajes/', views.message_list, name="lista"),

]
