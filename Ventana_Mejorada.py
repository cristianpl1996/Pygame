# Modulos
import pygame, sys
from pygame.locals import *
# Constantes.
WIDTH=400
HEIGHT=400
# Clases y Funciones.
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Ventana Mejorada")
	reloj = pygame.time.Clock()
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		reloj.tick(20)
		pantalla.fill((0,0,0))
		pygame.display.update()

if __name__ == "__main__":
    main()
