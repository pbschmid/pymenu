pymenu
======

Pymenu is a simple menu class for Pygame.

Still in development.

Usage
-----

Simply initialize the menu, create the buttons with the pybutton class, add the buttons to the menu and draw the menu to the screen.

    # initialize the menu
    menu = pymenu.PyMenu(BLACK, WINDOWWIDTH/2, 45, "My Game")
    
    # create the buttons
    newButton = pybutton.PyButton(WINDOWWIDTH/2, 130, "New Game")
    quitButton = pybutton.PyButton(WINDOWWIDTH/2, 220, "Quit")

    # add the buttons and their actions to the menu
    menu.addButton(newButton, callback)
    menu.addButton(quitButton, callback)

    # draw the menu
    menu.draw(window)

You can find more information on how to use the class in the demo.py file.

(More documentation on how to customize the menu and buttons will follow soon.)
