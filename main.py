# main.py
import pygame
import sys
from base_datos import PERSONAJES

# Inicialización
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina el personaje - Hunter x Hunter")
fuente = pygame.font.SysFont(None, 36)
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Preguntas y claves (más inteligentes)
preguntas = [
    ("¿Es un hombre?", "es_hombre"),
    ("¿Es usuario de Nen?", "es_usuario_de_nen"),
    ("¿Es miembro de la Brigada Fantasma?", "es_miembro_de_la_brigada"),
    ("¿Usa cartas como arma?", "usa_cartas"),
    ("¿Tiene el cabello blanco?", "tiene_cabello_blanco"),
    ("¿Es un asesino?", "es_asesino"),
    ("¿Usa una caña de pescar como arma?", "usa_pesca")
]

# Variables de juego
personajes_filtrados = PERSONAJES.copy()
pregunta_actual = 0

# Funciones para mostrar texto e imagen
def mostrar_texto(texto, y, centro=True):
    render = fuente.render(texto, True, negro)
    rect = render.get_rect(center=(ANCHO//2, y)) if centro else render.get_rect(topleft=(20, y))
    pantalla.blit(render, rect)

def mostrar_imagen(nombre_archivo):
    imagen = pygame.image.load(f"{nombre_archivo}")
    imagen = pygame.transform.scale(imagen, (200, 300))
    pantalla.blit(imagen, (ANCHO//2 - 100, 100))

def pantalla_final(personaje):
    pantalla.fill(blanco)
    mostrar_texto(f"¡Tu personaje es: {personaje['nombre']}!", 50)
    mostrar_imagen(personaje["imagen"])
    pygame.display.flip()
    pygame.time.wait(5000)

# Bucle principal
while True:
    pantalla.fill(blanco)

    if len(personajes_filtrados) == 1:
        pantalla_final(personajes_filtrados[0])
        break
    elif pregunta_actual >= len(preguntas):
        pantalla.fill(blanco)
        mostrar_texto("No pude adivinar el personaje.", ALTO // 2)
        pygame.display.flip()
        pygame.time.wait(5000)
        break

    texto_pregunta, clave = preguntas[pregunta_actual]
    mostrar_texto(texto_pregunta, ALTO // 3)
    mostrar_texto("Presiona [S] para Sí o [N] para No", ALTO // 2)

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                personajes_filtrados = [p for p in personajes_filtrados if p.get(clave) == True]
                pregunta_actual += 1
            elif evento.key == pygame.K_n:
                personajes_filtrados = [p for p in personajes_filtrados if p.get(clave) == False]
                pregunta_actual += 1
