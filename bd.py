from sqlite3.dbapi2 import Cursor
import sqlite3 
from sqlite3 import Error
from flask import request

NOM_BD = 'Michaels.db'

def sql_connection():
    try:
        con=sqlite3.connect('Michaels.db')
        return con
    except Error:
        print(Error)

con=sql_connection() # Conectarse a la base de datos
cur=con.cursor() # Crea un área intermedia para gestión de los contenidos

def ejecutar_acc(sql) -> int:
    """ Ejecuta consultas de accion : INSERT, DELETE, UPDATE """
    try:
        with sqlite3.connect(NOM_BD) as con:  # Conectarse a la base de datos
            cur = con.cursor()                # Crea un área intermedia para gestión de los contenidos
            res = cur.execute(sql).rowcount   # Ejecutar la consulta
            if res!=0:                        # Verificar si se realizó algún cambio
                con.commit()                  # Volver permanente el cambio
    except:
        res = 0
    return res

def ejecutar_sel(sql) -> list:
    """ Ejecuta consultas de seleccion : SELECT """
    try:
        with sqlite3.connect(NOM_BD) as con:  # Conectarse a la base de datos
            cur = con.cursor()                # Crea un área intermedia para gestión de los contenidos
            res = cur.execute(sql).fetchall() # Se obtienen los registros devueltos
    except:
        res = None
    return res

def accion(sql, datos) -> int:
    try:
        with sqlite3.connect(NOM_BD) as con:    
            cur = con.cursor()
            res = cur.execute(sql, datos).rowcount
            if res!=0:
                con.commit()
    except:
        res = 0
    return res

def sql_insert_menu(idm, nombre, precio):
    try:
        strsql="insert into Menu (idm, nombre, precio) values('"+idm+"', '"+nombre+"', '"+precio+");" #se usa para ejecutar las sentencias sql
        res=cur.execute(strsql)
        if res!=0:
            con.commit()
            con.close()
    except:
        res=0
    return res    

def sql_edit_menu(idm, nombre, precio):
    try:
        strsql="update Menu set idm = '"+idm+"', nombre= '"+nombre+"', precio='"+precio+"' where idm="+idm+";"
        res=cur.execute(strsql)
        if res!=0:
            con.commit()
            con.close()
    except:
        res=0
    return res 

def sql_delete_menu(id):
    try:
        strsql="delete from Menu where idm="+id+";"
        res=cur.execute(strsql)
        if res!=0:
            con.commit()
            con.close()
    except:
        res=0
    return res

def sql_insert_platos(idp, nombre):
    try:
        strsql="insert into platos (idp, nombre) values('"+idp+"', '"+nombre+");" #se usa para ejecutar las sentencias sql
        res=cur.execute(strsql)
        if res!=0:
            con.commit()
            con.close()
    except:
        res=0
    return res  
