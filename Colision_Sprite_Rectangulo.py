import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla=pygame.display.set_mode((480,300))
	pygame.display.set_caption("Colision Sprite Rectangulo")
	reloj=pygame.time.Clock()
	imagen=pygame.image.load("imagen.png")
	x,y=100,100
	vx,vy=0,0
	r1=pygame.Rect(250,70,25,500)
	sprite=pygame.sprite.Sprite()
	sprite.image=imagen
	sprite.rect=imagen.get_rect()
	sprite.rect.top=50
	sprite.rect.left=50
	while True:
		pantalla.fill((255,255,255))	
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
			if evento.type==KEYDOWN:
				if evento.key==K_LEFT:
					vx-=10
				if evento.key==K_RIGHT:
					vx+=10
				if evento.key==K_UP:
					vy-=10
				if evento.key==K_DOWN:
					vy+=10			
			if evento.type==KEYUP:			
				if evento.key==K_LEFT:
					vx=0
				if evento.key==K_RIGHT:
					vx=0
				if evento.key==K_UP:
					vy=0
				if evento.key==K_DOWN:
					vy=0			
		
		oldx=sprite.rect.left
		oldy=sprite.rect.top
		sprite.rect.move_ip(vx,vy)
		if sprite.rect.colliderect(r1):
			sprite.rect.left=oldx
			sprite.rect.top=oldy

		reloj.tick(20)
		pygame.draw.rect(pantalla,(0,0,0),r1)
		pantalla.blit(sprite.image,sprite.rect)
		pygame.display.update()

main()	