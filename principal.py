from funciones import *
db = Conectar_BD("localhost","jugador","jugador","monster_hunter")

opcion=MostrarMenu()
while opcion != 0:
    if opcion == 1:
        ListarMapas(db);
    if opcion == 2:
        monstruo = input("dime el inicio del nombre del monstruo: ")
        MonstruoSubcadena(db,monstruo)
    if opcion == 3:
        monstruo = input("dime el inicio del nombre del monstruo: ")
        ObjetoMonstruo(db,monstruo)
    opcion=MostrarMenu()

Desconectar_BD(db)