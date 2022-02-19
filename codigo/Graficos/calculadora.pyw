from tkinter import*

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

#Variable global para guardar el tipo de operacion
operacion=""
#variable global resultado para almacenar
resultado=0

 #------------PANTALLA----------------------------------------------
#crear una instancia stringVar donde se almacenera el contenido de la calculadora 
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#---------------FUNCIONES DEL TECLADO --------------------------------
#funcion que agrega el numero 
def numeroPulsado(num):
    global operacion
    if operacion!="":  #para borrar lo que se tiene en pantalla cuando detecte que se a dado click a una operacion
        numeroPantalla.set(num)
        operacion=""
    else:
#obtiene lo que tiene la pantalla con get y le agrega el siguiente valor con set
        numeroPantalla.set(numeroPantalla.get() + num)

#---- funcuion suma
def suma(num): #num es el numero que va ver en pantalla
    global operacion
    global resultado
    resultado+=int(num) #num esta registrado como texto, se convierte con int 
    operacion="suma"
    #para que lo escriba en la pantalla
    numeroPantalla.set(resultado)

#---funcion del resultado
def el_resultado():
    global resultado
#para sumar el ultimo valor en la pantalla
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
#se resetea el resultado
    resultado=0



#------------FILA UNO------------------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#------------FILA DOS------------------------------------------------
#colocar la función "lambda" hace que este en espera y se eqjecute hasta que se pulse el boton, ya que sin el, se asigna el valor entre parentesis automanticamnete
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="X", width=3)
botonMult.grid(row=3, column=4)

#------------FILA TRES------------------------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#------------FILA CUATRO------------------------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonPunto=Button(miFrame, text=".", width=3)
botonPunto.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)



raiz.mainloop()