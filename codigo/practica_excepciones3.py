def evaluaEdad(edad):

	if edad<0:
		raise TypeError("No se permiten edades negativas") #lanzar una excepcion y con ello cae el programa
	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Ers joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Tienes que cuidate"


print(evaluaEdad(10))

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError ("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

#controlaremos la excepcion y aparte le daremos un nombre con as

op1=(int(input("Introduce un númer: ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("Progrma terminado")



