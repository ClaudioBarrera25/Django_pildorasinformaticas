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

def calcular_edad(request, edad, anio):
    periodo = anio - 2019 
    edad_futura = edad + periodo
    documento = f'<html><body><h2>En el año {anio} tendrás {edad_futura} años.</h2></body></html>'
    return HttpResponse(documento)