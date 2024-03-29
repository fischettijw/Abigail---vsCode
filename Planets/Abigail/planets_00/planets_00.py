import pygame
import os
import math
from planets_class_00 import Planet

os.system('cls')

pygame.init()

WIDTH, HEIGHT = (1300, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
Planet.WIDTH = WIDTH
Planet.HEIGHT = HEIGHT

program_title = "Newtonian Orbital Simulation of the Inner Planets"

CLOCK = pygame.time.Clock()

# create FONTS
FONT_CS_36 = pygame.font.SysFont("comicsans", 36)

# create TEXT for visible SCREEN output
title_text = FONT_CS_36.render(program_title, True, Planet.WHITE)
abigail_text = FONT_CS_36.render("By: Abigail M. Lightle", True, Planet.WHITE)

# create images for visible SCREEN output
img_background = pygame.image.load("stars.jpg").convert()

# def __init__(self, name, x,y,relative_radius,color,mass, y_vel ):
sun = Planet("Sun", 0, 0, 2.5, Planet.YELLOW, 1.98892E30, 0)
mercury = Planet("Mercury", -0.387, 0, 0.376, Planet.DARK_GRAY, 3.30e23, 47000)
venus = Planet("Venus", -0.723, 0, 0.949, Planet.WHITE, 4.87E24, 35020)
earth = Planet("Earth", -1, 0, 1.0, Planet.BLUE, 5.97E24, 29783)
mars = Planet("Mars", -1.524, 0, 0.533, Planet.RED, 6.42E23, 24077)
planets = [sun, earth, venus, mars, mercury]


fps = 60
pygame.display.set_caption(
    f"{program_title}      fps - {fps}      by Abigail M. Lightle      Science Fair 2023-2024")
ticks = 0
run = True
#################  START GAME LOOP  ###############
while run == True:
    CLOCK.tick(fps)
    ticks += 1

    # BLIT star background
    SCREEN.blit(img_background, (0, 0))

    # BLIT Text to Screen
    SCREEN.blit(title_text, (225, 5))
    SCREEN.blit(abigail_text, (915, 840))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pass

    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)
      
    pygame.display.flip()


#################  END GAME LOOP ###############
pygame.quit()
