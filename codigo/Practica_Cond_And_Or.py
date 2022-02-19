print("Programa de becas")
distancia_escuela=int(input("Introduce la distancia a la escuela KM "))
print(distancia_escuela)

numero_de_hermanos=int(input("Introduce el numero de hermanos"))
print(numero_de_hermanos)

salario_familiar=int(input("Introduce salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_de_hermanos>2 or  salario_familiar<=2000:
	print("Aprobada")
else:
	print("Denegada")
