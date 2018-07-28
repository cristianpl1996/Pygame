import pygame, sys, random
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((480,500))
	pygame.display.set_caption("Terminamos el Primer Juego")
	reloj=pygame.time.Clock()
	listarec=[]
	segundosint=0
	fuente=pygame.font.SysFont("Arial",25,True,False)
	info=fuente.render("Tienes 10 segundos",0,(255,255,255))
	sonido=pygame.mixer.Sound("sonido.wav")
	termino=False
	rotos=0
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
					if termino==False:
						if r1.colliderect(recs):
							sonido.play()
							recs.width=0
							recs.height=0
							rotos+=1

		reloj.tick(20)
		r1.left,r1.top=pygame.mouse.get_pos()
		r1.left -=r1.width/2
		r1.top -=r1.height/2
		pantalla.fill((0,0,0))
		for recs in listarec:
			pygame.draw.rect(pantalla,(0,0,255),recs)
		pygame.draw.rect(pantalla,(200,20,20),r1)	
		pantalla.blit(info,(5,5))
		if segundosint>=10:
			termino=True
		if termino==False:	
			segundosint=pygame.time.get_ticks()/1000
			segundos=str(segundosint)
			contador=fuente.render("Sg: "+segundos,0,(255,0,0))
		else:
			contador=fuente.render("Sg: "+segundos+" Usted rompio "+str(rotos),0,(255,0,0))	
		pantalla.blit(contador,(240,5))
		pygame.display.update()
				
main()