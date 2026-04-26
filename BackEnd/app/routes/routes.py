from flask import Blueprint, render_template
from flask import request
import time
import os
from werkzeug.utils import secure_filename
from app.modules.ia_processing import procesar
from flask import jsonify

main = Blueprint('main',__name__)

@main.route("/")
def index():
    return "onichan uwu mi compadre"

@main.route("/upload", methods=["POST"])
def upload():
    timestamp = str(time.time())
    archivo = request.files["imagen"]
    base_dir = os.path.dirname(os.path.dirname(__file__))
    carpeta = os.path.join(base_dir, "sources")

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    nombre = timestamp + secure_filename(archivo.filename)
    ruta = os.path.join(carpeta, nombre)

    archivo.save(ruta)
    
    try:
        pred, prob = procesar(ruta)
    finally:
        if os.path.exists(ruta):
            os.remove(ruta)

    return jsonify({
        "prediccion": pred,
        "probabilidad": prob
    })