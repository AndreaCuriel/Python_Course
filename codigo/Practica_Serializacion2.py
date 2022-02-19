import pickle

#para abrir el fichero y especificarle que sera leer en binario "rb"
fichero=open("lista_nombre", "rb") 

#para cargar l información
lista=pickle.load(fichero)

print(lista)