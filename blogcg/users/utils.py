import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blogcg import  mail


def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn



def send_reset_email(user):
    token= user.get_reset_token()
    msg=Message('Peticion de restablecimiento de contraseña', sender='tablerosbi@centralganadera.com', recipients=[user.email])
    msg.body = f'''Para restablecer su password, visite el siguiente link:
{url_for('users.reset_token', token=token, _external=True)}
Si usted no es la persona que hizo la petición de restablecimiento por favor ignore este mail y no haga ningun tipo de cambios.
'''
    mail.send(msg)

