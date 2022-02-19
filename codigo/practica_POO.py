class Coche():

    #propiedades de estado incial con un CONSTRUCTOR
    
    def __init__(self):  #el contructor siempre se llama __int__
    #Se van ENCAPSULAR con dos guines bajos al inicio "__"las propiedades para protejerlas y no puedan ser modificadas fuera de la clase
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    #comportamiento con Método

    def arrancar(self,arrancamos): #self se refiere al objeto (es this en java), en python es obligatorio poner self, en java se entiende sin tener que escribir this 
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Problemas en el chequeo"
        else:
            return "El coche esta detenido"


    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedad. Un ancho de ", self.__anchoChasis, " y un largo de ",
        self.__largoChasis)

    
#METODO ENCAPSULADO "__", no puede ser modificado fuera de su clase
#sera llamado en el método arrancar.
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False 

    

        

miCoche=Coche()  #intanciar una clase, crear objeto o ejemplarizar la clase

print(miCoche.arrancar(True))
miCoche.estado()

print("----------A continuacion creamos el segundo objeto-------------")

miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()