#entry

from tkinter import *
raiz=Tk()
miFrame=Frame(raiz, width=1200, height=700)
miFrame.pack()

#------------Variables ----------

minombre=StringVar()  #una cadena de caracteres


#-----------------Entry--------------------------------------
#asociar la variable minombre en cuadro nombre, con textvariable
cuadroNombre=Entry(miFrame, textvariable=minombre)
# dos elementos para grid, row y column
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1)
cuadroPass.config(show="*")


#-------------------Label-------------------------------------

nombreLabel=Label(miFrame, text="Nombre:")
#para alinear los elementos se usa sticky con los puntos cardinales 
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10 )

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10 )

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10 )

#-------------------Text----------------------------------------

textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=3, column=1, padx=10, pady=10)

#para hacerle un scrollbar con la clase Scrollbar, con command se asigna a que objeto texto va pemanecer y si es vertical se escribe yview

scrollvertical=Scrollbar(miFrame, command=textComentario.yview)

#es necesario colocarlo con grid, una columna mas que donde esta nuesta textComentario
#para adaptar el scroll en las dimensiones del textComentario con sticky
scrollvertical.grid(row=3, column=2, sticky="nsew")
#para que el scroll se pocisione en donde estamos modificando, en que punto nos encontramos 
textComentario.config(yscrollcommand=scrollvertical.set)

#----------------Botton-------------------------------------------
#el primer parametro es el contenedor padre, en este caso l raiz

def codigoBoton():
	minombre.set("Andrea") #asignarla a minombre el valor de Andrea

#en command se manda a llamar la funcion que difinira su comportamiento
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()








raiz.mainloop()