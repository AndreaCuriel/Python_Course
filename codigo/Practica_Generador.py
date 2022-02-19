#diferencia entre funcion y generalodr
#el generador va almacenando los datos como se van solicitando, a diferencia de la funcion, lo cual lo hace mas eficiente
#son utiles cuando tienes que generar datos infinitos, y que pueda continuar el programa
#primero hacer una funcion de numero pares
def generaPares(Limite):
	num=1
	miLista=[]
	while num<Limite:
		miLista.append(num*2)
		num=num+1
	return miLista


print(generaPares(10))

#Generador 
def generaPares1(Limite):
	num=1
	while num<Limite:
		yield num*2 #construye un objeto iterable, esta linea hace la diferencia entre una funcion y un generador 
		num=num+1 

devuelvePares=generaPares1(10)

#for i in devuelvePares: imprime dato por dato del valor del objeto iterable del generador 
	#print(i)
#Va llamando en cada print el generador, toma el siguiente valor y se imprime
#entra en un estado de suspension entre llamdas el generador 
print(next(devuelvePares)) #impreme solo un dato del generador
print("va mas codigo")
print(next(devuelvePares)) #imprime el siguiente dato 
print("va mas codigo")
print(next(devuelvePares))

#Usar Yield from, con bucles anidados 
def devuelve_ciudades(*ciudades): #va leer un numero indeterminado tipo tupla
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilboa", "Valencia")
print(next(ciudades_devueltas))

#ya que podemos acceder a cada elemento del objeto, ahora se accedera a cada letra de cada elemeto. para ello se necesita los for anidados 

def devuelve_ciudades1(*ciudades): #va leer un numero indeterminado tipo tupla
	for elemento in ciudades:
		for subelemento in elemento:
			yield subelemento

ciudades_devueltas1=devuelve_ciudades1("Madrid", "Barcelona", "Bilboa", "Valencia")
print(next(ciudades_devueltas1)) #entregara la M de Madrid 

#simplificar lo de arriba con yield from

def devuelve_ciudades2(*ciudades): #va leer un numero indeterminado tipo tupla
	for elemento in ciudades:
		yield from elemento # hace el efecto del for anidado de la linea 47

ciudades_devueltas2=devuelve_ciudades2("Madrid", "Barcelona", "Bilboa", "Valencia")
print(next(ciudades_devueltas2)) #entregara la M de Madrid 









