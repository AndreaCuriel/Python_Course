#Serializacion, es el llamar o mandar objetos o colecciones a ficheros externos, siendo estos codificados en binario
#se utilizara la biblioteca pickle 

import pickle
#creamos una lista 
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

#se crea un archivo externo con escritura binaria "wb"
fichero_binario=open("lista_nombre", "wb") 

#hacer el volcado de la lista hacia el fichero binario 
pickle.dump(lista_nombres, fichero_binario)

#cerrar el fichero que se encuenta en la memoria
fichero_binario.close()

#eliminarlo 
del(fichero_binario)

#se podra encontar el archivo "lista nombres" en binario en la misma direccion de este codigo

