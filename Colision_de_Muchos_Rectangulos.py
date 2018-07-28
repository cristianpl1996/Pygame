import pygame, sys, random
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((480,500))
	pygame.display.set_caption("Colision de Muchos Rectangulos")
	reloj=pygame.time.Clock()
	listarec=[]

	r1=pygame.Rect(0,0,25,25)
	for x in xrange(25):
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
			if evento.type == MOUSEBUTTONDOWN:
				for recs in listarec:
					if r1.colliderect(recs):
						recs.width=0
						recs.height=0
					
				
		reloj.tick(20)
		r1.left,r1.top=pygame.mouse.get_pos()
		r1.left -=r1.width/2
		r1.top -=r1.height/2
		pantalla.fill((0,0,0))
		for recs in listarec:
			pygame.draw.rect(pantalla,(0,0,255),recs)
		pygame.draw.rect(pantalla,(200,20,20),r1)	
		pygame.display.update()
				
main()