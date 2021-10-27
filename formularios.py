from re import T
from typing import Text
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField, SelectField
from wtforms import validators
from wtforms.fields.core import FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired
from wtforms.fields.html5 import EmailField

class Registro(FlaskForm):
    usu = TextField('Usuario', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    nom = TextField('Nombre', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    ema = EmailField('E-mail', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='E-mail es requerido')])
    pas = PasswordField('Password', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='Password es requerido')])
    dire = TextField('Dirección', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='La dirección es requerida')])
    tel = TextField('Telefono', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El telefóno es requerido')])
    tipoU = SelectField('Tipo Usuario',choices=('Final','Administrador', 'Super Administrador'),validate_choice=True)
    #tipoU = TextField('Tipo U', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El tipo de Usuario es requerido')])
    regbtn = SubmitField('Registrarse')
   
class Login(FlaskForm):
    ema = EmailField('E-mail', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='E-mail es requerido')])
    pwd = PasswordField('Password', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    logbtn = SubmitField('Iniciar Sesión')

class platos(FlaskForm):
    idp = IntegerField('Identificacion', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    busbtn = SubmitField('Buscar')
    nom = TextField('Nombre', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    agrbtn = SubmitField('Agregar')
    edibtn = SubmitField('Editar')
    elibtn = SubmitField('Eliminar')
    verbtn = SubmitField('Ver Todos')

class menu(FlaskForm):
    nom=TextField('Nombre', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    busbtn = SubmitField('Buscar')
    des=TextField('Descripcion', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    pre=FloatField('Precio', validators=[Length(min=4,max=7,message='Precio no corresponde'),InputRequired(message='El nombre es requerido')])
    agrbtn = SubmitField('Agregar')
    edibtn = SubmitField('Editar')
    elibtn = SubmitField('Eliminar')
    verbtn = SubmitField('Ver Todos')

class edituadmin(FlaskForm):
    usu = TextField('Usuario', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    busbtn = SubmitField('Buscar')
    nom = TextField('Nombre', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    ema = EmailField('E-mail', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='E-mail es requerido')])
    pas = PasswordField('Password', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='Password es requerido')])
    dire = TextField('Dirección', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='La dirección es requerida')])
    tel = TextField('Telefono', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El telefóno es requerido')])
    tipoU = SelectField('Tipo Usuario',choices=('Final','Administrador', 'Super Administrador'),validate_choice=True)
    #tipoU = TextField('Tipo U', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El tipo de Usuario es requerido')])
    agrbtn = SubmitField('Agregar')
    edibtn = SubmitField('Editar')
    elibtn = SubmitField('Eliminar')
    verbtn = SubmitField('Ver Todos')

class editu(FlaskForm):
    usu = TextField('Usuario', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    nom = TextField('Nombre', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    ema = EmailField('E-mail', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='E-mail es requerido')])
    pas = PasswordField('Password', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='Password es requerido')])
    dire = TextField('Dirección', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='La dirección es requerida')])
    tel = TextField('Telefono', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El telefóno es requerido')])
    tipoU = SelectField('Tipo Usuario',choices=('Final','Administrador', 'Super Administrador'),validate_choice=True)
    #tipoU = TextField('Tipo U', validators=[Length(min=2, max=100,message='Longitud fuera de rango'),InputRequired(message='El tipo de Usuario es requerido')])
    agrbtn = SubmitField('Agregar')
    edibtn = SubmitField('Editar')
    elibtn = SubmitField('Eliminar')
    verbtn = SubmitField('Ver Todos')