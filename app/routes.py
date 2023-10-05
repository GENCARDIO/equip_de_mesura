from flask import render_template, request, redirect, send_file, session, flash
from config import URL_HOME
import os
from app import app
from app import utils
from app import models
# from sqlalchemy import or_
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
@app.route("/fitxa_tecnica", methods=["POST"])
def fitxa_tecnica():
    """
    Redirecciona l'html principal per afegir l'arxiu d'input.

    :returns: Retorna l'html corresponent.
    :rtype: render_template
    """

    try:
        equip = request.form['codi_aux']
        print(equip)
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
        # print(key, value)

    uploaded_files = request.form.getlist("imagenes[]")
    for i, file in enumerate(uploaded_files):
        data["desc_img_" + str(i)] = file

    # print(data)
    # return "ok"

    if data["img_1"] == '':
        data["img_1"] = "no_foto.png"
    if data["img_2"] == '':
        data["img_2"] = "no_foto.png"
    if data["img_3"] == '':
        data["img_3"] = "no_foto.png"

    # try:

    equip = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux == data["codi_aux"]).first()
    data["data_modificacio"] = equip.data_modificacio
    data["versio_doc"] = equip.versio_doc
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
    equip.volum = data["volum"]
    equip.condicions_ambientals = data["condicions_ambientals"]
    equip.humitat = data["humitat"]
    equip.presa_aigua = data["presa_aigua"]
    equip.marca_pantalla = data["marca_pantalla"]
    equip.model_pantalla = data["model_pantalla"]
    equip.num_serie_pantalla = data["num_serie_pantalla"]
    equip.codi_pantalla = data["codi_pantalla"]
    equip.marca_sai = data["marca_sai"]
    equip.model_sai = data["model_sai"]
    equip.num_serie_sai = data["num_serie_sai"]
    equip.codi_sai = data["codi_sai"]
    # Cont Comercial = data[?]
    # Cont Tecnic = data[?]
    # Observacions = data[?]
    equip.marca_lector = data["marca_lector"]
    equip.model_lector = data["model_lector"]
    equip.num_serie_lector = data["num_serie_lector"]
    equip.codi_lector = data["codi_lector"]
    equip.marca_impresora = data["marca_impresora"]
    equip.model_impresora = data["model_impresora"]
    equip.num_serie_impresora = data["num_serie_impresora"]
    equip.codi_impresora = data["codi_impresora"]
    equip.marca_tensio = data["marca_tensio"]
    equip.model_tensio = data["model_tensio"]
    equip.num_serie_tensio = data["num_serie_tensio"]
    equip.codi_tensio = data["codi_tensio"]
    equip.soft_1 = data["soft_1"]
    equip.versio_1 = data["versio_1"]
    equip.soft_2 = data["soft_2"]
    equip.versio_2 = data["versio_2"]
    equip.soft_3 = data["soft_3"]
    equip.versio_3 = data["versio_3"]
    equip.soft_4 = data["soft_4"]
    equip.versio_4 = data["versio_4"]
    equip.soft_5 = data["soft_5"]
    equip.versio_5 = data["versio_5"]
    equip.personal_tecnic_udmmp = data["personal_tecnic_udmmp"]
    equip.facultatius_udmmp = data["facultatius_udmmp"]
    equip.personal_tecnic_udmmp_2 = data["personal_tecnic_udmmp_2"]
    equip.facultatius_udmmp_2 = data["facultatius_udmmp_2"]
    equip.personal_tecnic_udmmp_3 = data["personal_tecnic_udmmp_3"]
    equip.facultatius_udmmp_3 = data["facultatius_udmmp_3"]
    equip.personal_tecnic_udmmp_4 = data["personal_tecnic_udmmp_4"]
    equip.facultatius_udmmp_4 = data["facultatius_udmmp_4"]
    equip.personal_tecnic_udmmp_5 = data["personal_tecnic_udmmp_5"]
    equip.facultatius_udmmp_5 = data["facultatius_udmmp_5"]
    equip.ref_fung1 = data["ref_fung1"]
    equip.desc_fung1 = data["desc_fung1"]
    equip.ref_fung2 = data["ref_fung2"]
    equip.desc_fung2 = data["desc_fung2"]
    equip.ref_fung3 = data["ref_fung3"]
    equip.desc_fung3 = data["desc_fung3"]
    equip.ref_fung4 = data["ref_fung4"]
    equip.desc_fung4 = data["desc_fung4"]
    equip.ref_fung5 = data["ref_fung5"]
    equip.desc_fung5 = data["desc_fung5"]
    equip.doc1 = data["doc1"]
    equip.doc2 = data["doc2"]
    equip.cont_manteniment = data["cont_manteniment"]
    equip.manteniment_ext = data["manteniment_ext"]
    equip.manteniment_int = data["manteniment_int"]
    equip.verificacio_int = data["verificacio_int"]
    equip.verificacio_ext = data["verificacio_ext"]
    equip.cal_ext = data["cal_ext"]
    equip.cal_int = data["cal_int"]
    equip.nom_contracte = data["nom_contracte"]
    equip.emp_respon1 = data["emp_respon1"]
    equip.periode_cober1 = data["periode_cober1"]
    equip.dades_cont1 = data["dades_cont1"]
    equip.emp_respon2 = data["emp_respon2"]
    equip.periode_cober2 = data["periode_cober2"]
    equip.dades_cont2 = data["dades_cont2"]
    equip.emp_respon_prev_ext = data["emp_respon_prev_ext"]
    equip.periodicitat_prev_ext = data["periodicitat_prev_ext"]
    equip.cont_prev_ext = data["cont_prev_ext"]
    equip.mant_prev_ext = data["mant_prev_ext"]
    equip.verif_prev_ext = data["verif_prev_ext"]
    equip.calib_prev_ext = data["calib_prev_ext"]
    equip.marges_accept_prev_ext = data["marges_accept_prev_ext"]
    equip.desc_prev_int = data["desc_prev_int"]
    equip.periodicitat_prev_int = data["periodicitat_prev_int"]
    equip.marges_accept_prev_int = data["marges_accept_prev_int"]
    equip.desc_verif_int = data["desc_verif_int"]
    equip.periodicitat_verif_int = data["periodicitat_verif_int"]
    equip.marges_accept_verif_int = data["marges_accept_verif_int"]
    equip.calib_desc_int = data["calib_desc_int"]
    equip.calib_periodicitat_int = data["calib_periodicitat_int"]
    equip.calib_marges_accept_int = data["calib_marges_accept_int"]
    equip.motiu_modificacio = data["motiu_modificacio"]
    models.session.commit()

    # Generar DOCX i PDF
    path_docx, report_name = utils.create_docx(data)
    utils.create_pdf(path_docx, report_name)
    path_pdf = "pdfs/" + report_name + ".pdf"
    # path_zip = utils.zip_files(path_docx, path_pdf, report_name)

    return send_file(path_pdf, as_attachment=True)

    # except Exception:
    #     flash("No s'ha creat el pdf, error intern!", "warning")
    #     return redirect("/")


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


