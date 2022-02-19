#para entrar al else, el bucle anterior tiene que concluir, si este se rompe por un break, el else no se leera.
email=input("Introduce tu email:")
for i in email:
	if i=="@":
		arroba=True
		break; #rompe el for 

#el else no pertenece al bucle 
else: #funciona cuando el bucle de arriba haya recorrido todo (for), si el break se lee, nunca se leera else, ya que no se conluyo el bucle for.
	arroba=False

print(arroba)


