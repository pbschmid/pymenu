# demo.py

import pygame, simplemenu

BLACK = (0, 0, 0)

# set up window
WINDOWWIDTH = 500
WINDOWHEIGHT = 400

pygame.init()

def setUpMenu():
	""" Example how to use the simplemenu and simplebutton classes. """
	# create the window
	window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption("My Game")
	# create the menu
	menu = simplemenu.Menu(BLACK, WINDOWWIDTH, WINDOWHEIGHT)
	menu.draw(window)

if __name__ == '__main__':
	setUpMenu()

