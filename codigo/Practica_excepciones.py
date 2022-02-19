#ver la funcionalidad de las excepciones
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplicacion(num1, num2):
	return num1*num2

def division(num1, num2):
	#se usara un try, para creaar la excepcion
	try: 
		num1/num2
	except ZeroDivisionError: #el nombre del error lo encuentra al correr el programa
		print("no se puede dividir")
		return "operacion erronea"

while True: #un bucle infinito cuando los datos ingresados no son enteros, controlando el error
	
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break #rompe el bucle si los datos ingresados son validos

	except ValueError:
		print("Datos incorrectos, Intente de nuevo.")

operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, division): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplicacion":
	print(multiplicacion(op1,op2))

elif operacion=="division":
	print(division(op1,op2))

else:
	print("no existe")

print("continuacion de la ejecución")



