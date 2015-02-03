# pybutton.py

import pygame
from constants import *

class PyButton(object):
  """ A class that can create and draw buttons to the screen.
    They can change background colors with mouseovers. """

  def __init__(self, x, y, text, font="Krungthep", height=20, textcolor=WHITE, bgcolor=BLACK, hovercolor=GRAY):
    """ Creates a button object and its attributes. """
    self.x, self.y = x, y
    self.font = font
    self.height = height
    self.text = text
    self.textcolor = textcolor
    self.color = bgcolor
    self.bgcolor = bgcolor
    self.hovercolor = hovercolor
    self.surf = self._renderText()
    self.rect = self._createRect()
    self.selected = True
    self.active = True

  def _renderText(self):
    """ Renders the button text to a surface. """
    font = pygame.font.SysFont(self.font, self.height)
    surface = font.render(self.text, True, self.textcolor, self.bgcolor)
    return surface

  def _createRect(self):
    """ Creates a rectangle for the text surface. """
    button_rect = self.surf.get_rect()
    button_rect.center = (self.x, self.y)
    return button_rect

  def draw(self, surface):
    """ Draws the button to a surface. """
    surface.blit(self._renderText(), self._createRect())

  def setActive(self):
    """ Sets the button to active. """
    self.active = True

  def setInactive(self):
    """ Sets the button to inactive. """
    self.active = False

  def setHighlighted(self):
    """ Sets a new hover bgcolor in case of a mouseover. """
    self.bgcolor = self.hovercolor

  def setNormal(self):
    """ Sets the bgcolor back to the normal color. """
    self.bgcolor = self.color

  def isHovered(self):
    """ Returns True if the button is hovered. """
    return self.active and self.rect.collidepoint(pygame.mouse.get_pos())
