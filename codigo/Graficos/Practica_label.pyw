from tkinter import *

#raiz
root=Tk()
#frame
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

#miLabel=Label(miFrame, text="Hola Alumnos de Python")
#miLabel.pack() #adapata el contenedor con el tamano del texto, por dicha razon mejor usamos .place
#miLabel.place(x=200, y=200)

#Abreviar lo de arriba sino se va utilizar otro label
#(color, tipo de letra y tamano)
Label(miFrame, text="Hola Alumnos de Python", fg="red", font=("Comic Sans MS", 18) ).place(x=200, y=200)

#como usar imagenes
#miImagen=PhotoImage(file="mouse.gif")
#Label(miFrame, image=miImagen).place(x=200, y=200)


root.mainloop()

