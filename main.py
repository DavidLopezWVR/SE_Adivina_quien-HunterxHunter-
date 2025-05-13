# main.py
from base_datos import obtener_personajes

def filtrar_personajes(personajes, respuestas):
    """
    Filtra los personajes según las respuestas dadas.
    """
    filtrados = []
    for personaje in personajes:
        coincide = True
        for pregunta, respuesta in respuestas.items():
            if personaje.get(pregunta) != respuesta:
                coincide = False
                break
        if coincide:
            filtrados.append(personaje)
    return filtrados

def obtener_personaje_adivinado(candidatos):
    """
    Si hay un solo candidato, lo devuelve, si no hay candidatos, devuelve 'Ninguno'.
    """
    if len(candidatos) == 1:
        return candidatos[0]
    return None
