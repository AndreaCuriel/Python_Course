from tkinter import *
raiz=Tk()
varOption=IntVar()

#imprimir en consola el valor
def imprimir():
    if varOption.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenio")
    
        

Label(raiz, text="Genero: ").pack()
Radiobutton(raiz, text="Masculino", variable=varOption, value=1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

etiqueta=Label(raiz)
etiqueta.pack()


raiz.mainloop()