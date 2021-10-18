from sqlite3.dbapi2 import Cursor
from flask import Flask, jsonify
from flask import Flask
from flask import render_template as render
from flask import redirect
from formularios import Registro
import os
import sqlite3 
from sqlite3 import Error
from flask import request
from bd import ejecutar_sel, ejecutar_acc

app = Flask(__name__)
app.secret_key = os.urandom(24)


listaproductos =[
    {
        'id':'1',
        'nombre':'donut'
    },
    {
        'id':'2',
        'nombre':'donutb'
    },
    {
        'id':'2',
        'nombre':'panqueque'
    }
]
users=[
    {
        'user':'erikaside',
        'correo':'erikaside@hotmail.com',
        'nombre':'erika',
        'direccion':'calle 128 No 24-5',
        'numerocel':'3152268452',
        'tipou':'Super Administrador'
    },
    {
        'user':'camilowr',
        'correo':'camilowr@hotmail.com',
        'nombre':'camilo',
        'direccion':'calle 286 No 6-14',
        'numerocel':'3192274752',
        'tipou':'Administrador'
    },
    {
        'user':'andreapl',
        'correo':'andreapl@hotmail.com',
        'nombre':'andrea',
        'direccion':'calle 94 No 14-74',
        'numerocel':'3329665896',
        'tipou':'Usuario'
    },
    {
        'user':'yasmintg',
        'correo':'yasmintg@hotmail.com',
        'nombre':'yasmin',
        'direccion':'calle 61 No 32-14',
        'numerocel':'3164796129',
        'tipou':'Usuario'
    }
]

def sql_connection():
    try:
        con=sqlite3.connect('Michaels.db')
        return con
    except Error:
        print(Error)

def sql_insert_menu(idm, nombre, precio):
    strsql="insert into Menu (idm, nombre, precio) values('"+idm+"', '"+nombre+"', '"+precio+");"
    con=sql_connection()
    #se usa para ejecutar las sentencias sql
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

def sql_select_menu():
    strsql="select * from Menu;"
    con=sql_connection()
    #se usa para ejecutar las sentencias sql
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    Menu=cursorObj.fetchall()

def sql_edit_menu(idm, nombre, precio):
    strsql="update Menu set idm = '"+idm+"', nombre= '"+nombre+"', precio='"+precio+"' where idm="+idm+";"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_menu(id):
    strsql="delete from Menu where id="+id+";"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

@app.route('/',methods=['GET'])
def inicio():
    return render("index.html")

@app.route('/Registro',methods=['GET','POST'])
def registro():
    frm = Registro()
    return render("Registro.html", form=frm)

@app.route('/Ingreso',methods=['GET','POST'])
def ingreso():
    return render("Ingreso.html", usuarios=users)

@app.route('/Perfil',methods=['GET','POST'])
def perfil():
    return render("Perfil.html")

@app.route('/Carrito',methods=['GET','POST'])
def carrito():
    return render("Carrito.html")

@app.route('/Menu',methods=['GET'])
def productos():
    return render("Menu.html")

@app.route('/Platos',methods=['GET'])
def platos()-> str :
    """ Devolver el contenido completo de la base de datos """
    sql = "SELECT * FROM platos ORDER BY fecha, hora, nombre"
    res = ejecutar_sel(sql)
    if len(res)==0:
        mess = 'No existen platos registradas en el sistema'
        stat = 'fail'
    else:
        mess = 'Se muestran los platos registrados'
        stat = 'success'
    return render("Platos.html")
###
###@app.route('/Productos/<idmenu>',methods=['GET','POST'])
###def producto(idmenu):
###    men=listaproductos
###    for menus in men:
###        return "Este es el resultado"+menus.nombre
        #if idmenu==menus.nombre:
         #   return "Este es el producto  "+ idmenu
        #else:    
         #   return "Producto no existe"

@app.route('/Listadeseos',methods=['GET','POST'])
def deseos():
    return render("Listadeseos.html")

@app.route('/Aboutus',methods=['GET'])
def about():
    return render("Nosotros.html")

@app.route('/Editaru',methods=['GET','POST'])
def modify_user():
#si el usuario esta registrado ingresar a la pagina de lo contrario solicitar datos de ingreso
    return render("Editaru.html")

@app.route('/Editaruadmin',methods=['GET','POST'])
def modify_user_admin():
#si el usuario esta registrado ingresar a la pagina de lo contrario solicitar datos de ingreso
    return render("Editaruadmin.html")

@app.route('/Agregarmenu',methods=['GET','POST'])
def agregar_menu():
    return render("Agregarmenu.html")

@app.route('/Agregarplato',methods=['GET','POST'])
def agregar_plato():
    return render("Agregarplato.html")

if __name__ == '__main__':
    app.run(debug=True)
