# Snippet Generator
# https://snippet-generator.app/

# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import os
from Pygame_Helper_Functions import *
import collections

# Clear Terminal
os.system("cls")

# Screen Size
screen_width = 1024
screen_height = 768
screen_size = (screen_width, screen_height)

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('My Pygame Window Caption')

fps_Clock = pygame.time.Clock()
fps = 30

circle_color = RED

# Game Loop
running_average = collections.deque(maxlen=10)
done = False
while done == False:
    # FPS Clock
    FPS = fps_Clock.tick(fps)
    
    running_average.append(FPS)
    print(int(sum(running_average)/len(running_average)))
    
    
    
    
    screen.fill(CYAN)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle_color = random_color()

    # Drawing/Game Code
    # circle(surface, color, center, radius, width)
    pygame.draw.circle(screen, circle_color, (300, 250), 100, 0) 

    # FLIP (update) Screen
    pygame.display.flip()

print('#'*30)
for i in running_average:
    print(i)
    
pygame.quit()