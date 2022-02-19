#listas o arrays
milista=["Maria", "Pepe", "Marta", "Israel", 6, True]
print(milista[:])
print(milista[2])
print(milista[0:3])
#Agregar al final de la lista
milista.append("Susana")
#agregar al otro elemento en la lista con poscion exacta
milista.insert(2,"Carlos")
print(milista[:])
#agregar varios elementos
milista.extend(["Andrea", "Sandra", "Luis"])
print(milista[:])
#devolver el indice de posicion de une lemento en la lista
print(milista.index("Israel"))
#para saber si hay un elemento en la lista
print("Israel" in milista)
#eliminar elementos
milista.remove("Pepe")
print(milista[:])
#eliminar el ultimo elemento
milista.pop()
print(milista[:])

milista2=["Lucia", "Karla"]
milista3=milista+milista2
print(milista3[:])

#para repetir listas
milista4=[5,4,3]*3
print(milista4[:])
milista4=milista4[:]*3
print(milista4[:])











