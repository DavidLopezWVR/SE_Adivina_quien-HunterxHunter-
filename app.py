from flask import Flask, render_template, request, redirect, session, url_for
import json
import os

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Ruta al archivo JSON
RUTA_JSON = "personajes.json"

# Características que se preguntarán en orden
CARACTERISTICAS = ["sexo", "es_usuario_de_nen", "tipo_de_nen", "clan"]

def cargar_personajes():
    if os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_personajes(personajes):
    with open(RUTA_JSON, "w", encoding="utf-8") as f:
        json.dump(personajes, f, indent=4, ensure_ascii=False)

@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

@app.route("/jugar")
def jugar():
    session["pregunta_actual"] = 0
    session["respuestas"] = {}
    session["posibles"] = cargar_personajes()
    return redirect(url_for("preguntar_caracteristica"))

@app.route("/preguntar", methods=["GET", "POST"])
def preguntar_caracteristica():
    if request.method == "POST":
        caracteristica = CARACTERISTICAS[session["pregunta_actual"]]
        valor = request.form["valor"]
        session["respuestas"][caracteristica] = valor

        # Filtrar personajes según respuestas
        filtrados = []
        for p in session["posibles"]:
            valor_p = str(p.get(caracteristica, "")).lower()
            if valor_p == valor.lower():
                filtrados.append(p)

        session["posibles"] = filtrados
        session["pregunta_actual"] += 1

    # Si queda solo un personaje
    if len(session["posibles"]) == 1:
        return redirect(url_for("adivinar"))

    # Si no quedan opciones
    if not session["posibles"]:
        return redirect(url_for("enseniar"))

    # Si aún hay preguntas por hacer
    if session["pregunta_actual"] < len(CARACTERISTICAS):
        siguiente = CARACTERISTICAS[session["pregunta_actual"]]
        return render_template("pregunta_caracteristica.html", caracteristica=siguiente)

    # Ya se preguntó todo pero hay más de un personaje
    return redirect(url_for("adivinar"))

@app.route("/adivinar", methods=["GET", "POST"])
def adivinar():
    personaje = session["posibles"][0]

    if request.method == "POST":
        if request.form["respuesta"] == "si":
            return render_template("gracias.html", nombre=personaje["nombre"])
        else:
            return redirect(url_for("enseniar"))

    return render_template("preguntar.html", personaje=personaje)

@app.route("/enseniar", methods=["GET", "POST"])
def enseniar():
    if request.method == "POST":
        nuevo_personaje = {
            "nombre": request.form["nombre"],
            "sexo": request.form["sexo"],
            "edad": request.form["edad"],
            "es_usuario_de_nen": "true" if "es_usuario_de_nen" in request.form else "false",
            "tipo_de_nen": request.form["tipo_de_nen"],
            "clan": request.form["clan"]
        }
        personajes = cargar_personajes()
        personajes.append(nuevo_personaje)
        guardar_personajes(personajes)
        return render_template("gracias.html", nombre=nuevo_personaje["nombre"])
    return render_template("enseniar.html")

if __name__ == "__main__":
    app.run(debug=True)



