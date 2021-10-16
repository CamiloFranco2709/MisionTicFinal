from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired
from wtforms.fields.html5 import EmailField

class Registro(FlaskForm):
    nom = TextField('Nombre', validators=[Length(min=5, max=20,message='Longitud fuera de rango'),InputRequired(message='El nombre es requerido')])
    usu = TextField('Usuario', validators=[Length(min=5, max=40,message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    ema = EmailField('E-mail', validators=[Length(min=10, max=20,message='Longitud fuera de rango'),InputRequired(message='E-mail es requerido')])
    dire = TextField('Dirección', validators=[Length(min=5, max=40,message='Longitud fuera de rango'),InputRequired(message='La dirección es requerida')])
    tel = TextField('Telefono', validators=[Length(min=7, max=40,message='Longitud fuera de rango'),InputRequired(message='El telefóno es requerido')])
    tipoU = TextField('Tipo U', validators=[Length(min=7, max=40,message='Longitud fuera de rango'),InputRequired(message='El tipo de Usuario es requerido')])
    regbtn = SubmitField('Registrarse')

class Login(FlaskForm):
    usr = TextField('Usuario *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    email = EmailField('Email *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),DataRequired(message='Email es requerido')])
    btn = SubmitField('Ingresar')

