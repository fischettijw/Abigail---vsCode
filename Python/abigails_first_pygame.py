# 1 https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-tutorial-movement/
# 2 https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
# 3 https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/

import pygame
import os
os.system('cls')

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Abigail's First PyGame")


x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    # pygame.time.delay(100)

    # This will loop through a list of any keyboard or mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  # If we exit the loop this will execute and close our game
