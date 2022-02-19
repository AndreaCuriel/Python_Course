import math

i=1

while i<=10:
	print(f"ejecución {i}");
	#print("Ejecición " + str(i))
	i=i+1

print("Termino")

edad=int(input("Introduce tu edad: "))

while edad<0 or edad>100:
	print("Has intoducido mal tu edad")
	edad=int(input("Introduce tu edad: "))


#uso de while con in if y break

print("raiz cuadrada")
numero=int(input("Introduce el numero: "))
intentos=0

while numero<0:
	print("no se puede hallar la raiz de nuemro negativos")

	if intentos==2:
		print("Has consumido tus oportunidades")
		break;

	numero=int(input("Introduce el numero: "))
	intentos=intentos+1
	

if intentos<2:
	solucion=math.sqrt(numero)
	print(f"la raiz es {solucion}")



