from re import T
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField, SelectField
from wtforms.fields.core import SelectField
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


