import pickle

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


#-------------------------------------------------------------------
#instanciar o crear los objetos

coche1=Vehiculos("Mazda", "MXS")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Renailt", "Mehane")

#lista de objetos 

coches=[coche1, coche2, coche3]

#crear fichero e ingresar la lista de objetos 

fichero=open("losCoches", "wb") # ecribir en binario wb

pickle.dump(coches, fichero)

fichero.close()
del (fichero)






