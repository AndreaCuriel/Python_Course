#Polimorfismo viene de poli, muchas, morfismo de formas

class Coche():
    def desplazamiento(self):
        print("me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")

#magia del polimorfismo
#creando un metodo desplazamiento que recibira un objeto 

def desplazamientoVehiculo(vehiculo): #este objeto vehiculo sabra en que metodo dirigirse, por su caracteristica de polimorfismo 
    vehiculo.desplazamiento()





#-----------------Instancias--------------------------


miVehiculo=Moto()

miVehiculo2=Coche()

miVehiculo3=Camion()

#magia del polimorfismo, llamaremos el método el cual identificara que metodo del mismo nombre le corresponde a cada objeto

listaVehiculos= [miVehiculo, miVehiculo2, miVehiculo3]

for x in listaVehiculos:

    desplazamientoVehiculo(x) 








