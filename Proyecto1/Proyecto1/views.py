from django.http import HttpResponse

def saludo(request): # primera vista
    return HttpResponse('Hola Alumnos.')

def despedida(request):
    return HttpResponse('Hasta luego!')