from funciones import *
db = Conectar_BD("localhost","jugador","jugador","monster_hunter")

opcion=MostrarMenu()
while opcion != 0:
    if opcion == 1:
        ListarMapas(db);
    elif opcion == 2:
        monstruo = input("dime el inicio del nombre del monstruo: ")
        MonstruoSubcadena(db,monstruo)
    elif opcion == 3:
        monstruo = input("dime el inicio del nombre del monstruo: ")
        ObjetoMonstruo(db,monstruo)
    elif opcion == 4:
        nuevo={}
        nuevo["idMonstruo"]=input("Identificador:")
        nuevo["nombre"]=input("Nombre:")
        nuevo["tipo"]=input("tipo (Dragon Anciano,Bestia de Colmillos,Anfibio):")
        nuevo["tamano"]=float(input("tamano:"))
        NuevoMonstruo(db,nuevo)
    elif opcion == 5:
        monstruo = input("dime el inicio del nombre del monstruo: ")
        borrarObjeto(db,monstruo)
    elif opcion == 6:
        porcentaje = float(input("dime el porcentaje"))
        AumentarValor(db,porcentaje)

    
    opcion=MostrarMenu()
Desconectar_BD(db)