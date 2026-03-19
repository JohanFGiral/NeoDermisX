from flask import Blueprint, render_template
from flask import request
import time
import os
from werkzeug.utils import secure_filename
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

    return "Archivo guardado correctamente ✅"