import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla=pygame.display.set_mode((500,500))
	pygame.display.set_caption("Imagenes")
	reloj=pygame.time.Clock()
	imagen=pygame.image.load("imagen.png")
	x,y=0,0
	while True:
		pantalla.fill((255,255,255))
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
		reloj.tick(20)
		x,y= pygame.mouse.get_pos()
		pantalla.blit(imagen,(x,y))
		pygame.display.update()

main()	