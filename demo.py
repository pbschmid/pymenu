# demo.py

import pygame, pymenu

BLACK = (0, 0, 0)

# set up window
WINDOWWIDTH = 500
WINDOWHEIGHT = 400

pygame.init()

def setUpMenu():
	""" How to use the PyMenu and PyButton classes. """
	# create the window
	window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption("My Game")
	# create the menu
	menu = pymenu.PyMenu(BLACK, WINDOWWIDTH, WINDOWHEIGHT)
	menu.draw(window)

if __name__ == '__main__':
	setUpMenu()

