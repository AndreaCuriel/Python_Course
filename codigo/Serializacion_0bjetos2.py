#cargar el fichero externo para leer los objetos 
from Serializacion_0bjetos1 import *
import pickle


fichero_apertura=open("losCoches", "rb") #leer en binario "rb"

misCoches=pickle.load(fichero_apertura)

fichero_apertura.close()

for c in misCoches:
	print(c.estado())