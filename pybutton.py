# button.py

import pygame

class Button(object):
	""" A class that can create and draw buttons to the screen.
		They change background colors with mouseovers. """

	def __init__(self, x, y, text_color, bg_color, hover_color, text):
		""" Creates a button object and its attributes. """
		self.x, self.y = x, y
		self.text = text
		self.text_color = text_color
		self.color = bg_color
		self.bg_color = bg_color
		self.hover_color = hover_color
		self.surf = self._render_text()
		self.rect = self._create_rect()
		self.selected = True
		self.active = True

	def _render_text(self):
		""" Renders the button text to a surface. """
		font = pygame.font.SysFont("Krungthep", 20)
		surface = font.render(self.text, True, self.text_color, self.bg_color)
		return surface

	def _create_rect(self):
		""" Creates a rectangle for the text surface. """
		button_rect = self.surf.get_rect()
		button_rect.center = (self.x, self.y)
		return button_rect

	def draw(self, surface):
		""" Draws the button to a surface. """
		surface.blit(self._render_text(), self._create_rect())

	def set_active(self):
		""" Sets the button to active. """
		self.active = True

	def set_inactive(self):
		""" Sets the button to inactive. """
		self.active = False

	def set_highlighted(self):
		""" Sets a new hover bgcolor in case of a mouseover. """
		self.bg_color = self.hover_color

	def set_normal(self):
		""" Sets the bgcolor back to the normal color. """
		self.bg_color = self.color

	def is_hovered(self):
		""" Returns True if the button is hovered. """
		return self.active and self.rect.collidepoint(pygame.mouse.get_pos())

