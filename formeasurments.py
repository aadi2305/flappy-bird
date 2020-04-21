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
x_add = randint(30,250) 
x_add1 = randint(30,250) 

running = True
while running:
	#setting up the background which is constantly moving
	screen.blit(background,(0,0))
	screen.blit(base,(0,400))
	screen.blit(inverted_pipe, (30, -150))
	screen.blit(inverted_pipe, (288-30-52, -150))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	pygame.display.update()