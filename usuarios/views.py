from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import Formulariocreate
# Create your views here.
def loguin (request):
    formulario= AuthenticationForm()
    if request.method=='POST':
        formulario= AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
           usuario=formulario.cleaned_data.get('username')
           contrasenia=formulario.cleaned_data.get('password')
           
           user=authenticate(request, username=usuario, password=contrasenia )
           login(request, user)
           
           return redirect('inicio')
    
    return render(request, 'usuarios/loguin.html', {'formulario':formulario})

def registro(request):
    formulario= Formulariocreate()
    if request.method=='POST':
        formulario= Formulariocreate(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('loguin')
        
    
    return render(request, 'usuarios/registro.html', {'formulario':formulario})