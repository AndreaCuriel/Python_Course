from io import open

archivo_texto=open("archivo.txt", "r")

#colocar el puntero a la mitad 
archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())

archivo_texto.close()

#para hacer que el archivo sea de lectura y escritura se coloca r+

archivo_texto=open("archivo.txt", "r+")

#se colocara el puntero a la mitad de la primera linea que se tiene

archivo_texto.seek(len(archivo_texto.readline())/2)

print(archivo_texto.readline())

archivo_texto.write("\ntermino de la linea ")



