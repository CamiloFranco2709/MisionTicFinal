from sqlite3.dbapi2 import Cursor
from flask import Flask, jsonify
from flask import Flask, redirect
from flask import render_template as render
from flask import redirect
from flask.templating import render_template
from formularios import Registro, Login
import os
import sqlite3 
from sqlite3 import Error
from flask import request
from bd import ejecutar_sel, ejecutar_acc, accion
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/',methods=['GET'])
def inicio():
    return render("index.html")

@app.route('/Registro/',methods=['GET','POST'])
def registro():
    frm = Registro()
    if request.method == 'GET':
        return render("Registro.html", form=frm, titulo='Registro de datos')
    else:
        nom = escape(request.form['nom'])
        ema = escape(request.form['ema'])
        pas = escape(request.form['pas'])
        dire = escape(request.form['dire'])
        tel = escape(request.form['tel'])
        tipoU = escape(request.form['tipoU'])

        swerror = False
        if nom==None or len(nom)==0:
            flash('ERROR: Debe suministrar un nombre de usuario')
            swerror = True
        if ema==None or len(ema)==0:
            flash('ERROR: Debe suministrar un e-mail válido ')
            swerror = True
        if pas==None or len(pas)==0:
            flash('ERROR: Debe suministrar un password válido')
            swerror = True
        if dire==None or len(dire)==0:
            flash('ERROR: Debe suministrar una dirección válida')
            swerror = True
        if tel==None or len(tel)==0:
            flash('ERROR: Debe suministrar un telefono válido')
            swerror = True
        if tipoU==None or len(tipoU)==0:
            flash('ERROR: Debe suministrar un Tipo de Usuario')
            swerror = True        
        if not swerror:      
            sql = 'INSERT INTO usuarios(nombre, correo, password, direccion, telefono, tipousuario) VALUES(?, ?, ?, ?, ?, ?)'
            pwd = generate_password_hash(pas)     
            res = accion(sql, (nom, ema, pwd, dire, tel, tipoU))
            if res==0:
                flash('ERROR: No se pudieron almacenar los datos, reintente')
            else:
                flash('INFO: Los datos fueron almacenados satisfactoriamente')
        return render('Registro.html', form=frm, titulo='Registro de datos')


@app.route('/Ingreso',methods=['GET','POST'])
def ingreso():
    frm = Login()
    if request.method=='GET':
        return render_template('Ingreso.html', form=frm, titulo='Control de acceso')
    # 1. Recuperar los datos del formulario y le aplico transformaciones
    else:
        usu = escape(frm.usu.data.strip())
        pwd = escape(frm.pwd.data.strip())
        # Preparar la consulta 
        sql = f"SELECT id, nombre, password, direccion, telefono, tipousuario FROM usuarios WHERE correo='{usu}'"
        # Ejecutar la consulta
        res = ejecutar_sel(sql)
        # Procesar los resultados
        if len(res)==0:
            flash('ERROR: Usuario o contraseña inválidos')
            return render_template('Ingreso.html', form=frm, titulo='Iniciar Sesión')
        else:
            # Recupero la clave almacenada en la base de datos - cifrada
            cbd = res[0][2]
            # Comparo contra la clave suminstrada por el usuario
            if check_password_hash(cbd,pwd):
                # Se guardarán los datos del usuario en una variable de sesion
                session.clear()
                session['id'] = res[0][0]
                session['nom'] = res[0][1]
                session['cla'] = pwd
                session['dir'] = res[0][3]
                session['tel'] = res[0][4]
                session['tipoU'] = res[0][5]
                session['usr'] = usu
                if session['tipoU'] == 'Super Administrador':
                    return render_template('PerfilSuperA.html')
                elif session['tipoU'] == 'Administrador':
                    return render_template('PerfilAdmin.html')
                else:
                    return redirect('/')
            else:
                flash('ERROR: Usuario o contraseña inválidos')
                return render_template('Ingreso.html', form=frm, titulo='Iniciar Sesión')

@app.route('/salir/', methods=['GET','POST'])
def salir():
    session.clear()
    return render_template("index.html")            
            
@app.route('/Perfil',methods=['GET','POST'])
def perfil():
    return render("Perfil.html")

@app.route('/Carrito',methods=['GET','POST'])
def carrito():
    return render("Carrito.html")

@app.route('/Menu',methods=['GET'])
def productos()-> str :
    """ Devolver el contenido completo de la base de datos """
    sql = "SELECT * FROM menu ORDER BY idm,nombre"
    res = ejecutar_sel(sql)
    print(res)
    return render("Menu.html",resultado=res)
    """
    if len(res)==0:
        mess = 'No existen platos registradas en el sistema'
        stat = 'fail'
    else:
        mess = 'Se muestran los platos registrados'
        stat = 'success'
    return jsonify({'resultado':stat,'mensaje':mess,'datos':res})
    """
@app.route('/Platos',methods=['GET'])
def platos()-> str :
    """ Devolver el contenido completo de la base de datos """
    sql = "SELECT * FROM platos ORDER BY nombre,id"
    res = ejecutar_sel(sql)
    if len(res)==0:
        mess = 'No existen platos registradas en el sistema'
        stat = 'fail'
    else:
        mess = 'Se muestran los platos registrados'
        stat = 'success'
    return jsonify({'resultado':stat,'mensaje':mess,'datos':res}) 

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
