for i in [1,2,3]:
	print("Hola")

for i in ["primavera", "verano", "invierno"]:
	print(i)


#imprimir sin saltos de linea
for i in ["primavera", "verano", "invierno"]:
	print(i, end="")



#Dejar una separacion
for i in ["primavera", "verano", "invierno"]:
	print(i, end="  ")

print("")
#for que recorre el numero de caracteres de un string
y=0
for i in "andrea.com":
    y=y+1
    print(y)

#comprobar email con @
email=input("Introduce tu correo")
contador=0

for i in email:
	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:
	print("Correo validado")
else:
	print("Error")

#for con rango 

for i in range(5):
	print(i)

#para unir texto con el varlor de las variables, ejemplo en java es "el sueldo es " + sueldo, aqui se usa otra notación. con una f 

for i in range(6):
	print(f"valor de la variable {i}")


print(" ");

#que corra el for en un ranfo eterminado
for i in range(5,10):
	print(f"valor de la variable {i}")

print(" ");

#que corra el for en un ranfo eterminado pero en multiplos, el 21 esta excluido
for i in range(5,21,5):
	print(f"valor de la variable {i}")

print(" ");


#usar len para detectar la longitud del string 

nombre="Andrea";

for i in range(len(nombre)):
	print(f"valor de la variable {i}")