# Historic
@app.route("/historic")
def historic():
    equips = models.session.query(models.Fitxes).filter(models.Fitxes.codi_aux.like('EIM%'),
                                                        models.Fitxes.motiu_modificacio.isnot(None),
                                                        models.Fitxes.motiu_modificacio != '').all()

    return render_template("historic.html", equips=equips)


# Historic PDF
@app.route("/historic_pdf", methods=["POST"])
def historic_pdf():
    codi_equip = request.form['codi']
    path_pdf = "pdfs/" + codi_equip + ".pdf"
    return send_file(path_pdf, as_attachment=True)


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


@app.route('/guardar_imagenes_desc', methods=['POST'])
def guardar_imagenes_desc():
    imagenes = request.files.getlist('imagenes[]')
    for imagen in imagenes:
        if imagen:
            filename = os.path.join("app/static", imagen.filename)
            imagen.save(filename)

    return "ok"


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


@app.route('/receive_token', methods=["POST", "GET"])
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
        session['acronim'] = decoded_token.get('rol_tok', 'Usuario no encontrado')
        print(session['user'])
        print(session['rols'])
        print(session['email'])
        print(session['idClient'])
        print(session['rol'])
        print(session['acronim'])
        return redirect('/')
    except Exception:
        return redirect('/logout')


@app.route('/apps', methods=["POST", "GET"])
def apps():
    tocken_cookies = {'user_tok': session['user'], 'rols_tok': session['rols'], 'email_tok': session['email'],
                      'id_client_tok': session['idClient'], 'rol_tok': 'None', 'acronim_tok': session['acronim']}
    secret_key = '12345'
    token = jwt.encode(tocken_cookies, secret_key, algorithm='HS256')
    url = f'{URL_HOME}apps/token?token={token}'

    return redirect(url)
