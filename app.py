from sqlite3.dbapi2 import Cursor
from flask import Flask, jsonify
from flask import Flask, redirect
from flask import render_template as render
from flask import redirect
from flask.templating import render_template
from wtforms import form
from formularios import Registro, Login
import os
import sqlite3 
from sqlite3 import Error
from flask import request
from bd import ejecutar_sel, ejecutar_acc, accion
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash, request, session
from functools import wraps


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.errorhandler(404)
def e404(e):
    return render_template("index.html"), 404

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("usu") is None:
            return redirect("/Ingreso")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/home/')
@app.route('/index/')
@app.route('/')
def inicio():
    return render("index.html")

@app.route('/Registro/',methods=['GET','POST'])
def registro():
    frm = Registro()
    if request.method == 'GET':
        return render("Registro.html", form=frm, titulo='Registro de datos')
    else:
        usu = escape(request.form['usu'])
        nom = escape(request.form['nom'])
        ema = escape(request.form['ema'])
        pas = escape(request.form['pas'])
        dire = escape(request.form['dire'])
        tel = escape(request.form['tel'])
        tipoU = frm.tipoU.data

        swerror = False
        if usu==None or len(usu)==0:
            flash('ERROR: Debe suministrar un nombre de usuario')
            swerror = True
        if nom==None or len(nom)==0:
            flash('ERROR: Debe suministrar un nombre')
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
        if tipoU==None:
            flash('ERROR: Debe suministrar un Tipo de Usuario')
            swerror = True        
        if not swerror:      
            sql = 'INSERT INTO usuarios(usuario, nombre, correo, password, direccion, telefono, tipousuario) VALUES(?, ?, ?, ?, ?, ?, ?)'
            pwd = generate_password_hash(pas)     
            res = accion(sql, (usu, nom, ema, pwd, dire, tel, tipoU))
            if res==0:
                flash('ERROR: No se pudieron almacenar los datos, reintente')
            else:
                flash('INFO: Los datos fueron almacenados satisfactoriamente')
            if frm.validate_on_submit():
                return redirect('/Registro')                
        return render('Registro.html', form=frm, titulo='Registro de datos')

@app.route('/Editaruadmin/',methods=['GET','POST'])
def modify_user_admin():
    if request.method=='POST':
        usuario = request.form['usuariotxt'].strip()
        if "buscar" in request.form:
            sql = f"SELECT usuario, nombre, correo, direccion, telefono, tipousuario FROM usuarios WHERE usuario='{usuario}'"
            resultado = ejecutar_sel(sql)
            # Procesar los resultados
            if len(resultado)==0:
                flash('ERROR: Usuario no existe en la base de datos, por favor registrarse')
                return render_template('Editaruadmin.html')              
            else:
                usuario = resultado[0][0]
                nombre = resultado[0][1]
                correo = resultado[0][2]
                direccion = resultado[0][3]
                telefono = resultado[0][4]               
                tipousuario = resultado[0][5]
                print(nombre, correo, direccion, telefono, tipousuario)
                flash('Usuario:{} Nombre: {} E-mail: {} Dirección: {} Numero de celular: {} Tipo de Usuario: {}'.format(usuario, nombre,correo,direccion,telefono,tipousuario))                
                return render_template('Editaruadmin.html')
        elif "editar" in request.form:
            nom = request.form['nombretxt'].strip()
            cor = request.form['emailtxt'].strip()
            pwd = generate_password_hash(request.form['password'])
            dire = request.form['direcciontxt'].strip()
            tele = request.form['numerocel'].strip()
            tipou = request.form['TipoU']
            sql = f"UPDATE usuarios SET nombre, correo, password, direccion, telefono, tipousuario VALUES (?, ?, ?, ?, ?, ?) WHERE usuario='{usuario}'"
            res = accion(sql, (nom, cor, pwd, dire, tele, tipou))
            if res==0:
                print(nom, cor, pwd, dire, tele, tipou)
                flash('ERROR: No se pudieron almacenar los datos, reintente')
                return render_template('Editaruadmin.html')     
            else:
                flash('INFO: Los datos fueron actualizados satisfactoriamente')
                return render_template('Editaruadmin.html')
    else:        
        return render_template("Editaruadmin.html")

@app.route('/Ingreso/',methods=['GET','POST'])
def ingreso():
    frm = Login()
    if request.method=='GET':
        return render_template('Ingreso.html', form=frm, titulo='Control de acceso')
    # 1. Recuperar los datos del formulario y le aplico transformaciones
    else:
        email = escape(frm.ema.data.strip())
        pwd = escape(frm.pwd.data.strip())
        # Preparar la consulta 
        sql = f"SELECT id, usuario, nombre, password, direccion, telefono, tipousuario FROM usuarios WHERE correo='{email}'"
        # Ejecutar la consulta
        res = ejecutar_sel(sql)
        # Procesar los resultados
        if len(res)==0:
            flash('ERROR: Usuario o contraseña inválidos')
            return render_template('Ingreso.html', form=frm, titulo='Iniciar Sesión')
        else:
            # Recupero la clave almacenada en la base de datos - cifrada
            cbd = res[0][3]
            # Comparo contra la clave suminstrada por el usuario
            if check_password_hash(cbd,pwd):
                # Se guardarán los datos del usuario en una variable de sesion
                session.clear()
                session['id'] = res[0][0]
                session['usu'] = res[0][1]
                session['nom'] = res[0][2]
                session['cla'] = pwd
                session['dir'] = res[0][4]
                session['tel'] = res[0][5]
                session['tipoU'] = res[0][6]
                session['usr'] = email
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
    sql = "SELECT * FROM menu ORDER BY idm,nombre"
    res = ejecutar_sel(sql)
    return render("Platos.html",resultado=res)

@app.route('/Listadeseos',methods=['GET','POST'])
@login_required
def deseos():
    return render("Listadeseos.html")

@app.route('/Aboutus',methods=['GET'])
def about():
    return render("Nosotros.html")

@app.route('/Editaru',methods=['GET','POST'])
def modify_user():
    return render("Editaru.html")

@app.route('/Agregarmenu',methods=['GET','POST'])
def agregar_menu():
    return render("Agregarmenu.html")        

@app.route('/Agregarplato',methods=['GET','POST'])
def agregar_plato():
    frm = platos()
    if request.method == 'GET':
        return render("Agregarplato.html", form=frm, titulo='Agregar Plato')
    else:
        nom = escape(request.form['nom'])
        des = escape(request.form['des'])

        swerror = False
        if nom==None or len(nom)==0:
            flash('ERROR: Debe suministrar un nombre')
            swerror = True
        if des==None or len(des)==0:
            flash('ERROR: Debe suministrar un e-mail válido ')
            swerror = True
        if not swerror:      
            sql = 'INSERT INTO usuarios(nombre, descripcion) VALUES(?, ?)'
            res = accion(sql, (nom, des))
            if res==0:
                flash('ERROR: No se pudieron almacenar los datos, reintente')
            else:
                flash('INFO: Los datos fueron almacenados satisfactoriamente')
            if frm.validate_on_submit('agrbtn'):
                return redirect('/Agregarplato')                
        return render('Agregarplato.html', form=frm, titulo='Registro de datos')
    

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, port=443, ssl_context=('c20211021.pem','l20211021.pem')) PARA HTTPS
