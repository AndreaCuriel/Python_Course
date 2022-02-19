from io import open

archivo_texto=open("archivo.txt", "r+")
#se lee el contenido del archivo, convirtiendo en una lista
lista_texto=archivo_texto.readlines()
#se agrega una linea mas en la posicion de la lista 1
lista_texto[1]="Esta linea ha sido incluida desde el exterior\n"
#se coloca el puntero desde el inicio para agregar la nueva linea
archivo_texto.seek(0)
#se escribe la linea 
archivo_texto.writelines(lista_texto)
archivo_texto.close()