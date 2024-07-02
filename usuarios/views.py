from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from usuarios.forms import Formulariocreate, Formularioeditar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosAdicionales
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from productos.models import Producto

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
           DatosAdicionales.objects.get_or_create(user=user)
           
           return redirect('bienvenida')
    
    return render(request, 'usuarios/loguin.html', {'formulario':formulario})

def registro(request):
    formulario= Formulariocreate() 
    if request.method=='POST':
        formulario= Formulariocreate(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('loguin')
        
    
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

def Bienvenida (request):
   
    return render(request, 'usuarios/bienvenida.html')

def Verperfil (request):
   
    return render(request, 'usuarios/ver_perfil.html')


@login_required
def editar_perfil(request):
    datosextra=request.user.datosadicionales
    formulario=Formularioeditar(initial={'avatar': datosextra.avatar}, instance= request.user)
    if request.method=='POST':
        formulario= Formularioeditar(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            datosextra= request.user.datosadicionales
            datosextra.avatar=formulario.cleaned_data.get('avatar')
            datosextra.ciudad=formulario.cleaned_data.get('ciudad')
            datosextra.save()
            formulario.save()
        
            return redirect('inicio')
    return render(request, 'usuarios/editar_perfil.html' , {'formulario':formulario})

class cambiarpass(LoginRequiredMixin, PasswordChangeView):
    template_name='usuarios/cambiar_pass.html'
    success_url=reverse_lazy('editar_perfil')
    
    
    
@login_required
def send_message(request):
    
    if request.method == 'POST':
        recipient_username = request.POST['recipient']
        message_content = request.POST['message']

        try:
            recipient = User.objects.get(username=recipient_username)
            Message.objects.create(sender=request.user, recipient=recipient, content=message_content)
            return redirect('lista')
        except User.DoesNotExist:
            return render(request, 'usuarios/send_message.html', {'error': 'User not found'})

    return render(request, 'usuarios/send_message.html')

@login_required
def message_list(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    context = {'messages': messages}
    return render(request, 'usuarios/message_list.html', context)
  