from django.shortcuts import render
from appOrganizacion.models import *
import os

# Create your views here.
def historia(request):
    return render(request, 'historia.html')


def misionVision(request):
    return render(request, 'misionVision.html')

def objetivos(request):
    return render(request, 'objetivos.html')

def vistaCorreoForgot(request):
    return render(request, 'vistaCorreoForgot.html')

def donar(request):
    return render(request, 'donar.html')

def inicio(request):
    """
    Esta vista renderiza la página de inicio.

    Args:
        request (HttpRequest): El objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza la página de inicio (inicio.html).
    """
    return render(request, 'inicio.html')