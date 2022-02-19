from tkinter import *
#importar la libreria para las ventanas emergentes
from tkinter import messagebox

root=Tk()


#---funcion para una ventana emergente-----------------
def infoadicional():
    messagebox.showinfo("Procesador de Andy", "Procedador de textos version 2021")

def avisoLicecia():
    messagebox.showwarning("Licencia", "Autorizada")

def salirApp():
    #el metodo askquiestion regresa un valor (yes or no) 
    valor=messagebox.askquestion("Salir", "Deseas salir de la aplicación")
    if valor=="yes":
        root.destroy()

def salirApp1():
    #se usara otro metodo que regresa true o false y sus botones son ok or cancel
    valor=messagebox.askokcancel("Salir", "Desea salir de la aplicacion")
    if valor==True:
        root.destroy()

def cerrarDocumento():
    #tambien da un valor true o false para su manipulacion
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")

  
#crear la barra menu

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#crear los elemtos del menu, tearoff en cero quitas una barra que sale en el menu al seleccionar 
menuArchivo=Menu(barraMenu, tearoff=0)
    #Subemenu
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Cerrar", command=cerrarDocumento)
#agregar un separador
menuArchivo.add_separator()
menuArchivo.add_command(label="Guardar como")
menuArchivo.add_command(label="Salir", command=salirApp)
menuArchivo.add_command(label="Salir", command=salirApp1)
menuEdicion=Menu(barraMenu)
menuHerramientas=Menu(barraMenu)
menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de...", command=infoadicional)
menuAyuda.add_command(label="Licencia", command=avisoLicecia)
#agregarlos a la barra

barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Edicion", menu=menuEdicion)
barraMenu.add_cascade(label="Herramientas", menu=menuHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)



root.mainloop()
