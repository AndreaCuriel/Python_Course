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
