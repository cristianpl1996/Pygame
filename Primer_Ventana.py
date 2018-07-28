import pygame, sys
from pygame.locals import *

ancho=300
alto=300

def main():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Primer Ventana")

	while True:
		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()


main()	