import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((300,300))
	pygame.display.set_caption("Superficies")
	reloj=pygame.time.Clock()
	blanco=(255,255,255)
	rojo=(255,0,0)
	azul=(0,0,255)
	s1= pygame.Surface((100,150))
	s1.fill(rojo)
	s2= pygame.Surface((25,25))
	s2.fill(azul)

	while True:
			
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		reloj.tick(20)
		pantalla.fill(blanco)
		pantalla.blit(s1,(100,100))
		pantalla.blit(s2,(100,100))
		pygame.display.update()

main()	