# pymenu.py

import pygame, pybutton, sys
from pygame.locals import *
from constants import *

BACK, NEW, CHALLENGE, ABOUT = range(0,4)

class PyMenu(object):
	""" A class that can create and draw a simple game menu 
		with different buttons and colors, from where the
		various game modes can be accessed by mouse clicks. """

	def __init__(self, menucolor, width, height):
		""" Creates the necessary buttons and colors for a basic game menu. """
		# menu index
		self._index = 1
		self.menucolor = menucolor
		# menu buttons
		self.titleButton = pybutton.PyButton(width/2, 45, "My Game")
		self.backButton = pybutton.PyButton(width/2, 100, "Back to Game")
		self.newButton = pybutton.PyButton(width/2, 130, "New Game")
		self.challengeButton = pybutton.PyButton(width/2, 160, "Challenge")
		self.aboutButton = pybutton.PyButton(width/2, 190, "About")
		self.quitButton = pybutton.PyButton(width/2, 220, "Quit")

		self.buttons = [self.backButton, self.newButton, self.challengeButton, self.aboutButton, self.quitButton]

		# deactivate buttons
		for button in [self.titleButton, self.backButton]:
			button.setInactive()

	def draw(self, surface):
		""" Draws the menu screen on the surface. """
		while True:
			# check for events
			self._checkEvents()
			# draw background
			surface.fill(self.menucolor)
			# draw buttons
			self.titleButton.draw(surface)
			for button in self.buttons:
				button.draw(surface)

			# highlight buttons
			for button in self.buttons:
				if button.selected:
					button.setHighlighted()
				else:
					button.setNormal()

			# update menu
			pygame.display.update()

	def _checkEvents(self):
		""" Checks for pygame events. """
		for event in pygame.event.get():
			# check if player quits
			self._checkQuit(event)
			# check for keyboard events
			self._checkKeyboard(event)
			# check for button events
			self._checkMouse(event)

	def _checkKeyboard(self, event):
		""" Check for keyboard events. """
		# keydown events
		if event.type == KEYDOWN:
			if event.key == K_UP or event.key == ord('w'):
				self._index -= 1
				if self._index < 0:
					self._index += 5
			if event.key == K_DOWN or event.key == ord('s'):
				self._index += 1
				if self._index > 4:
					self._index -= 5
			if event.key == K_RETURN:
				self._checkSelection(self._index)
			# button selection
			for button in self.buttons:
				if button == self.buttons[self._index] and button.active:
					button.selected = True
				else:
					button.selected = False

	def _checkMouse(self, event):
		""" Check for mouse events. """
		# mouse motion events
		if event.type == MOUSEMOTION:
			for i in range(0, len(self.buttons)):
				if self.buttons[i].isHovered():
					self.buttons[i].selected = True
					self._index = i
				else:
					self.buttons[i].selected = False
		# mouse click events
		if event.type == MOUSEBUTTONUP:
			for button in self.buttons:
				if button.isHovered():
					self._checkSelection(self._index)

	def _checkQuit(self, event):
		""" Checks if player wants to quit. """
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	def _checkSelection(self, index):
		""" Checks the selected menu index. """
		# back to game
		if index == 0:
			if self.backButton.active:
				return self._chooseMode(BACK)
		# new game
		if index == 1:
			self.backButton.setActive()
			return self._chooseMode(NEW)
		# challenge
		if index == 2:
			self.backButton.setActive()
			return self._chooseMode(CHALLENGE)
		# about
		if index == 3:
			return self._chooseMode(ABOUT)
		# quit
		if index == 4:
			pygame.quit()
			sys.exit()

	def _chooseMode(self, mode):
		""" Return the chosen game mode. """
		return mode

