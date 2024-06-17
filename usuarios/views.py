from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def loguin (request):
    formulario= AuthenticationForm()
    
    
    return render(request, 'usuarios/loguin.html', {})