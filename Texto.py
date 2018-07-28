import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((480,300))
	pygame.display.set_caption("Texto")
	reloj=pygame.time.Clock()
	fuente=pygame.font.Font(None,48)
	texto=fuente.render("Hola Mundo",0,(255,255,255))

	while True:		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()		
				
		reloj.tick(20)	
		pantalla.fill((30,30,200))
		pantalla.blit(texto,(100,100))
		pygame.display.update()
				
main()