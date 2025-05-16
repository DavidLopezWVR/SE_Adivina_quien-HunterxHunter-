#main.py

import pygame
import sys
import json
from preguntas import obtener_preguntas
from interfaz import mostrar_pantalla_inicio
from agregar_personajes import agregar_personaje_pygame

# Inicialización
pygame.init()
ANCHO, ALTO = 1000, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina el personaje - Hunter x Hunter")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 200, 0)
verde_claro = (0, 255, 0)
rojo = (200, 0, 0)
rojo_claro = (255, 0, 0)
gris = (100, 100, 100)
gris_claro = (170, 170, 170)

# Fuente
fuente = pygame.font.SysFont("impact", 36)

# Cargar personajes
with open("personajes.json", "r", encoding="utf-8") as archivo:
    PERSONAJES = json.load(archivo)

# Mostrar pantalla de inicio
mostrar_pantalla_inicio(pantalla, ANCHO, ALTO, fondo_path="img_interfaz/fondo_1.png")

# Fondo del juego
fondo_juego = pygame.image.load("img_interfaz/fondo_2.jpg")
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))

# Preguntas
preguntas = obtener_preguntas()
personajes_filtrados = PERSONAJES.copy()
pregunta_actual = 0

# Funciones
def mostrar_pregunta_con_fondo(pregunta, y):
    caja = pygame.Surface((ANCHO - 10, 80), pygame.SRCALPHA)
    caja.fill((255, 255, 255, 180))
    rect = caja.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(caja, rect)

    texto = fuente.render(pregunta, True, negro)
    texto_rect = texto.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(texto, texto_rect)

def dibujar_boton(texto, x, y, ancho, alto, color, color_hover, mouse_pos):
    rect = pygame.Rect(x, y, ancho, alto)
    es_hover = rect.collidepoint(mouse_pos)
    color_final = color_hover if es_hover else color
    pygame.draw.rect(pantalla, color_final, rect, border_radius=15)

    texto_render = fuente.render(texto, True, blanco)
    texto_rect = texto_render.get_rect(center=rect.center)
    pantalla.blit(texto_render, texto_rect)

    return rect

def mostrar_imagen(nombre_archivo):
    imagen = pygame.image.load(nombre_archivo)
    imagen = pygame.transform.scale(imagen, (400, 500))
    pantalla.blit(imagen, (ANCHO // 2 - 100, 100))

def pantalla_final(personaje):
    pantalla.blit(fondo_juego, (0, 0))
    mostrar_pregunta_con_fondo(f"¡Tu personaje es: {personaje['nombre']}!", 50)
    mostrar_imagen(personaje["imagen"])
    pygame.display.flip()
    pygame.time.wait(5000)

# Bucle principal
while True:
    pantalla.blit(fondo_juego, (0, 0))

    if len(personajes_filtrados) == 1:
        pantalla_final(personajes_filtrados[0])
        break

    elif pregunta_actual >= len(preguntas):
        mostrar_pregunta_con_fondo("No pude adivinar el personaje.", ALTO // 2 - 80)

        mouse_pos = pygame.mouse.get_pos()
        boton_agregar = dibujar_boton("AGREGAR", ANCHO // 2 - 160, ALTO // 2, 140, 60, verde, verde_claro, mouse_pos)
        boton_salir_final = dibujar_boton("SALIR", ANCHO // 2 + 20, ALTO // 2, 140, 60, rojo, rojo_claro, mouse_pos)

        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_agregar.collidepoint(evento.pos):
                        exito = agregar_personaje_pygame(pantalla, PERSONAJES)

                        if exito:
                            with open("personajes.json", "r", encoding="utf-8") as archivo:
                                PERSONAJES = json.load(archivo)

                            personajes_filtrados = PERSONAJES.copy()
                            pregunta_actual = 0

                            # Volver a pantalla de inicio
                            mostrar_pantalla_inicio(pantalla, ANCHO, ALTO, fondo_path="img_interfaz/fondo_1.png")
                            fondo_juego = pygame.image.load("img_interfaz/fondo_2.jpg")
                            fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))
                        esperando = False
                    elif boton_salir_final.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

        continue

    # Mostrar pregunta
    texto_pregunta, clave = preguntas[pregunta_actual]
    mostrar_pregunta_con_fondo(texto_pregunta, ALTO // 3)

    # Botones
    mouse_pos = pygame.mouse.get_pos()
    boton_si = dibujar_boton("SÍ", ANCHO // 2 - 200, ALTO // 2, 120, 60, verde, verde_claro, mouse_pos)
    boton_no = dibujar_boton("NO", ANCHO // 2 + 80, ALTO // 2, 120, 60, rojo, rojo_claro, mouse_pos)
    boton_salir = dibujar_boton("SALIR", ANCHO // 2 - 60, ALTO // 2 + 100, 120, 50, gris, gris_claro, mouse_pos)

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_si.collidepoint(evento.pos):
                personajes_filtrados = [p for p in personajes_filtrados if p.get(clave) == True]
                pregunta_actual += 1
            elif boton_no.collidepoint(evento.pos):
                personajes_filtrados = [p for p in personajes_filtrados if p.get(clave) == False]
                pregunta_actual += 1
            elif boton_salir.collidepoint(evento.pos):
                pygame.quit()
                sys.exit()

