from django.urls import path
from . import views


urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('crearnuevo/', views.crearproducto.as_view(), name='crearproducto'),
    path('motores/', views.Listademotores.as_view(), name='motores'),
    path('Detallemotor/<int:pk>/', views.Motordetalle.as_view(), name='detail'),
    path('editarmotor/<int:pk>/', views.Motoreditar.as_view(), name='edit'),
    path('Borrarmotor/<int:pk>/', views.Eliminarmotor.as_view(), name='eliminar'),
    path('busquedaproducto/', views.busquedaproducto, name='busquedaproducto'),
    
    path('aviones/', views.Listadeaviones.as_view(), name='aviones'),
    path('Detalleavion/<int:pk>/', views.Aviondetalle.as_view(), name='detail'),
    path('editaravion/<int:pk>/', views.Avioneditar.as_view(), name='edit'),
    path('Borraravion/<int:pk>/', views.Eliminaravion.as_view(), name='eliminar'),
    
    path('radios/', views.Listaderadios.as_view(), name='radios'),
    path('Detalleradio/<int:pk>/', views.Radiodetalle.as_view(), name='detail'),
    path('editarradio/<int:pk>/', views.Radioditar.as_view(), name='edit'),
    path('Borrarradio/<int:pk>/', views.Eliminarradio.as_view(), name='eliminar'),
    
    
    # path('motores/', views.Listaderadioes.as_view(), name='motores'),
    # path('Detallemotor/<int:pk>/', views.Radiodetalle.as_view(), name='motor'),
    # path('editarmotor/<int:pk>/', views.Radioeditar.as_view(), name='editarmotor'),
    # path('Borrarmotor/<int:pk>/', views.Eliminarradio.as_view(), name='eliminarmotor'),
    
    # path('motores/', views.Listadeotros.as_view(), name='motores'),
    # path('Detallemotor/<int:pk>/', views.Otrodetalle.as_view(), name='motor'),
    # path('editarmotor/<int:pk>/', views.Otroeditar.as_view(), name='editarmotor'),
    # path('Borrarmotor/<int:pk>/', views.EliminarOtro.as_view(), name='eliminarmotor'),
   
]