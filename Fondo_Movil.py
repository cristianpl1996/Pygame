import pygame, sys, random
from pygame.locals import *

class Fondo(pygame.sprite.Sprite):
	def __init__(self):
		self.imagen=pygame.image.load("fondomovil.gif").convert_alpha()
		self.rect=self.imagen.get_rect()
	def update(self,pantalla,vx,vy):
		self.rect.move_ip(-vx,-vy)
		pantalla.blit(self.imagen,self.rect)	
		

class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.imagen1=pygame.image.load("braid1.png").convert_alpha()
		self.imagen2=pygame.image.load("braid2.png").convert_alpha()
		self.imagen3=pygame.image.load("braid3.png").convert_alpha()
		self.imagen4=pygame.image.load("braid4.png").convert_alpha()
		self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
		self.imagen_actual=0
		self.imagen=self.imagenes[self.imagen_actual][0]
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=350,300
		self.moviendo=False
		self.orientacion=0
	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
	def update(self,superficie,vx,vy,t):
		if (vx,vy)==(0,0):
			self.moviendo=False
		else:
			self.moviendo=True
		if vx>0:
			self.orientacion=0
		elif vx<0:
			self.orientacion=1			
		if t==1 and self.moviendo:
			self.nextimagen()
		vx=0
		vy=0	
		self.mover(vx,vy)
		self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
		superficie.blit(self.imagen,self.rect)
	def nextimagen(self):
		self.imagen_actual+=1
		if self.imagen_actual>len(self.imagenes)-1:	
			self.imagen_actual=0	

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Segundo Juego")
	reloj = pygame.time.Clock()
	player1=Player()
	fondo1=Fondo()
	velocidad=10
	vx,vy=0,0
	leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
	t=0
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					leftsigueapretada=True
					vx-=velocidad
				if evento.key == K_RIGHT:
					rigthsigueapretada=True
					vx+=velocidad
				if evento.key == K_UP:
					upsigueapretada=True
					vy-=velocidad
				if evento.key == K_DOWN:
					downsigueapretada=True
					vy+=velocidad
			if evento.type == KEYUP:
				if evento.key == K_LEFT:
					leftsigueapretada=False
					if rightsigueapretada:
						vx+=velocidad
					else:	
						vx=0
				if evento.key == K_RIGHT:
					rightsigueapretada=False
					if leftsigueapretada:
						vx-=velocidad
					else:	
						vx=0
				if evento.key == K_UP:
					upsigueapretada=False
					if downsigueapretada:
						vy+=velocidad
					else:	
						vy=0
				if evento.key == K_DOWN:
					downsigueapretada=False
					if upsigueapretada:
						vy-=velocidad
					else:	
						vy=0													
		reloj.tick(20)
		t+=1
		if t>1:
			t=0	
		pantalla.fill((255,255,255))
		fondo1.update(pantalla,vx,vy)
		player1.update(pantalla,vx,vy,t)
		pygame.display.update()


main()	