from django.urls import path
from . import views


urlpatterns = [
    path('motores/', views.motores.as_view(), name='motores'),
    path('motores/crear/', views.crearmotores.as_view(), name='crear_motores'),
    path('motores/<int:pk>/', views.vermotores.as_view(), name='vermotores'),
    path('motores/<int:pk>/editar', views.editarmotores.as_view(), name='editarmotores'),
    path('motores/<int:pk>/eliminar', views.eliminarmotores.as_view(), name='eliminarmotores'),
   
]