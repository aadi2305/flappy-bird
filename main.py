import pygame
import random
from random import randint
#all the prerequisits 
pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Floppy Bird")
icon = pygame.image.load("imgs/bird1.png")
pygame.display.set_icon(icon)

#loading the images
background = pygame.image.load("imgs/bg.png")
base = pygame.image.load("imgs/base.png")
pipe = pygame.image.load("imgs/pipe.png")
inverted_pipe = pygame.image.load("imgs/inverted-pipe .png")

#all the varibles
game_status = "not over"
x_bg = 0
x_bg1 = 288
x_pipe = 0
y_pipe1 = randint(-220,-50)
y_pipe = randint(-220,-50)
x_add = randint(40+288,196+288) 
x_add1 = x_add + 230
speed = 0.5
running = True
while running:
	#setting up the background which is constantly moving
	if game_status == "not over":
		
		screen.blit(background, (x_bg,0))
		screen.blit(background,(x_bg1,0))

		screen.blit(inverted_pipe,(x_add,y_pipe1))
		screen.blit(inverted_pipe,(x_add1 ,y_pipe))

		screen.blit(pipe,(x_add,y_pipe1+320+100))
		screen.blit(pipe,(x_add1 ,y_pipe+320+100))

		screen.blit(base, (x_bg,400))
		screen.blit(base, (x_bg1,400))
		
		x_bg -= speed
		x_bg1 -= speed
		x_add -= speed
		x_add1 -= speed

		if x_add < -52:
			x_add = randint(30+288,206+288)
			y_pipe1 = randint(-220,-50)
		if x_add1 < -52:
			x_add1 = x_add + 230
			y_pipe = randint(-220,-50)
		


		if x_bg == -288:
			
			#x_add = randint(30,250)
			x_bg = 288
		if x_bg1 == -288:
			 
			x_bg1 = 288
			#x_add1 = randint(30,250)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	pygame.display.update()