from flask import Flask
from flask import render_template as render
from flask import redirect
from formularios import Registro
import os

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

@app.route('/Productos',methods=['GET'])
def productos():
    return render("Productos.html")

@app.route('/Productos/<idmenu>',methods=['GET','POST'])
def producto(idmenu):
    if idmenu in listaproductos:
        return "Este es el producto  "+ idmenu
    else:    
        return "Producto no existe"

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

if __name__ == '__main__':
    app.run(debug=True)