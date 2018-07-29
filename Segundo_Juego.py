import pygame, sys, random
from pygame.locals import *

class Recs(object):
	def __init__(self,numeroinicial):
		self.lista=[]
		for x in xrange(numeroinicial):
			leftrandom=random.randrange(2,560)
			toprandom=random.randrange(-580,-10)
			width=random.randrange(10,30)
			height=random.randrange(15,30)
			self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))	
	def reagregar(self):
		for x in xrange(len(self.lista)):
			if self.lista[x].top>482:
				leftrandom=random.randrange(2,560)
				toprandom=random.randrange(-580,-10)
				width=random.randrange(10,30)
				height=random.randrange(15,30)
				self.lista[x]=pygame.Rect(leftrandom,toprandom,width,height)				
	def mover(self):
		for rectangulo in self.lista:
			rectangulo.move_ip(0,2)			
	def pintar(self,superficie):
		for rectangulo in self.lista:
			pygame.draw.rect(superficie,(255,255,255),rectangulo)

class Player(pygame.sprite.Sprite):
	def __init__(self, imagen):
		self.imagen = imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=100,100
	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
	def update(self,superficie):
		superficie.blit(self.imagen,self.rect)	

def colison(player,recs):
	for rec in recs.lista:
		if player.rect.colliderect(rec):
			return True
	return False	

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((600,480))
	pygame.display.set_caption("Segundo Juego")
	reloj = pygame.time.Clock()
	imagen1=pygame.image.load("nave.png").convert_alpha()
	imagenexplosion=pygame.image.load("explosion.png").convert_alpha()
	imagenFondo=pygame.image.load("fondo.png").convert_alpha()
	pygame.mixer.music.load("fondo.wav")
	sonido1=pygame.mixer.Sound("explosion.wav")
	recs1=Recs(25)
	player1=Player(imagen1)
	velocidad=10
	vx,vy=0,0
	leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
	colisiono=False
	pygame.mixer.music.play(2)
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if colisiono==False:		
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
		if colison(player1,recs1):
			colisiono=True
			player1.imagen=imagenexplosion
			pygame.mixer.music.stop()
			sonido1.play()	
		if colisiono==False:
			recs1.mover()
			player1.mover(vx,vy)
					
		pantalla.blit(imagenFondo,(0,0))
		recs1.pintar(pantalla)
		player1.update(pantalla)
		pygame.display.update()
		recs1.reagregar()

main()	