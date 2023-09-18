from flask import render_template, request, redirect, send_file, session, flash
from config import URL_HOME
import os
from app import app
from app import utils
from app import models
from sqlalchemy import or_
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

    equips = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux.like('EIM%')).all()
    return render_template("main.html", equips=equips)


# Ruta per seleccionar les files de les mostres
@app.route("/fitxa_tecnica", methods=["POST", "GET"])
def fitxa_tecnica():
    """
    Redirecciona l'html principal per afegir l'arxiu d'input.

    :returns: Retorna l'html corresponent.
    :rtype: render_template
    """

    try:
        equip = request.form['opcions']
        dades = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux == equip).first()
        return render_template("fitxa_tecnica.html", dades=dades)

    except Exception:
        flash("L'equip seleccionat no existeix!", "warning")
        return redirect("/")


# Generar pdf
@app.route("/generar_pdf", methods=["POST"])
def generar_pdf():
    data = {}

    for key, value in request.form.items():
        data[key] = value
    if 'img_' in request.files:
        img_1 = request.files['img_1']
        img_2 = request.files['img_2']
        img_3 = request.files['img_3']
        data["img_1"] = img_1.filename
        data["img_2"] = img_2.filename
        data["img_3"] = img_3.filename
    else:
        data["img_1"] = "logo3.jpg"
        data["img_2"] = "logo3.jpg"
        data["img_3"] = "logo3.jpg"

    try:

        equip = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux == data["codi_aux"]).first()
        equip.descripcio = data["descripcio"]
        equip.fabricant = data["fabricant"]
        equip.ref_fabricant = data["ref_fabricant"]
        equip.serial_number = data["serial_number"]
        equip.model = data["model"]
        equip.emp_subministradora = data["emp_subministradora"]
        # Servei Tecnic = data["servei_tecnic"]
        # Telefon = data["telefon"]
        equip.data_alta = data["data_alta"]
        equip.condicions_equip = data["condicions_equip"]
        equip.data_baixa = data["data_baixa"]
        equip.situacio_contractual = data["situacio_contractual"]
        equip.preu = data["preu"]
        equip.tipus = data["tipus"]
        equip.amplada = data["amplada"]
        equip.alçada = data["alçada"]
        equip.profunditat = data["profunditat"]
        equip.pes = data["pes"]
        # Volum = data["volum"]
        equip.condicions_ambientals = data["condicions_ambientals"]
        equip.humitat = data["humitat"]
        equip.presa_aigua = data["presa_aigua"]
        # Marca Pantalla = data["marca_pantalla"]
        # Model Pantalla = data["model_pantalla"]
        # Num Serie Pantalla = data["num_serie_pantalla"]
        # Codi Pantalla = data["codi_pantalla"]
        equip.sai = data["marca_sai"] + " / " + data["model_sai"] + " / " + data["num_serie_sai"] + " / " + data["codi_sai"]
        # Cont Comercial = data[?]
        # Cont Tecnic = data[?]
        # Observacions = data[?]
        # Marca Lector = data["marca_lector"]
        # Model Lector = data["model_lector"]
        # Num Serie Lector = data["num_serie_lector"]
        # Codi Lector = data["codi_lector"]
        # Marca Impresora = data["marca_impresora"]
        # Model Impresora = data["model_impresora"]
        # Num Serie Impresora = data["num_serie_impresora"]
        # Codi Impresora = data["codi_impresora"]
        # Marca Tensio = data["marca_tensio"]
        # Model Tensio = data["model_tensio"]
        # Num Serie Tensio = data["num_serie_tensio"]
        # Codi Tensio = data["codi_tensio"]
        # Software 1 = data["soft_1"]
        # Versio 1 = data["versio_1"]
        # Software 2 = data["soft_2"]
        # Versio 2 = data["versio_2"]
        # Software 3 = data["soft_3"]
        # Versio 3 = data["versio_3"]
        # Personal Tecnic Udmmp = data["personal_tecnic_udmmp"]
        # Facultatius Udmmp = data["facultatius_udmmp"]
        # Ref Fungible 1 = data["ref_fung1"]
        # Descripcio Fungible 1 = data["desc_fung1"]
        # Ref Fungible 2 = data["ref_fung2"]
        # Descripcio Fungible 2 = data["desc_fung2"]
        # Document 1 = data["doc1"]
        # Document 2 = data["doc2"]
        # Contracte Manteniment = data["cont_manteniment"]
        # Manteniment Extern = data["manteniment_ext"]
        # Manteniment Internt = data["manteniment_int"]
        # Verificacio Interna = data["verificacio_int"]
        # Verificacio Externa = data["verificacio_ext"]
        # Calibratge Extern = data["cal_ext"]
        # Calibratge Intert = data["cal_int"]
        # Nom Contracte = data["nom_contracte"]
        # Empresa Responsable 1 = data["emp_respon1"]
        # Periode Cobertura 1 = data["periode_cober1"]
        # Dades Contracte 1 = data["dades_cont1"]
        # Empresa Responsable 2 = data["emp_respon2"]
        # Periode Cobertura 2 = data["periode_cober2"]
        # Dades Contracte 2 = data["dades_cont2"]
        # Empresa Responsable Preventiu Extern = data["emp_respon_prev_ext"]
        # Periodicitat Preventiu Extern = data["periodicitat_prev_ext"]
        # Contracte Preventiu Extern = data["cont_prev_ext"]
        # Manteniment Preventiu Extern = data["mant_prev_ext"]
        # Verificacio Preventiu Extern = data["verif_prev_ext"]
        # Calibratge Preventiu Extern = data["calib_prev_ext"]
        # Marges Acceptacio Preventiu Extern = data["marges_accept_prev_ext"]
        # Descripcio Preventiu Intern = data["desc_prev_int"]
        # Periodicitat Preventiu Intern = data["periodicitat_prev_int"]
        # Marges Acceptacio Preventiu Intern = data["marges_accept_prev_int"]
        # Descripcio Veriricacio Interna = data["desc_verif_int"]
        # Periodicitat Verificacio Interna = data["periodicitat_verif_int"]
        # Marges Acceptacio Verificacio Interna = data["marges_accept_verif_int"]
        # Descripcio Calibratge Intern = data["calib_desc_int"]
        # Periodicitat Calibratge Intern = data["calib_periodicitat_int"]
        # Marges Acceptacio Calibratge Intern = data["calib_marges_accept_int"]
        models.session.commit()

        # Generar PDF
        utils.create_docx(data)

        return send_file("docx/" + data['codi_aux'] + ".docx")

    except Exception:
        flash("No s'ha creat el pdf, error intern!", "warning")
        return redirect("/")


