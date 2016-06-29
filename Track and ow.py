import pygame
import sys
import time

pygame.init()

size = width,height = 750,750
speed1 = [1,0]
speed2 = [0,-1]
speed3 = [0,1]
evergreen = (40, 181, 101)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pygamehurdle.jpg");
ball2 = pygame.image.load("our pygamestickfigure.jpeg")
ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()
ballrect.x,ballrect.y = 0,600
ballrect2.x,ballrect2.y = 350,500
lasttime = 0
lasttime2 = 0

jump=False
fall=False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if jump == False and fall == False:
					jump = True
	if jump == True:
		if ballrect2.y > 350:
			if (pygame.time.get_ticks() - lasttime2 > 3):
				ballrect2.y = ballrect2.y+(speed2[1])
				lasttime2 = pygame.time.get_ticks()
		if ballrect2.y == 350 and jump == True:
			jump = False
			fall = True
	if fall == True:
		if ballrect2.y < 500:
			if (pygame.time.get_ticks() - lasttime2 > 10):
				ballrect2.y = ballrect2.y+(speed3[1])
				lasttime2 = pygame.time.get_ticks()
		if ballrect2.y >= 500:
			fall = False	

	if (pygame.time.get_ticks() - lasttime > 5):
		ballrect = ballrect.move(speed1)
		lasttime = pygame.time.get_ticks()

	if ballrect.right == width:
		ballrect.x,ballrect.y = 0,600
	if ballrect.top <= ballrect2.bottom and ballrect.right>=ballrect2.left and (jump==True or (jump==False and fall==False)):
		if ballrect.x<500:
			evergreen = (250, 35, 35)
		if ballrect.top < 0 or ballrect.bottom > height:
			speed1[1]=-speed1[1]
		
	if ballrect2.left < 0 or ballrect2.right > width:
			speed2[0] = -speed2[0]
	if ballrect2.top < 0 or ballrect2.bottom > height:
		speed2[1]=-speed2[1]

	screen.fill(evergreen)
	screen.blit(ball,ballrect)
	screen.blit(ball2,ballrect2)	
	pygame.display.flip()
	