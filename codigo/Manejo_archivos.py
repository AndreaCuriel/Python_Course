#importar el modulo IO, para poder manipular los streams, archivos externos
from io import open

#crea el archivo .txt en la misma direccion que se encuentra este programa
# w significa escribir (write)
archivo_texto=open("archivo.txt", "w") 


#agregar una frase en el archivo.txt creado 
frase="Estupendo día para estudiar Python \nManejo de Archvios externos"
archivo_texto.write(frase)

#cerrar el archivo que se ha abierto en mempria desde el programa python
archivo_texto.close()

#ahora leer, para ello hay qye abrir primero el archivo, y colocar la r de lectura (read)
archivo_texto=open("archivo.txt", "r")
#leer la infoemación
texto=archivo_texto.read() #si se le coloca un numero en el método read, leera hasta llegar a esa posición. 
#es necesario mover el puntero para volver a leer desde el inicio del archivo
archivo_texto.seek(0)
#se podra leer desde el inicio del archivo
linea_texto=archivo_texto.readlines() #sera guardado en una lista, cada linea de texto
#cerrar el archivoß
archivo_texto.close()
#mostrar en la terminal lo que se leyo 
print(texto)
print(linea_texto[1])

#agregar una tercera linea de texto al archivo.txt

archivo_texto=open("archivo.txt", "a") #a de append 

#escribir
archivo_texto.write("\n nueva linea")
archivo_texto.close()















