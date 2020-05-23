#-----------------------------------------------------------------------------------------------------------
#--------------Elaborado por José Francisco Armas Sosa---------------------
#--------------Carnet 1990 00 2168 ---------------------
#--------------Universidad Mariano Galvez---------------------
#--------------Programacion 1 seccion "A"---------------------
#--------------Modulo de inventarios---------------------
#--------------Este modulo no contempla la actualizacion del campo cantidad para evitar que se hagan operaciones turbias ---------------------
#-----------------------------------------------------------------------------------------------------------

import sqlite3
import os
import pprint
#-----------------------------------------------------------------------------------------------------------
#--------------insertar registros  ---------------------
#-----------------------------------------------------------------------------------------------------------

def pr_inserta_datos():
    miConexion=sqlite3.connect("Vehiculos")

    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()

    #miCursor.execute("CREATE TABLE INVENTARIO (cod_vehiculo integer PRIMARY KEY AUTOINCREMENT, marca varchar, modelo varchar, anio number(4), descripcion varchar(255), Cantidad number, precio_compra number, precio_venta number)")

    #Codigo 
    #Marca
    #Modelo
    #Año
    #Descripción
    #Cantidad
    #Precio Compra
    #Precio Venta

    #v_cod_vehiculo = int(input(f"Ingrese codigo vehiculo: "))
    v_marca = (input(f"Ingrese marca vehiculo: "))
    v_modelo = (input(f"Ingrese modelo vehiculo: "))
    v_anio = int(input(f"Ingrese anio vehiculo: "))
    v_descripcion = (input(f"Ingrese descripcion vehiculo: "))
    v_cantidad = int(input(f"Ingrese cantidad vehiculo: "))
    v_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))
    v_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))


    #cadena =(f"""insert into INVENTARIO Values({v_cod_vehiculo},
    #'{v_marca}',
    #'{v_modelo}',
    # {v_anio},
    #'{v_descripcion}',
    # {v_cantidad},
    # {v_precio_compra}, 
    # {v_precio_venta} )""")

    #print(cadena)

    miCursor.execute(f"""insert into INVENTARIO Values(NULL,
    '{v_marca}',
    '{v_modelo}',
    {v_anio},
    '{v_descripcion}',
    {v_cantidad},
    {v_precio_compra}, 
    {v_precio_venta} )""")

    miConexion.commit()
    print("Datos guardados exitosamente! \n")
    miConexion.close()

#-----------------------------------------------------------------------------------------------------------
#-------------- Listar Registros ---------------------
#-----------------------------------------------------------------------------------------------------------
def pr_listar():
    print("Lista de Existencias de Vehiculos")
    miConexion=sqlite3.connect("Vehiculos")
    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()

    miCursor.execute("Select * from INVENTARIO")
    
    listado_inventario=miCursor.fetchall()
    #pprint.pprint(listado_inventario)
    print( "Codigo, Marca, Modelo, Año, Descripción, Cantidad, Precio Compra, Precio Venta")
    for ls_vehiculos in listado_inventario:
        print(ls_vehiculos)
    #    pprint.pprint(ls_vehiculos)
    print("Fin del listado" + '\n')
    v_continuar = input("presione ENTER para continuar... ")
    v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

    miConexion.commit()
    miConexion.close()
#-----------------------------------------------------------------------------------------------------------
#-------------- Actualizar Registros ---------------------
#-----------------------------------------------------------------------------------------------------------
def pr_actualiza():
    pr_listar()
    miConexion=sqlite3.connect("Vehiculos")
    # para crear tabla se crea cursor
    miCursor=miConexion.cursor()
    v_cod_vehiculo = int(input("Ingrese el codigo del vehiculo que desea modificar o '0' para salir: "))
    if v_cod_vehiculo != 0:
        v_marca = (input(f"Ingrese marca vehiculo: "))
        v_modelo = (input(f"Ingrese modelo vehiculo: "))
        v_anio = int(input(f"Ingrese anio vehiculo: "))
        v_descripcion = (input(f"Ingrese descripcion vehiculo: "))
        v_cantidad = int(input(f"Ingrese cantidad vehiculo: "))
        v_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))
        v_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))
        miCursor.execute(f"""UPDATE INVENTARIO SET
            marca = '{v_marca}',
            modelo = '{v_modelo}',
            anio ={v_anio},
            descripcion = '{v_descripcion}',
            Cantidad = {v_cantidad},
            precio_compra = {v_precio_compra}, 
            precio_venta = {v_precio_venta} where cod_vehiculo = {v_cod_vehiculo}""")
    miConexion.commit()
    print("Datos guardados exitosamente! \n")
    miConexion.close()
