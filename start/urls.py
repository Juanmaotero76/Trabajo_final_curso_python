from django.urls import path

from start import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('contacto/', views.contacto, name='contacto'),
    path('about/', views.about, name='about'),
]