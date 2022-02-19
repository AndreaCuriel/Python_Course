#crear la super clase o clase padre, que contendra las propiedades y comportamientos generales que comparten todos los objetos
class Vehiculos():

	#CONSTRUCTOR
	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	#Metodos de comportamiento

	def arranca(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#clase Furgoneta que HEREDA de vehiculo
class Furgoneta(Vehiculos):

#método propio para verificacion de carga en la furgoneta 
	def carga(self, cargar):
		self.cargado=cargar
		if (self.cargado):
			return "La furgoneta esta cargada"
		else:
			return ":a furgone no esta crgada"


#clase Moto que HEREDA de vehiculos
class Moto(Vehiculos):
	hcaballito=" "
	def caballito(self):
		self.hcaballito="Esta haciendo el caballito"

#SOBREESCRIBIR un método de la clase padre, para agregar otras caracteristicas. ocasionando que cuando se realice la llmada, se anule el método del padre y llame el método de la clase Moto

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

#Clase de Vehiculos electricos, que hereda a Vehiculos, para poder llamar el super y poder usar el contructor de Vehiculos junto con el de contructor de Vehiculos electricos

class VElectricos(Vehiculos):

	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonimia=100

	def cargarEnergia(self):
		self.cargando=True

#La clase Bicicleta electrica, va tener HERENCIA MULTIPLE (vehiculo y de VElectricos)
#la primera clase al escribir de izquierda a derecha tiene preferencia, se asignara su contructor, evitando tener mas de uno.
class BicicletaElectrica(VElectricos, Vehiculos):
	pass







