# -------------------------------
# Juego tipo Akinator: Hunter x Hunter
# -------------------------------

# Base de personajes con atributos
personajes = [
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

# Diccionario de preguntas con tipo
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

# Función principal del juego
def jugar():
    print("🧠 ¡Piensa en un personaje de Hunter x Hunter y yo lo adivinaré!")
    posibles = personajes.copy()

    for atributo, config in preguntas.items():
        respuesta = input(config["texto"]).strip().lower()

        # Normalizar respuesta si es clan
        if atributo == "clan" and respuesta == "ninguno":
            respuesta = None

        # Filtrar posibles personajes
        posibles = [
            p for p in posibles if str(p[atributo]).lower() == str(respuesta)
        ]

        # Resultado temprano
        if len(posibles) == 1:
            print(f"\n🎯 ¡Tu personaje es {posibles[0]['nombre']}!")
            return
        elif len(posibles) == 0:
            print("\n❌ No conozco ese personaje.")
            return

    # Si quedan varios
    if len(posibles) > 1:
        print("\n🤔 No estoy seguro, pero podría ser uno de estos:")
        for p in posibles:
            print(f"- {p['nombre']}")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()
