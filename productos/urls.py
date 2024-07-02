from django.urls import path
from . import views


urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('crearnuevo/', views.crearproducto.as_view(), name='crearproducto'),
    path('busquedaproducto/', views.busquedaproducto, name='busquedaproducto'),
    
    path('motores/', views.Listademotores.as_view(), name='motores'),
    path('Detallemotor/<int:pk>/', views.Motordetalle.as_view(), name='detailmo'),
    path('editarmotor/<int:pk>/', views.Motoreditar.as_view(), name='editmo'),
    path('Borrarmotor/<int:pk>/', views.Eliminarmotor.as_view(), name='eliminarmo'),
    
    
    path('aviones/', views.Listadeaviones.as_view(), name='aviones'),
    path('Detalleavion/<int:pk>/', views.Aviondetalle.as_view(), name='detail'),
    path('editaravion/<int:pk>/', views.Avioneditar.as_view(), name='editav'),
    path('Borraravion/<int:pk>/', views.Eliminaravion.as_view(), name='eliminarav'),
    
    path('radios/', views.Listaderadios.as_view(), name='radios'),
    path('Detalleradio/<int:pk>/', views.Radiodetalle.as_view(), name='detail'),
    path('editarradio/<int:pk>/', views.Radioditar.as_view(), name='editra'),
    path('Borrarradio/<int:pk>/', views.Eliminarradio.as_view(), name='eliminarra'),
    
    path('otros/', views.Listadeotros.as_view(), name='otros'),
    path('Detalleotros/<int:pk>/', views.Otrodetalle.as_view(), name='detail'),
    path('editarotros/<int:pk>/', views.Otroeditar.as_view(), name='editot'),
    path('Borrarotros/<int:pk>/', views.Eliminarotro.as_view(), name='eliminarot'),  
   
]