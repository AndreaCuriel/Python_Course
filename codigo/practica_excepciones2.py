def divide():

	try:
		op1=float(input("Introduce el primer numero: "))
		op2=float(input("Introduce el primer numero: "))
		print("La división es:" + str(op1/op2))

#excepciones de manera consecutiva
	except ValueError:
		print("el valor introducido es incorrecto")
	except ZeroDivisionError:
		print("No se puede dividir entre 0")

# excepcion general, no es recomendable
	#except:
		#print("error")
#cundo quieres que algo siempre se ejecute, se usa finally
	finally:
		print("Calculo Finalizado")

divide()

