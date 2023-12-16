from django.http import HttpResponse
import datetime

def saludo(request): # primera vista
    documento = '<html><body><h1>Hola Alumnos.</h1></body></html>'
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Hasta luego!')

def obtener_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = f'<html><body><h1>fecha {fecha_actual}.</h1></body></html>'
    return HttpResponse(documento)
