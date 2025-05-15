# agregar_personajes.py

import pygame
import sys
import json

# Colores y dimensiones
blanco = (255, 255, 255)
negro = (0, 0, 0)
ANCHO, ALTO = 800, 600

def mostrar_texto(texto, y, pantalla, fuente, centro=True):
    render = fuente.render(texto, True, negro)
    rect = render.get_rect(center=(ANCHO // 2, y)) if centro else render.get_rect(topleft=(20, y))
    pantalla.blit(render, rect)

def agregar_personaje_pygame(pantalla, PERSONAJES):
    fuente = pygame.font.SysFont(None, 36)  # ← Mover aquí la inicialización

    campos = [
        ("Nombre del personaje:", "nombre"),
        ("Ruta de imagen:", "imagen"),
        ("¿Es masculino? (s/n):", "sexo_masculino"),
        ("¿Es usuario de Nen? (s/n):", "es_usuario_de_nen"),
        ("¿Es maestro de Nen? (s/n):", "es_maestro_nen"),
        ("¿Es miembro del Genei Ryodan? (s/n):", "es_miembro_del_Genei_Ryodan"),
        ("¿Usa cartas como arma? (s/n):", "usa_cartas"),
        ("¿Usa katanas? (s/n):", "usa_katanas"),
        ("¿Tiene cabello blanco? (s/n):", "tiene_cabello_blanco"),
        ("¿Tiene ojos rojos? (s/n):", "tiene_ojos_rojos"),
        ("¿Es asesino? (s/n):", "es_asesino"),
        ("¿Es una quimera? (s/n):", "es_quimera"),
        ("¿Es de la familia Zoldyck? (s/n):", "es_de_la_familia_zoldyck"),
        ("¿Pertenece al gremio de cazadores? (s/n):", "pertenece_al_gremio_de_cazadores"),
        ("¿Es adulto? (s/n):", "es_adulto"),
        ("¿Usa traje? (s/n):", "usa_traje"),
        ("¿Es antagonista? (s/n):", "es_antagonista"),
        ("¿Tiene apariencia infanto-juvenil? (s/n):", "tiene_apariencia_infanto_juvenil"),
        ("¿Es padre/madre de otro personaje? (s/n):", "es_padre_de_otro_personaje"),
        ("¿Ha reencarnado o cambiado de forma? (s/n):", "reencarno_o_cambio_de_forma")
    ]

    nuevo_personaje = {}
    texto_input = ''
    indice_campo = 0
    escribiendo = True

    while escribiendo:
        pantalla.fill(blanco)
        pregunta, clave = campos[indice_campo]
        mostrar_texto("Agregar nuevo personaje", 50, pantalla, fuente)
        mostrar_texto(pregunta, 150, pantalla, fuente)
        mostrar_texto(texto_input, 250, pantalla, fuente)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                elif evento.key == pygame.K_RETURN:
                    valor = texto_input.strip()
                    if clave in ["nombre", "imagen"]:
                        nuevo_personaje[clave] = valor
                    else:
                        nuevo_personaje[clave] = valor.lower() == 's'
                    texto_input = ''
                    indice_campo += 1
                    if indice_campo >= len(campos):
                        escribiendo = False
                else:
                    texto_input += evento.unicode

    PERSONAJES.append(nuevo_personaje)
    with open("personajes.json", "w", encoding="utf-8") as f:
        json.dump(PERSONAJES, f, indent=4, ensure_ascii=False)
