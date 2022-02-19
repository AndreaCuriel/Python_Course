#importar el modulo para utilizar los objetos para la peticion
from django.http import HttpResponse
#se creo una funcion que recibe como argumento un objeto request 
def saludo(request):  #funcion vista, primera vista, que devuelve una respuesta
    return HttpResponse("Mi primera pagina con Django")

#hay que indicar el url, enlazar la url para que nos lance la vista de la funcion, nos camos a urls.py
#abrir la consola para abrir el servidor, y correr la url + saludo, que es el path que agregamos en urls.py

def salida(request):  #funcion vista, primera vista, que devuelve una respuesta
    return HttpResponse("Nos vemos")
    