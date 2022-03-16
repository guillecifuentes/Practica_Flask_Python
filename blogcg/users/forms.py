from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blogcg.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Nombre de Usuario',validators=[DataRequired(),Length(min=2,max=50)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirmar Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Registrarse')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nombre de usuario ya ha sido utilizado, por favor elija uno diferente')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email ya ha sido utilizado, por favor elija uno diferente')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Recuerdeme Me')
    submit=SubmitField('Ingresar')

class UpdateAccountForm(FlaskForm):
    username=StringField('Nombre de Usuario',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('Actualizar imagen de perfil',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Actualizar')

    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Este nombre de usuario ya ha sido utilizado, por favor elija uno diferente')

    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Este email ya ha sido utilizado, por favor elija uno diferente')


class RequestResetForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(),Email()])
    submit=SubmitField('Solicitar restablecimiento de contraseña')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No hay una cuenta con este email, debes registrarte primero')

class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirmar Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Restablecer contraseña')