#-----------------------------------------------------------------------------------------------------------
#-------------- Busca Registros ---------------------
#-----------------------------------------------------------------------------------------------------------
def pr_busqueda():
    print("Lista de Existencias de Vehiculos")
    print("Criterios de busqueda: ")
    print("1. Codigo de Vehiculo")
    print("2. Marca de Vehiculo")
    print("3. Modelo de Vehiculo")
    print("4. Año de Vehiculo")
    print("5. Descripcion de Vehiculo")
    print("6. Precio de Compra de Vehiculo")
    print("7. Precio de Venta")
     
    v_criterio=int(input("Ingrese el numero del campo para el criterio de busqueda: "))
    v_valor_busqueda=""
    v_valor_busqueda=(input(f"Ingrese el valor de busqueda: "))
    if v_criterio == 1:
        v_where = (f"cod_vehiculo = {v_valor_busqueda} ")
    elif v_criterio == 2:
        v_where = (f"marca like '%{v_valor_busqueda}%'")
    elif v_criterio == 3:
        v_where = (f"Modelo like '%{v_valor_busqueda}%'")
    elif v_criterio == 4:
        v_where = (f"Año = {v_valor_busqueda} ")
    elif v_criterio == 5:
        v_where = (f"Descripcion = '%{v_valor_busqueda}%'")
    elif v_criterio == 6:
        v_where = (f"precio_compra = {v_valor_busqueda} ")
    elif v_criterio == 4:
        v_where = (f"precio_venta = {v_valor_busqueda} ")
    
    
    miConexion=sqlite3.connect("Vehiculos")
    
    miCursor=miConexion.cursor()

    miCursor.execute(f"Select * from INVENTARIO WHERE {v_where} " )
    
    listado_inventario=miCursor.fetchall()
    #pprint.pprint(listado_inventario)
    print( "Codigo, Marca, Modelo, Año, Descripción, Cantidad, Precio Compra, Precio Venta")
    for ls_vehiculos in listado_inventario:
        print(ls_vehiculos)
    #    pprint.pprint(ls_vehiculos)
    print("Fin del listado" + '\n')
    miConexion.commit()
    miConexion.close()
    v_continuar = input("presione ENTER para continuar... ")
    v_continuar = v_continuar+"null" # solo lo puse para que no marque feo vscode



#-----------------------------------------------------------------------------------------------------------
#--------------Menu principal ---------------------
#-----------------------------------------------------------------------------------------------------------
v_opcion=0
while True:
	#os.system("cls")

	print("Menu principal Modulo de Inventarios:" + '\n' )
	print("1. Ingreso de datos al modulo" + '\n' )
	print("2. Modificacion de registros" + '\n' )
	print("3. Reporte de existencias" + '\n' )
	print("4. Busquedas de existencias" + '\n' )
	print("5. Salir" + '\n' )
    
	while True:
		try:
			v_opcion = int(input("ingrese opcion: "))
			break
		except ValueError:
			print("Error de ingreso pruebe nuevamente")

	if v_opcion == 5:
		break
	#print("el valor es" + v_opcion)


	if v_opcion == 1:
		pr_inserta_datos()
	elif v_opcion == 2:
            pr_actualiza()
	elif v_opcion == 3:
		pr_listar()
	elif v_opcion == 4:
		pr_busqueda()


