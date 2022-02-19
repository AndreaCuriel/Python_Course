print("Asignaturas optativas")
print("Informatica, Pruebas, Economia")
opcion=input("Ingresa la asignatura que deseas ")
asignatura=opcion.lower()
#va comparar la variable con la cadena
if asignatura in ("informatica", "pruebas", "economia"):
	print("La asignatura elegida es " + asignatura)
else:
	print("Error")