# Afegir equip
@app.route("/form_afegir_equip")
def form_afegir_equip():
    """
    Redirecciona a la pagina principal.

    :returns: Retorna el html de la pagina principal.
    :rtype: render_template
    """
    # Redirecciona al html
    return render_template("afegir_equip.html")


# Afegir equip
@app.route("/afegir_equip", methods=["POST"])
def afegir_equip():
    """
    Redirecciona a la pagina principal.

    :returns: Retorna el html de la pagina principal.
    :rtype: render_template
    """

    info = {}
    dades = request.form.items()
    for key, value in dades:
        info[key] = value

    if info["codi_aux"] == "":
        flash("Error, el codi_aux es obligatori!", "warning")
        return redirect("/form_afegir_equip")

    equip = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux == info["codi_aux"]).first()
    if equip is not None:
        flash("Error, el codi_aux no pot esta repetit!", "warning")
        return redirect("/form_afegir_equip")

    try:
        insert = models.Fitxes(
            codi_aux=info["codi_aux"],
            codi_cgc=info["codi_cgc"],
            descripcio=info["descripcio"],
            fabricant=info["fabricant"],
            ref_fabricant=info["ref_fabricant"],
            serial_number=info["serial_number"],
            model=info["model"],
            emp_subministradora=info["emp_subministradora"],
            data_alta=info["data_alta"],
            condicions_equip=info["condicions_equip"],
            data_baixa=info["data_baixa"],
            situacio_contractual=info["situacio_contractual"],
            preu=info["preu"],
            tipus=info["tipus"],
            amplada=info["amplada"],
            alçada=info["alçada"],
            profunditat=info["profunditat"],
            pes=info["pes"],
            condicions_ambientals=info["condicions_ambientals"],
            humitat=info["humitat"],
            presa_aigua=info["presa_aigua"],
            sai=info["sai"],
            cont_comercial=info["contacte_comercial"],
            cont_tecnic=info["contacte_tecnic"],
            observacions=info["observacions"]
        )
        models.session.add(insert)
        models.session.commit()
        flash("Afegit correctament", "success")
        return redirect("/")
    except Exception:
        flash("Error al afegir", "warning")
        return redirect("/form_afegir_equip")


@app.route('/guardar_imagen', methods=['POST'])
def guardar_imagen():
    if 'img_' not in request.files:
        pass
        # return jsonify({'success': False, 'message': 'No se proporcionó ninguna imagen'}), 400

    imagen = request.files['imagen']

    if imagen.filename == '':
        pass
        # return jsonify({'success': False, 'message': 'No se seleccionó ningún archivo'}), 400

    if imagen:
        filename = os.path.join("app/static", imagen.filename)
        imagen.save(filename)
        # return jsonify({'success': True, 'message': 'Imagen guardada exitosamente', 'imageUrl': filename}), 200

    return "ok"
    # return jsonify({'success': False, 'message': 'Error al guardar la imagen'}), 500


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
