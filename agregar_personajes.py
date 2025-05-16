# agregar_personajes.py

import pygame
import sys
import json
import os

# Colores y dimensiones
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (100, 100, 100)
gris_claro = (170, 170, 170)
ANCHO, ALTO = 1000, 800

def mostrar_texto(texto, x, y, pantalla, fuente):
    render = fuente.render(texto, True, negro)
    rect = render.get_rect(topleft=(x, y))
    pantalla.blit(render, rect)

def dibujar_boton(texto, x, y, ancho, alto, color, color_hover, mouse_pos, pantalla, fuente):
    rect = pygame.Rect(x, y, ancho, alto)
    es_hover = rect.collidepoint(mouse_pos)
    color_final = color_hover if es_hover else color
    pygame.draw.rect(pantalla, color_final, rect, border_radius=15)
    render = fuente.render(texto, True, blanco)
    texto_rect = render.get_rect(center=rect.center)
    pantalla.blit(render, texto_rect)
    return rect

def crear_imagen_con_nombre(nombre, carpeta_destino="img"):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    ancho, alto = 400, 600
    fondo = pygame.Surface((ancho, alto))
    fondo.fill((255, 255, 255))  # fondo blanco

    fuente_grande = pygame.font.SysFont("impact", 36)
    texto = fuente_grande.render(nombre.upper(), True, (0, 0, 0))
    rect = texto.get_rect(center=(ancho // 2, alto // 2))
    fondo.blit(texto, rect)

    ruta_guardado = os.path.join(carpeta_destino, f"{nombre.lower().replace(' ', '_')}.png")
    pygame.image.save(fondo, ruta_guardado)
    return ruta_guardado

def agregar_personaje_pygame(pantalla, PERSONAJES):
    fuente = pygame.font.SysFont("impact", 32)

    fondo = pygame.image.load("img_interfaz/fondo_3.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    campos = [
        ("Nombre del personaje:", "nombre"),
        ("¿Es masculino? (s/n):", "sexo_masculino"),
        ("¿Es usuario de Nen? (s/n):", "es_usuario_de_nen"),
        ("¿Es maestro de Nen? (s/n):", "es_maestro_nen"),
        ("¿Es miembro del Genei Ryodan? (s/n):", "es_miembro_del_Genei_Ryodan"),
        ("¿Usa cartas como arma? (s/n):", "usa_cartas"),
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
        pantalla.blit(fondo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        mostrar_texto("AGREGAR NUEVO PERSONAJE", 180, 100, pantalla, fuente)
        pregunta, clave = campos[indice_campo]
        mostrar_texto(pregunta, 20, 230, pantalla, fuente)
        mostrar_texto(texto_input, 100, 270, pantalla, fuente)

        boton_cancelar = dibujar_boton("Cancelar", 400, 700, 200, 50, gris, gris_claro, mouse_pos, pantalla, fuente)

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
                    if clave == "nombre":
                        nuevo_personaje["nombre"] = valor
                        nuevo_personaje["imagen"] = crear_imagen_con_nombre(valor)
                    else:
                        nuevo_personaje[clave] = valor.lower() == 's'
                    texto_input = ''
                    indice_campo += 1
                    if indice_campo >= len(campos):
                        escribiendo = False
                else:
                    texto_input += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_cancelar.collidepoint(evento.pos):
                    return

    # Guardar en archivo
    PERSONAJES.append(nuevo_personaje)
    with open("personajes.json", "w", encoding="utf-8") as f:
        json.dump(PERSONAJES, f, indent=4, ensure_ascii=False)

    # Confirmación
    pantalla.blit(fondo, (0, 0))
    mostrar_texto("¡Personaje agregado correctamente!", 40, 300, pantalla, fuente)
    pygame.display.flip()
    pygame.time.wait(5000)

    return True

