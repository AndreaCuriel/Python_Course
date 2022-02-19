#usando la Db sqlite
#importar la libreria
import sqlite3
from sqlite3.dbapi2 import Cursor

miConexion=sqlite3.connect("FirstDB")
#crear el cursor
miCursor=miConexion.cursor()
#------------------------------------------------------------------------------------------------
#agregar sql para crear la tabla
#miCursor.execute("CREATE TABLE PRODUCTO(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#------------------------------------------------------------------------------------------------
#insertar un valor en la tabla
#miConexion.execute("INSERT INTO PRODUCTO VALUES('BALÓN', 15, 'DEPORTES')")

#-----------------------------------------------------------------------------------------------
#crear una lista con varias tuplas con los registros que vamos a agregar en la tabla

#variosProductos=[
    #("Camiseta", 10, "Deportes"),
    #("Jarrón", 90, "Ceramica"),
    #("Camión", 20, "Jigueteria")]

#miCursor.executemany("INSERT INTO PRODUCTO VALUES(?,?,?)",variosProductos)

#------------------------------------------------------------------------------------------------
#Leer los datos de la tabla
miCursor.execute("SELECT * FROM PRODUCTO")
#obtener la informacion en una lista
variosProductos=miCursor.fetchall()
print(variosProductos)

for productos in variosProductos:
    print("Nombre del articulo: ", productos[0], " Sección: ", productos[1])


#------------------------------------------------------------------------------------------------
#Para confirmar los cmabios
miConexion.commit()
#------------------------------------------------------------------------------------------------

miConexion.close()