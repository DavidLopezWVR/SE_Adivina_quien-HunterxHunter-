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
        # Datos iniciales por defecto
        return [
            {
                "nombre": "Gon Freecss",
                "sexo": "masculino",
                "edad": "niño",
                "es_usuario_de_nen": True,
                "tipo_de_nen": "reforzador",
                "clan": None
            },
            {
                "nombre": "Killua Zoldyck",
                "sexo": "masculino",
                "edad": "niño",
                "es_usuario_de_nen": True,
                "tipo_de_nen": "transmutador",
                "clan": "Zoldyck"
            },
            {
                "nombre": "Kurapika",
                "sexo": "masculino",
                "edad": "adolescente",
                "es_usuario_de_nen": True,
                "tipo_de_nen": "especialista",
                "clan": "Kurta"
            },
            {
                "nombre": "Hisoka",
                "sexo": "masculino",
                "edad": "adulto",
                "es_usuario_de_nen": True,
                "tipo_de_nen": "transmutador",
                "clan": None
            }
        ]

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

    nuevo = {"nombre": nombre, "es_usuario_de_nen": True}

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
            if aprender == "sí":
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
