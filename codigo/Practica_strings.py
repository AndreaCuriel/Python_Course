nombreusuario=input("Introduce tu nombre: ")
print("El nombre es: ", nombreusuario.capitalize()) #pone la primera edad en mayuscula
print("El nombre es: ", nombreusuario.lower()) #todo a minusculas
print("El nombre es: ", nombreusuario.upper()) #todo en mayusculas


edadusuario=input("Introduce tu edad: ")

while (edadusuario.isdigit()==False):
	print("Favor introoduce un valor numerico")
	edadusuario=input("Introduce tu edad: ")


print(edadusuario.isdigit())  #revisa si es un numero

if (int(edadusuario)<18):
	print("Es menor de edad")
else:
	print("Adulto")



