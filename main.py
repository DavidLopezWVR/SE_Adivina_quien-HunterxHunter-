# main.py
from preguntas import obtener_preguntas
from interfaz import mostrar_pantalla_inicio
from agregar_personajes import agregar_personaje_pygame
import pygame
import json
import sys

with open("personajes.json", "r", encoding="utf-8") as archivo:
    PERSONAJES = json.load(archivo)

# Inicialización
pygame.init()
ANCHO, ALTO = 900, 800
pygame.display.set_caption("Adivina el personaje - HunterxHunter")
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Mostrar pantalla inicial antes de cargar juego
mostrar_pantalla_inicio(pantalla, ANCHO, ALTO, fondo_path="img_interfaz/fondo_2.png")

#Pantalla de juego
fuente = pygame.font.SysFont(None, 36)
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Preguntas y claves extendidas
preguntas = obtener_preguntas()

personajes_filtrados = PERSONAJES.copy()
pregunta_actual = 0

def mostrar_texto(texto, y, centro=True):
    render = fuente.render(texto, True, negro)
    rect = render.get_rect(center=(ANCHO // 2, y)) if centro else render.get_rect(topleft=(20, y))
    pantalla.blit(render, rect)

def mostrar_imagen(nombre_archivo):
    imagen = pygame.image.load(nombre_archivo)
    imagen = pygame.transform.scale(imagen, (200, 300))
    pantalla.blit(imagen, (ANCHO // 2 - 100, 100))

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
        mostrar_texto("No pude adivinar el personaje.", ALTO // 2 - 30)
        mostrar_texto("Presiona [A] para agregarlo", ALTO // 2 + 10)
        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_a:
                        agregar_personaje_pygame(pantalla, PERSONAJES)

                        # 🔄 Reiniciar juego
                        with open("personajes.json", "r", encoding="utf-8") as archivo:
                            PERSONAJES = json.load(archivo)
                        personajes_filtrados = PERSONAJES.copy()
                        pregunta_actual = 0
                        esperando = False  # salir del bucle interno y continuar el juego
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


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
