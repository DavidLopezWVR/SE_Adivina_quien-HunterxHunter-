# hxh_web_game/app.py
from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'hunterxhunter_clave_secreta'

ARCHIVO = "personajes.json"
ATRIBUTOS = ["sexo", "edad", "es_usuario_de_nen", "tipo_de_nen", "clan"]

# ----------------------------
# Funciones auxiliares
# ----------------------------
def cargar_personajes():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_personajes(personajes):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(personajes, f, indent=4, ensure_ascii=False)

def filtrar_por_atributo(personajes, atributo, valor):
    return [p for p in personajes if str(p.get(atributo)).lower() == str(valor).lower()]

# ----------------------------
# Rutas del juego
# ----------------------------
@app.route("/")
def inicio():
    session['personajes'] = cargar_personajes()
    session['indice'] = 0
    return redirect(url_for('preguntar'))

@app.route("/preguntar", methods=["GET", "POST"])
def preguntar():
    personajes = session.get('personajes', [])
    indice = session.get('indice', 0)

    if len(personajes) == 1:
        return render_template("adivinar.html", personaje=personajes[0])

    if indice >= len(ATRIBUTOS):
        return render_template("no_se.html")

    atributo_actual = ATRIBUTOS[indice]

    if request.method == "POST":
        respuesta = request.form.get("respuesta")
        valor = True if respuesta == "sí" else False
        if atributo_actual in ["sexo", "edad", "tipo_de_nen", "clan"]:
            valor = request.form.get("valor")
        personajes_filtrados = filtrar_por_atributo(personajes, atributo_actual, valor)
        session['personajes'] = personajes_filtrados
        session['indice'] = indice + 1
        return redirect(url_for('preguntar'))

    return render_template("pregunta.html", atributo=atributo_actual)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "sexo": request.form["sexo"],
            "edad": request.form["edad"],
            "es_usuario_de_nen": request.form["es_usuario_de_nen"] == "sí",
            "tipo_de_nen": request.form["tipo_de_nen"],
            "clan": request.form["clan"] or None
        }
        personajes = cargar_personajes()
        personajes.append(datos)
        guardar_personajes(personajes)
        return redirect(url_for("inicio"))
    return render_template("nuevo.html")

if __name__ == "__main__":
    app.run(debug=True)

