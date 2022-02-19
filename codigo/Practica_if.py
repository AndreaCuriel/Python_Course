def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="reprobado"
	return valoracion


print("programa de evaluación de alumnos")
nota_alumno=int(input("Introduce la calificación"))

print(evaluacion(nota_alumno)) #se debe transformal el dato ontroducido en input a int. todo lo que entre en input es un string

if nota_alumno<5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")

	









