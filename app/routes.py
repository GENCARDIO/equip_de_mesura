from flask import render_template, request, flash, redirect, send_file, session
from config import URL_HOME
from app import app
from app import utils
from app import models
import jwt
from functools import wraps


# Authentication
def requires_auth(f):
    @wraps(f)
    def decorated_function(*args):
        print(session['rol'], "AUTH")
        if session['rol'] == 'None' or session['rol'] is None or session['rol'] == '':
            url = f'{URL_HOME}logout/You dont have permissions'
            return redirect(url)
        else:
            pass
        return f(*args)
    return decorated_function


# ROUTE FLASK
@app.route("/")
def inici():
    """
    Redirecciona a la pagina principal.

    :returns: Retorna el html de la pagina principal.
    :rtype: render_template
    """
    # Redirecciona al html

    equips = models.session.query(models.Fitxes).all()
    return render_template("main.html", equips=equips)


# Ruta per seleccionar les files de les mostres
@app.route("/seleccionar_arxiu", methods=["POST", "GET"])
def seleccionar_arxiu():
    """
    Redirecciona l'html principal per afegir l'arxiu d'input.

    :returns: Retorna l'html corresponent.
    :rtype: render_template
    """

    equip = request.form['opcions']
    dades = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux == equip).first()
    return render_template("seleccionar_arxiu.html", dades=dades)


# Route to go Home
@app.route("/home", methods=["POST", "GET"])
def home():
    """
    Redirects the home page.

    :returns: Returns the corresponding html.
    :rtype: redirect
    """
    return redirect("/")


# Route for logout
@app.route("/logout")
def logout():
    """
    Redirects to logout page.

    :returns: Returns the corresponding html.
    :rtype: redirect
    """
    url = URL_HOME + 'logout'
    return redirect(url)


@app.route('/receive_token')
def receive_token():
    received_token = request.args.get('token')
    secret_key = '12345'  # Debe ser la misma clave utilizada para generar el token

    try:
        decoded_token = jwt.decode(received_token, secret_key, algorithms=['HS256'])
        session['user'] = decoded_token.get('user_tok', 'Usuario no encontrado')
        session['rols'] = decoded_token.get('rols_tok', 'Usuario no encontrado')
        session['email'] = decoded_token.get('email_tok', 'Usuario no encontrado')
        session['idClient'] = decoded_token.get('id_client_tok', 'Usuario no encontrado')
        session['rol'] = decoded_token.get('rol_tok', 'Usuario no encontrado')
        print(session['user'])
        print(session['rols'])
        print(session['email'])
        print(session['idClient'])
        print(session['rol'])
        return redirect('/')
    except Exception:
        return redirect('/logout')


@app.route('/apps')
def apps():
    tocken_cookies = {'user_tok': session['user'], 'rols_tok': session['rols'], 'email_tok': session['email'],
                      'id_client_tok': session['idClient'], 'rol_tok': 'None'}
    secret_key = '12345'
    token = jwt.encode(tocken_cookies, secret_key, algorithm='HS256')
    url = f'{URL_HOME}apps/token?token={token}'

    return redirect(url)
