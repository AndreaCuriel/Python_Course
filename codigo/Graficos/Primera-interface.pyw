#importar la libreria para la GUI
from tkinter import *
#-----------------------CREAR LA RAIZ---------------------------------------------------------------------------------------------------
#contruir la raiz, llmando la clase Tk y el método mainloop

raiz=Tk()

raiz.title("Ventana de prueba")
#raiz.resizable(1,0)  #parametros boolean (ancho, alto), para no redimencionar la ventana
#para el icono de la ventana, es necesario una imagen.ico. se puede convertir por medio de una pagina web
raiz.iconbitmap("icono.ico")
#cambiar las dimensiones de la ventana
#raiz.geometry("650x350")
#cambiar el color de background
raiz.config(bg="blue")

#-----------------CREAR EL FRAME ----------------------------------------------------------------------------------------------
miFrame=Frame()

#hay que meter el frame en la raiz (empaquetarlo)
#miFrame.pack()
#miFrame.pack(side="bottom")
#con puntos cardinales
#miFrame.pack(side="left", anchor="n")
#para expander
#miFrame.pack(fill="x")
miFrame.pack(fill="y", expand="True")
#miFrame.pack(fill="both", expand="True")
miFrame.config(bg="red")  #color

#el frame tiene un tamano fijo y se queda anclado, puedes cambiar la forma del anclado con el método para empaquetarlo
miFrame.config(width= "650", height= "350") #dimension del frame, se comento las dimensiones de la raiz, ya que cuando se tine el frame, se dimesiona con este 

#Canbiar el borde
#grosor
miFrame.config(bd=35)
#forma
miFrame.config(relief="groove")

#cambiar e cursos en el frame
miFrame.config(cursor="hand2")

#----------------------CIERRE DEL FRAME------------------------------------------------------------------------------------------





#siempre debe estar al final


raiz.mainloop()  #es un método de un bucle infinito, que permanece a la escucha




