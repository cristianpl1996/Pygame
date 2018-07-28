import pygame, sys, random
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((480,500))
	pygame.display.set_caption("Crear Muchos Rectangulos")
	reloj=pygame.time.Clock()
	listarec=[]

	for x in xrange(15):
		w=random.randrange(15,45)
		h=random.randrange(20,60)
		x=random.randrange(450)
		y=random.randrange(450)
		listarec.append(pygame.Rect(x,y,w,h))

	while True:		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		reloj.tick(20)
		pantalla.fill((0,0,0))
		for recs in listarec:
			pygame.draw.rect(pantalla,(0,0,255),recs)
		pygame.display.update()
		


main()			