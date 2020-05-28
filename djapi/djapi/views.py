from django.http import HttpResponse
import datetime


def saludo(request):
    return HttpResponse("Hola pues")

def despedida(request):
    return HttpResponse("Adios pues")

def givemetime(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calculaEdad(request, agno, edad):
    edadActual=edad
    periodo=agno-2020
    edadFutura=edadActual+periodo
    return HttpResponse("Tu edad es 18, en el año %s tendras %s" %(agno, edadFutura))
