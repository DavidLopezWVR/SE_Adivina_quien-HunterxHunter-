import json
import os

# ------------------------------------------
# Archivo de datos
# ------------------------------------------
ARCHIVO_PERSONAJES = "personajes.json"

# ------------------------------------------
# Preguntas con sus atributos y textos
# ------------------------------------------
preguntas = {
    "sexo": {
        "texto": "¿Cuál es el sexo del personaje? (masculino/femenino): ",
        "tipo": "opcion"
    },
    "edad": {
        "texto": "¿Qué edad tiene? (niño/adolescente/adulto): ",
        "tipo": "opcion"
    },
    "tipo_de_nen": {
        "texto": "¿Qué tipo de nen tiene? (reforzador/emisor/transmutador/especialista/conjurador/manipulador): ",
        "tipo": "opcion"
    },
    "clan": {
        "texto": "¿Pertenece a algún clan? (Zoldyck/Kurta/Ninguno): ",
        "tipo": "opcion"
    }
}

# ------------------------------------------
# Cargar personajes desde archivo JSON
# ------------------------------------------
def cargar_personajes():
    if os.path.exists(ARCHIVO_PERSONAJES):
        with open(ARCHIVO_PERSONAJES, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []  # En caso de que el archivo no exista

# ------------------------------------------
# Guardar personajes al archivo JSON
# ------------------------------------------
def guardar_personajes(personajes):
    with open(ARCHIVO_PERSONAJES, "w", encoding="utf-8") as f:
        json.dump(personajes, f, indent=4, ensure_ascii=False)

# ------------------------------------------
# Aprender un nuevo personaje del usuario
# ------------------------------------------
def aprender_nuevo_personaje(personajes):
    print("\n🧠 Enséñame sobre ese personaje que no conozco...")
    nombre = input("Nombre del personaje: ").strip()

    nuevo = {
        "nombre": nombre,
        "es_usuario_de_nen": True  # Asumimos que todos usan nen
    }

    for atributo, config in preguntas.items():
        respuesta = input(config["texto"]).strip().lower()
        if atributo == "clan" and respuesta == "ninguno":
            respuesta = None
        nuevo[atributo] = respuesta

    personajes.append(nuevo)
    guardar_personajes(personajes)
    print(f"\n✅ ¡Gracias! He aprendido sobre {nombre}.")

# ------------------------------------------
# Juego principal
# ------------------------------------------
def jugar():
    personajes = cargar_personajes()

    if not personajes:
        print("⚠️ No hay personajes cargados. Agrega al menos uno en personajes.json.")
        return

    print("🧠 ¡Piensa en un personaje de Hunter x Hunter y yo lo adivinaré!\n")

    posibles = personajes.copy()

    for atributo, config in preguntas.items():
        respuesta = input(config["texto"]).strip().lower()

        if atributo == "clan" and respuesta == "ninguno":
            respuesta = None

        posibles = [
            p for p in posibles if str(p[atributo]).lower() == str(respuesta)
        ]

        if len(posibles) == 1:
            print(f"\n🎯 ¡Tu personaje es {posibles[0]['nombre']}!")
            return
        elif len(posibles) == 0:
            print("\n❌ No conozco ese personaje.")
            aprender = input("¿Quieres enseñármelo? (sí/no): ").strip().lower()
            if aprender in ["sí", "si", "s"]:
                aprender_nuevo_personaje(personajes)
            else:
                print("👌 Está bien, tal vez la próxima vez.")
            return

    if len(posibles) > 1:
        print("\n🤔 No estoy seguro, pero podría ser uno de estos:")
        for p in posibles:
            print(f"- {p['nombre']}")

# ------------------------------------------
# Ejecutar juego
# ------------------------------------------
if __name__ == "__main__":
    jugar()

