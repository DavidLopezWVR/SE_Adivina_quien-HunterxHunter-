# interfaz.py

import pygame
import sys

def mostrar_pantalla_inicio(pantalla, ancho, alto, fondo_path=None):
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    azul = (100, 149, 237)
    azul_hover = (65, 105, 225)
    rojo = (255, 99, 71)
    rojo_hover = (220, 20, 60)

    fuente = pygame.font.SysFont("impact", 40)

    # Botones
    boton_comenzar = pygame.Rect(ancho // 2 - 150, alto // 2 - 60, 300, 60)
    boton_salir = pygame.Rect(ancho // 2 - 150, alto // 2 + 20, 300, 60)
    radio = 15  # Radio para esquinas redondeadas

    # Fondo
    if fondo_path:
        fondo = pygame.image.load(fondo_path)
        fondo = pygame.transform.scale(fondo, (ancho, alto))
    else:
        fondo = None

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_comenzar.collidepoint(evento.pos):
                    return True
                elif boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill(blanco)

        # Cambiar color si el mouse está encima
        color_comenzar = azul_hover if boton_comenzar.collidepoint(mouse_pos) else azul
        color_salir = rojo_hover if boton_salir.collidepoint(mouse_pos) else rojo

        # Dibujar botones redondeados
        pygame.draw.rect(pantalla, color_comenzar, boton_comenzar, border_radius=radio)
        pygame.draw.rect(pantalla, color_salir, boton_salir, border_radius=radio)

        texto_comenzar = fuente.render("Comenzar", True, blanco)
        texto_salir = fuente.render("Salir", True, blanco)

        pantalla.blit(texto_comenzar, texto_comenzar.get_rect(center=boton_comenzar.center))
        pantalla.blit(texto_salir, texto_salir.get_rect(center=boton_salir.center))

        pygame.display.flip()

