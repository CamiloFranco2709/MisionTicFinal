from flask import Flask
from flask import render_template as render
from flask import redirect

app = Flask(__name__)
listaproductos =["donuta","donutb"]
@app.route('/',methods=['GET'])
def inicio():
    return render("index.html")

@app.route('/Registro',methods=['GET','POST'])
def registro():
    return render("Registro")

@app.route('/Ingreso',methods=['GET','POST'])
def ingreso():
    return render("Ingreso.html")

@app.route('/Perfil',methods=['GET','POST'])
def perfil():
    return render("Perfil.html")

@app.route('/Carritocompras',methods=['GET','POST'])
def carrito():
    return render("Carrito.html")

@app.route('/Productos',methods=['GET'])
def productos():
    return render("Productos.html")

@app.route('/producto/<idproducto>',methods=['GET','POST'])
def producto(idproducto):
    if idproducto in listaproductos:
        return "Este es el producto  "+ idproducto
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
    return render("Editaru.html")

@app.route('/Editaruadmin',methods=['GET','POST'])
def modify_user_admin():
    return render("Editaruadmin.html")

if __name__ == '__main__':
    app.run(debug=True)