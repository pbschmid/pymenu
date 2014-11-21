# menu.py

import pygame, simplebutton, sys
from pygame.locals import *

GREY = (100, 100, 100)
WHITE = (255, 255, 255)

BACK, NEW, CHALLENGE, ABOUT = range(0,4)

class Menu(object):
	""" A class that can create and draw a simple game menu 
		with different buttons and colors, from where the
		various game modes can be accessed by mouse clicks. """

	def __init__(self, menucolor, width, height):
		""" Creates the necessary buttons and colors for a basic game menu. """
		# menu index
		self._index = 1
		self.menu_color = menucolor
		# menu buttons
		self.title_button = simplebutton.Button(width/2, 45, WHITE, self.menu_color, self.menu_color, "My great Game")
		self.back_button = simplebutton.Button(width/2, 100, WHITE, self.menu_color, GREY, "Back to Game")
		self.new_button = simplebutton.Button(width/2, 130, WHITE, self.menu_color, GREY, "New Game")
		self.challenge_button = simplebutton.Button(width/2, 160, WHITE, self.menu_color, GREY, "Challenge")
		self.about_button = simplebutton.Button(width/2, 190, WHITE, self.menu_color, GREY, "About")
		self.quit_button = simplebutton.Button(width/2, 220, WHITE, self.menu_color, GREY, "Quit")
		self.buttons = [self.back_button, self.new_button, self.challenge_button, self.about_button, self.quit_button]

		# deactivate buttons
		for button in [self.title_button, self.back_button]:
			button.set_inactive()

	def draw(self, surface):
		""" Draws the menu screen on the surface. """
		while True:
			# check for events
			self._check_events()
			# draw background
			surface.fill(self.menu_color)
			# draw buttons
			self.title_button.draw(surface)
			for button in self.buttons:
				button.draw(surface)

			# highlight buttons
			for button in self.buttons:
				if button.selected:
					button.set_highlighted()
				else:
					button.set_normal()

			# update menu
			pygame.display.update()

	def _check_events(self):
		""" Checks for pygame events. """
		for event in pygame.event.get():
			# check if player quits
			self._check_quit(event)
			# check for keyboard events
			self._check_keyboard(event)
			# check for button events
			self._check_mouse(event)

	def _check_keyboard(self, event):
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
				self._check_selection(self._index)
			# button selection
			for button in self.buttons:
				if button == self.buttons[self._index] and button.active:
					button.selected = True
				else:
					button.selected = False

	def _check_mouse(self, event):
		""" Check for mouse events. """
		# mouse motion events
		if event.type == MOUSEMOTION:
			for i in range(0, len(self.buttons)):
				if self.buttons[i].is_hovered():
					self.buttons[i].selected = True
					self._index = i
				else:
					self.buttons[i].selected = False
		# mouse click events
		if event.type == MOUSEBUTTONUP:
			for button in self.buttons:
				if button.is_hovered():
					self._check_selection(self._index)

	def _check_quit(self, event):
		""" Checks if player wants to quit. """
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	def _check_selection(self, index):
		""" Checks the selected menu index. """
		# back to game
		if index == 0:
			if self.back_button.active:
				return self._choose_mode(BACK)
		# new game
		if index == 1:
			self.back_button.set_active()
			return self._choose_mode(NEW)
		# challenge
		if index == 2:
			self.back_button.set_active()
			return self._choose_mode(CHALLENGE)
		# about
		if index == 3:
			return self._choose_mode(ABOUT)
		# quit
		if index == 4:
			pygame.quit()
			sys.exit()

	def _choose_mode(self, mode):
		""" Return the chosen game mode. """
		return mode

