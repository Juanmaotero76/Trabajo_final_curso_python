from django.urls import path
from . import views


urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('crearnuevo/', views.crearproducto.as_view(), name='crearproducto'),
    path('motores/', views.Listademotores.as_view(), name='motores'),
    path('Detallemotor/<int:pk>/', views.Motordetalle.as_view(), name='motor'),
    path('editarmotor/<int:pk>/', views.Motoreditar.as_view(), name='editarmotor'),
    path('Borrarmotor/<int:pk>/', views.Eliminarmotor.as_view(), name='eliminarmotor'),
    path('busquedaproducto/', views.busquedaproducto, name='busquedaproducto'),
    
    path('aviones/', views.Listadeaviones.as_view(), name='aviones'),
    path('Detalleavion/<int:pk>/', views.Aviondetalle.as_view(), name='avion'),
    path('editaravion/<int:pk>/', views.Avioneditar.as_view(), name='editaravion'),
    path('Borraravion/<int:pk>/', views.Eliminaravion.as_view(), name='eliminaravion'),
    
    # path('motores/', views.Listaderadioes.as_view(), name='motores'),
    # path('Detallemotor/<int:pk>/', views.Radiodetalle.as_view(), name='motor'),
    # path('editarmotor/<int:pk>/', views.Radioeditar.as_view(), name='editarmotor'),
    # path('Borrarmotor/<int:pk>/', views.Eliminarradio.as_view(), name='eliminarmotor'),
    
    # path('motores/', views.Listadeotros.as_view(), name='motores'),
    # path('Detallemotor/<int:pk>/', views.Otrodetalle.as_view(), name='motor'),
    # path('editarmotor/<int:pk>/', views.Otroeditar.as_view(), name='editarmotor'),
    # path('Borrarmotor/<int:pk>/', views.EliminarOtro.as_view(), name='eliminarmotor'),
   
]