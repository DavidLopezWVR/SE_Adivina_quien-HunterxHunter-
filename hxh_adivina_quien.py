from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'personajes.json'

def cargar_personajes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_personajes(personajes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(personajes, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    respuesta = request.form.get('respuesta')
    return render_template('adivinar.html')

@app.route('/enseniar', methods=['POST'])
def enseniar():
    personaje = {
        "nombre": request.form['nombre'],
        "sexo": request.form['sexo'],
        "edad": request.form['edad'],
        "es_usuario_de_nen": request.form.get('es_usuario_de_nen') == 'on',
        "tipo_de_nen": request.form['tipo_de_nen'],
        "clan": request.form['clan'] or None
    }
    personajes = cargar_personajes()
    personajes.append(personaje)
    guardar_personajes(personajes)
    return render_template('gracias.html', nombre=personaje["nombre"])

if __name__ == '__main__':
    app.run(debug=True)


