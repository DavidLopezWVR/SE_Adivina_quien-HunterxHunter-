# interfaz.py

import pygame
import sys

def mostrar_pantalla_inicio(pantalla, ancho, alto, fondo_path=None):
    
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    fuente = pygame.font.SysFont("comicsansms", 40)  # Comic Sans, tamaño 40

    if fondo_path:
        fondo = pygame.image.load(fondo_path)
        fondo = pygame.transform.scale(fondo, (ancho, alto))
    else:
        fondo = None

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Enter para comenzar
                    return True
                elif evento.key == pygame.K_ESCAPE:  # Escape para salir
                    pygame.quit()
                    sys.exit()

        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill(blanco)

        texto_inicio = fuente.render("Presiona [Enter] para comenzar", True, negro, (200, 200, 255))
        texto_salir = fuente.render("Presiona [Esc] para salir", True, negro, (255, 200, 200))


        pantalla.blit(texto_inicio, texto_inicio.get_rect(center=(400,600)))
        pantalla.blit(texto_salir, texto_salir.get_rect(center=(400,150)))

        pygame.display.flip()
