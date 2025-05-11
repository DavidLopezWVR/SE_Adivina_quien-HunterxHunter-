# Lista de personajes con atributos
personajes = [
    {
        "nombre": "Gandalf",
        "humano": True,
        "mujer": False,
        "tiene_barba": True,
        "usa_sombrero": True
    },
    {
        "nombre": "Elsa",
        "humano": True,
        "mujer": True,
        "tiene_barba": False,
        "usa_sombrero": False
    },
    {
        "nombre": "Pikachu",
        "humano": False,
        "mujer": False,
        "tiene_barba": False,
        "usa_sombrero": False
    },
    {
        "nombre": "La Mujer Maravilla",
        "humano": True,
        "mujer": True,
        "tiene_barba": False,
        "usa_sombrero": False
    }
]

preguntas = [
    ("humano", "¿Tu personaje es humano? (s/n): "),
    ("mujer", "¿Tu personaje es mujer? (s/n): "),
    ("tiene_barba", "¿Tu personaje tiene barba? (s/n): "),
    ("usa_sombrero", "¿Tu personaje usa sombrero? (s/n): ")
]
def interpretar_respuesta(r):
    return r.strip().lower() in ["s", "sí", "si"]

def jugar():
    posibles = personajes.copy()

    for atributo, pregunta in preguntas:
        respuesta = input(pregunta)
        valor_usuario = interpretar_respuesta(respuesta)

        # Filtro con Modus Ponens
        posibles = [p for p in posibles if p[atributo] == valor_usuario]

        if len(posibles) == 1:
            print(f"\n🎯 ¡Tu personaje es {posibles[0]['nombre']}!")
            return
        elif len(posibles) == 0:
            print("\n❌ No conozco ese personaje.")
            return

    if len(posibles) > 1:
        print("\n🤔 No estoy seguro, pero podría ser uno de estos:")
        for p in posibles:
            print(f"- {p['nombre']}")

if __name__ == "__main__":
    print("🤖 ¡Piensa en un personaje y yo lo adivinaré!")
    jugar()
