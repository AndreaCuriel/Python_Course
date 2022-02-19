from tkinter import *
from types import TracebackType
raiz=Tk()

raiz.title("Ejemplo")

#foto=PhotoImage(file="icono.ico")
#Label(raiz, image=foto).pack()

frame=Frame(raiz)
frame.pack()

#crear las variables para los checkbuttons
playa=IntVar()
cuidad=IntVar()
selva=IntVar()

#funcion

def opcionesViaje():
    OpcionEscogida=""

    if(playa.get()==1):
        OpcionEscogida+=" Playa"
    if(cuidad.get()==1):
        OpcionEscogida+=" Cuidad"
    if(selva.get()==1):
        OpcionEscogida+=" Selva"

    textoFinal.config(text=OpcionEscogida)



#crear los checkbuttons
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Ciudad", variable=cuidad, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Selva", variable=selva, onvalue=1, offvalue=0, command=opcionesViaje).pack()

#crear el label donde se imprime la respuesta 
textoFinal=Label(frame)
textoFinal.pack()
raiz.mainloop()