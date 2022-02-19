for letra in "Python":
	if letra=="h":
		continue  #si letra es igual a "h" ignorara la siguiente instrucción y regresara al for con la siguiente letra 
	print("Viendo la letra:" + letra)

#solo contar el numero de letras con los espacios
nombre="Pildoras informaticas"
contador=0
for i in nombre:
	if i==" ":
		continue # ignorar la siguiente onstrucción

	contador+=1

print(contador)
