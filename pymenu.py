# pymenu.py

import pygame, pybutton, sys
from pygame.locals import *
from constants import *

class PyMenu(object):
  """ A class that can create and draw a simple game menu 
    with custom buttons and colors, from where the
    different game modes can be accessed. """

  def __init__(self, menucolor, width, height, title="My Game"):
    """ Initializes the menu title, buttons, commands, index and color. """
    # menu title, buttons and commands
    self.titleButton = pybutton.PyButton(width/2, 45, title)
    self.buttons = []
    self.commands = []

    # menu index and color
    self._index = 1
    self._maxIndex = len(self.buttons)-1
    self.menucolor = menucolor

  def draw(self, surface):
    """ Draws the menu screen to the surface. """
    while True:
      # check for events
      self._checkEvents()
      # draw background
      surface.fill(self.menucolor)
      # draw title
      self.titleButton.draw(surface)
      
      # draw buttons
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

  def addButton(self, button, command):
    """ Adds the given button to the menu. """
    self.buttons.append(button)
    self.commands.append(command)
    self._maxIndex = len(self.buttons)-1

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
          self._index += (self._maxIndex+1)
      if event.key == K_DOWN or event.key == ord('s'):
        self._index += 1
        if self._index > (self._maxIndex):
          self._index -= (self._maxIndex+1)
      if event.key == K_RETURN:
        self._runCommand(self._index) # call button action
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
      for i in range(0, (self._maxIndex+1)):
        if self.buttons[i].isHovered():
          self.buttons[i].selected = True
          self._index = i
        else:
          self.buttons[i].selected = False
    # mouse click events
    if event.type == MOUSEBUTTONUP:
      for button in self.buttons:
        if button.isHovered():
          self._runCommand(self._index) # call button action

  def _checkQuit(self, event):
    """ Checks if player wants to quit. """
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()

  def _runCommand(self, index):
    """ Calls the function corresponding to the index. """
    return self.commands[index](index)
