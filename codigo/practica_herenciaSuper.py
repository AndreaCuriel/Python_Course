class Persona():

#Constructor
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

class Empleado(Persona):

#Constructor usando SUPER para juntar los contructores
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)   #llama al método de la clase padre 
		self.salario=salario
		self.antiguedad=antiguedad

#REESCRIBIR el Metodo descripcion

	def descripcion(self):
		super().descripcion() #llama el método padre con Super
		print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)





#-----------------Instancias-----------------------------

Israel=Empleado(1500, 15, "Israel", 55, "Mexico")
Israel.descripcion()

#funcion para conocer si el objeto es una intsancia de una clase especifica
#ISINSTANCE (isintance(obejto, clase))
print("El objeto es instancia" , isinstance(Israel, Empleado))





