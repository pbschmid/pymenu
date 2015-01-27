# demo.py

import pygame, pybutton, pymenu
from constants import *

# set up window
WINDOWWIDTH = 500
WINDOWHEIGHT = 400

pygame.init()

def doSomething(something):
	print something

def setUpMenu():
	""" How to use the PyMenu and PyButton classes. """

	# create the window
	window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption("My Game")
	
	# initialize the menu
	menu = pymenu.PyMenu(BLACK, WINDOWWIDTH, WINDOWHEIGHT)
	
	# create buttons
	backButton = pybutton.PyButton(WINDOWWIDTH/2, 100, "Back to Game")
	newButton = pybutton.PyButton(WINDOWWIDTH/2, 130, "New Game")
	challengeButton = pybutton.PyButton(WINDOWWIDTH/2, 160, "Challenge")
	aboutButton = pybutton.PyButton(WINDOWWIDTH/2, 190, "About")
	quitButton = pybutton.PyButton(WINDOWWIDTH/2, 220, "Quit")

	# add buttons to menu
	menu.addButton(backButton, doSomething("Back to Game"))
	menu.addButton(newButton, doSomething("New Game"))
	menu.addButton(challengeButton, doSomething("Challenge"))
	menu.addButton(aboutButton, doSomething("About"))
	menu.addButton(quitButton, doSomething("Quit"))

	# draw menu
	menu.draw(window)


if __name__ == '__main__':
	setUpMenu()

