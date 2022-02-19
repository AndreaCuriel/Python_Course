'''	print("creando una funcion")

mensaje()

#ciclo for que llama la función mensaje
for i in range(5):
	mensaje()'''

#declaración de una funcion 
def suma():
	num1=5
	num2=7
	print(num1+num2)

#llamar la funcion
suma()

#función como parametros 
def suma(num1, num2):
	print(num1+num2)

suma(5, 5)

#funcion con return

def suma2(num1, num2):
	resultado=num1+num2
	return resultado  #a si puedes almacenar el resultado en una variable y poder utilizarla despues 

#se llama el metodo, con un print para que se vea el resultado 
print(suma2(7,8))

almacena_resultado=suma2(8,8)
print(almacena_resultado)








