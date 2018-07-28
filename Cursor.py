import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((400,400))
	pygame.display.set_caption("Cursor")
	reloj=pygame.time.Clock()
	#Colores.
	blanco=(255,255,255)
	rojo=(255,0,0)
	azul=(0,0,255)
	#Rectangulos
	r1=pygame.Rect(50,50,45,45)
	r2=pygame.Rect(200,200,100,50)	
	#Loop principal.
	while True:
			
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == MOUSEBUTTONDOWN:
				pygame.mouse.set_pos(150,150)	
						
							

		reloj.tick(20)#Fijo a 20fps.
		pantalla.fill(blanco)#Pinto superficie de fondo blanco
		r1.left,r1.top = pygame.mouse.get_pos()
		r1.left-=r1.width/2
		r1.top-=r1.height/2
		pygame.draw.rect(pantalla,rojo,r1)
		pygame.draw.rect(pantalla,azul,r2)
		pygame.display.update()

main()	