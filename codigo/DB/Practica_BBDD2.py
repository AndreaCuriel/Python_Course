import sqlite3
miConexion=sqlite3.connect("GestionProducto")
micursor=miConexion.cursor()
#--------------------------------------------------------------------------------------
#crear una tabla, usar triple comilla para poder escribir el query escalonado

#micursor.execute('''
    #CREATE TABLE PRODUCTOS (
    #CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    #NOMBRE_ARTICULO VARCHAR(50),
    #PRECIO INTEGER,
    #SECCION VARCHAR(20))
    #''')
#agregar datos
#productos=[
    #("AR01", "pelota", 20, "Juguetería"),
    #("AR02", "pantalón", 80, "Confección"),
    #("AR03", "destornillador", 50, "Ferreteria"),
    #("AR04", "jarrón", 30, "Ceramica")]

#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#---------------------------------------------------------------------------------------------------------
#AUTOMATIZAR AL INSERTAR REGISTROS, SIN ESPECIFICAR LA LLAVE
#CON ELLO SE AGREGAR LA SIGUIENTE INSTRUCCION EN EL QEURY DONDE SE CREA LA TABLA "AUTOINCREMENT"
#AGREGAR UNIQUE SI NO QUIERES QUE LOS CAMPOS SE REPITAN Y NO SON PRIMARY KEY

micursor.execute('''
    CREATE TABLE PRODUCTOSG (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')

#agregar datos
productos=[
    ("pelota", 20, "Juguetería"),
    ("pantalón", 80, "Confección"),
    ("destornillador", 50, "Ferreteria"),
    ("jarrón", 30, "Ceramica")]

#CON NULL SE GESTIONA QUE AHI VA LA LLAVE 
micursor.executemany("INSERT INTO PRODUCTOSG VALUES (NULL,?,?,?)", productos)

#---------------------------------------------------------------------------------
#SELECT

micursor.execute("SELECT * FROM PRODUCTOSG WHERE SECCION='Confección'")
productosLista=micursor.fetchall()
print(productosLista)

#----------------------------------------------------------------------------------
#UPDATE
micursor.execute("UPDATE PRODUCTOSG SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")



miConexion.commit()

miConexion.close()