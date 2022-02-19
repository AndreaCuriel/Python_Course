#la tupla va con parentesis 
mitupla=("Andrea", "Miguel", 4, 10, 1980, 4)
print(mitupla[:])
#tenemos dos metodos para convertir una tupla en lista y al contario
milista=list(mitupla)
print(milista[:])
# proceso de lista a tupla
mitupla1=tuple(milista)
print(mitupla[:])
#buscar si existe un valor en la tupla
print("Andrea" in mitupla1)
#método count, para saber cuantas veces se encuentra une elemnto
print(mitupla.count(4))
#método len para saber la lomgitud 
print(len(mitupla1))
#hacer una tupla unitaria
mitupla2=("Andrea",)
#desempacado de tupla, para asignar los elemtos por separado
mitupla3=("Andrdea", 17, 4, 1989)
nombre, dia, mes, agno=mitupla3
print(nombre)
print(dia)
print(mes)
print(agno)
#usar en index para saber la posicion de un elemento
print(mitupla.index("Miguel"))
#no se puede mdificar las tuplas, solo obtener sus valores 