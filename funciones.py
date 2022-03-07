import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()

def ListarMapas(db):
    sql="select * from Mapas"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["nombre"],"---",registro["nZonas"]," zonas")
    except:
       print("Error en la consulta")

def MonstruoSubcadena(db,monstruo):
    sql = "SELECT * FROM Monstruos WHERE nombre REGEXP '^%s'"%(monstruo)
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro["nombre"])
        return registro["nombre"]

    except:
       print("Error en la consulta")

def ObjetoMonstruo(db,monstruo):
    MonstruoSubcadena(db,monstruo)
    sql = "SELECT * FROM Objetos WHERE monstruo = (SELECT idMonstruo FROM Monstruos WHERE nombre REGEXP '^%s')"%(monstruo)
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["nombre"])
    except:
       print("Error en la consulta")

def NuevoMonstruo(db,nuevo):
    cursor = db.cursor()
    sql="insert into Monstruos values (%s, '%s', '%s', %f )" % (nuevo["idMonstruo"],nuevo["nombre"],nuevo["tipo"],nuevo["tamano"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()

def borrarObjeto(db,monstruo):
    buscar = MonstruoSubcadena(db,monstruo)
    sql="delete from Objetos where monstruo=(select idMonstruo from Monstruos where nombre = '%s')" % buscar
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        if cursor.rowcount==0:
            print("No hay objetos relacionados con ese monstruo")
    except:
        print("Error al borrar.")
        db.rollback()

def AumentarValor(db,porcentaje):
    sql = "update Objetos SET valor = valor+(valor*%f)/100"%porcentaje
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al cambiar")
        db.rollback()

def MostrarMenu():
    menu='''
    1. Lista los mapas y el total de zonas que tiene cada uno.
    2. Muestra los monstruos que empiecen por una subcadena.
    3. Pide por teclado un monstruo y muestra los objetos que suelta al morir.
    4. Inserta un nuevo monstruo en la tabla Monstruos.
    5. Borra los objetos de un monstruo indicado por teclado.
    6. aumenta el valor de los objetos un porcentaje indicado por teclado.
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")