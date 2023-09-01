from flask import render_template, request, flash, redirect, send_file
from app import app
from app import utils


# ROUTE FLASK
@app.route("/")
def inici():
    """
    Redirecciona a la pagina principal.

    :returns: Retorna el html de la pagina principal.
    :rtype: render_template
    """
    # Redirecciona al html
    return render_template("index.html")


# Ruta per seleccionar les files de les mostres
@app.route("/seleccionar_arxiu", methods=["POST", "GET"])
def seleccionar_arxiu():
    """
    Redirecciona l'html principal per afegir l'arxiu d'input.

    :returns: Retorna l'html corresponent.
    :rtype: render_template
    """

    return render_template("seleccionar_arxiu.html")
