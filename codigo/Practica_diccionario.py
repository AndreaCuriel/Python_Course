#el diccionario tiene clave y elemnto. No peude existir dos claves iguales o mas
midiccionario={"Alemania": "Berlín", "Francea":"París"}
print(midiccionario["Francea"])
#Imprimir todo el diccionario
print(midiccionario)
#agregar mas elementos
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#como modificar
midiccionario["Italia"]="Roma"
print(midiccionario)
#como eliminar
del midiccionario["Italia"]
print(midiccionario)

midiccionario2={"Alemania": "Berlín", "Francea":"París", 23:"Jordan"}

#se puede usar una tupla para asignar las claves
mitupla=("Espana", "Francea", "Reino Unido")
midiccionario2={ mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres"}
print(midiccionario2)

#que un diccionario almacene una tupla
midiccionario3={23:"Jorda", "Nombre":"Chicago", "anillos":(1991,1992,1993,1997,1998)}
print(midiccionario3)
print(midiccionario3["anillos"])
#que un diccioanrio tenga un diccionario adentro
midiccionario4={23:"Jorda", "Nombre":"Chicago", "anillos":{"temporadas":(1991,1992,1993,1997,1998)}}
print(midiccionario4)
print(midiccionario4["anillos"])
#usar metodo keys, nos da  las claves
#usar método value, nos da los valores
print(midiccionario.keys())
print(midiccionario.values())
#dimension del diccionario
print(len(midiccionario))




