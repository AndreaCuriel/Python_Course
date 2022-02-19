import pickle
class persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad 
		print("se ha creado una persona nueva con el nombre de ", self.nombre)

#método especial que convierte en cadana de texto la infomacion del objeto
	def __str__(self):
		return "{} {} {}" .format(self.nombre, self.genero, self.edad)

#se crea la clase LstaPersonas, para pode ir reuniendo cada personas que se vaya registrando en una lista 
class ListaPersona:

	personas=[] #se crea una lista para ir almacenando los objetos en ella

#crear el contructor
	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		 #hay que desplazae el cursos al principio para que puedas leer todo lo que hay en el fichero
		listaDePersonas.seek(0)
#se mete en un try, ya que si es la primera vez, el fichero no tendra información
		try:
			self.personas=pickle.load(listaDePersonas)
			print("se cargaron {} personas del fichero externo".format(len(self.personas)))
		 
		except:
			print("El fichero esta vacio")	

		finally:
			listaDePersonas.close()
			del(listaDePersonas)



	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		#volvara (escribira el contenido de "personas"que es una lista en "listaDePersonas")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)





miLista=ListaPersona() #se crea la instancia de la lista 

p=persona("Sandra", "Femenino", 29) #se crea la instancia de la persona

#se llama el metodo de agregar Personas a la instancia mi:ista para que agregue la persona en la lista

miLista.agregarPersonas(p)

p=persona("Miguel", "Masculino", 22)

miLista.agregarPersonas(p)

#llamar el metodo para ver la lista
miLista.mostrarPersonas()



