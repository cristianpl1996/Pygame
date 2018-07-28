import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((400,400))
	pygame.display.set_caption("Eventos Teclas")
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
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					r1.move_ip(-10,0)
				if evento.key == K_RIGHT:
					r1.move_ip(10,0)
				if evento.key == K_UP:
					r1.move_ip(0,-10)
				if evento.key == K_DOWN:
					r1.move_ip(0,10)			
							

		reloj.tick(20)#Fijo a 20fps.
		pantalla.fill(blanco)#Pinto superficie de fondo blanco

		pygame.draw.rect(pantalla,rojo,r1)
		pygame.draw.rect(pantalla,azul,r2)
		pygame.display.update()

main()	