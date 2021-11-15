import pygame, sys
from pygame.locals import *

# Variable Declaration
title = "Sequence Alignment"

# Initialize program
pygame.init()
font01 = pygame.font.Font(pygame.font.get_default_font(), 30)
font02 = pygame.font.Font(pygame.font.get_default_font(), 15)

# Assign FPS a value
FPS = 100
FramePerSec = pygame.time.Clock()
 
# Color
RED = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display
screen = pygame.display.set_mode((600,400))
screen.fill(WHITE)
pygame.display.set_caption(title)

# Functions

def message(line):
	messageDisplay = font01.render(line, True, BLACK)
	# pygame.draw.rect(screen, BLACK, (100, 400, 500, 500), 0)
	screen.blit(messageDisplay, dest=(100, 410))
	
def resetAll():
	screen.fill(WHITE)
	#pygame.draw.line(screen, YELLOW, (100, 300), (400, 300), 8)
	titleDisplay = font01.render(title, True, (255, 255, 255))
	screen.blit(titleDisplay, dest=(170,50))
	#move01 = font02.render("Computer: X", True, GREEN)
	#screen.blit(move01, dest=(393,20))
	pygame.display.update()
	
#	pygame.draw.circle(screen, RED, (column*100 + 50, row*100 + 50), 40, 10)

# Beginning Game Loop
resetAll()
# play = False
while True:
	pygame.display.update(0, 0, 400, 600)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p and start == False:
				play = True
				#message("Want to go first? Y/N")
			elif event.key == pygame.K_y and start == False and play == True:
				player = 1
				start = True
				#message("Click & take move!")
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if clickMouse(pos):
						#drawCirc(pos)
						#drawCross(cells)
			elif event.key == pygame.K_n and start == False and play == True:
				player = 0
				start = True
				#drawCross(cells)
				#message("Click & Take your move!")
			elif event.key == pygame.K_r:
				resetAll()
				#cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
				#cross = []
				#circle = []
				start = False
			elif event.key == pygame.K_e:
				pygame.quit()
				sys.exit()
		if start:
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if clickMouse(pos):
					#drawCirc(pos)
					if matchOver(circle):
						#start = False
					elif matchTie(cells):
						#start = False
					else:
						#drawCross(cells)
						if matchOver(cross):
							start = False
						elif matchTie(cells):
							start = False		
				else:
					break
	FramePerSec.tick(FPS)