pymenu
======

Pymenu is a simple menu class for Pygame.

Still in development.

Usage
-----

Simply initialize the pymenu, create buttons with the pybutton class, add the buttons to the menu and draw the menu to the screen.

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