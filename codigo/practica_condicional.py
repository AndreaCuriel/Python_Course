edad=145

if 0<edad<100:
	print("edad es correcta")
else:
	print("Edad incorrecta")

#ejemplo diferentes con salarios

salario_presidente=int(input("Introduce salario del presidente "))
#convertir todo en un tipo sino manda error
print("Salario de presidentes es " + str(salario_presidente))

salario_director=int(input("Introduce salario del presidente "))
#convertir todo en un tipo sino manda error
print("Salario del director es " + str(salario_director))

salario_jefe_area=int(input("Introduce salario del presidente "))
#convertir todo en un tipo sino manda error
print("Salario del jefe de area es " + str(salario_jefe_area))

salario_administracion=int(input("Introduce salario del presidente "))
#convertir todo en un tipo sino manda error
print("Salario del administracion es " + str(salario_administracion))

if salario_administracion<salario_jefe_area<salario_director<salario_presidente:
	print("todo funciona correctamente")
else:
	print("hay un error")
