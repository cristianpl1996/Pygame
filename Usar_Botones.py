import pygame, sys
from pygame.locals import *

class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x=200,y=200):
		self.imagen_normal=imagen1
		self.imagen_seleccion=imagen2
		self.imagen_actual=self.imagen_normal
		self.rect=self.imagen_actual.get_rect()
		self.rect.left,self.rect.top=x,y
	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.imagen_actual=self.imagen_seleccion
		else:
			self.imagen_actual=self.imagen_normal
		pantalla.blit(self.imagen_actual,self.rect)		

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((500,400))
	pygame.display.set_caption("Usar Botones")
	reloj = pygame.time.Clock()
	rojo=pygame.image.load("rojo.png")
	rojo2=pygame.image.load("rojo2.png")
	azul=pygame.image.load("azul.png")
	azul2=pygame.image.load("azul2.png")
	boton1=Boton(rojo,rojo2)
	boton2=Boton(azul,azul2,200,100)
	cursor1=Cursor()
	blanco=(255,255,255)
	rojo=(255,0,0)
	azul=(0,0,255)
	colordefondo=blanco

	while True:		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type==MOUSEBUTTONDOWN:
				if cursor1.colliderect(boton1.rect):
					colordefondo=rojo
				if cursor1.colliderect(boton2.rect):
					colordefondo=azul
			if evento.type==MOUSEBUTTONUP:
				colordefondo=blanco		

		reloj.tick(20)
		pantalla.fill(colordefondo)
		cursor1.update()
		boton1.update(pantalla,cursor1)
		boton2.update(pantalla,cursor1)
		pygame.display.update()

main()	