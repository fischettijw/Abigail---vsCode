import pygame
import os
import math
from planets_class_01 import Planet

os.system('cls')

pygame.init()

WIDTH, HEIGHT = (1300, 900)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
Planet.WIDTH = WIDTH
Planet.HEIGHT = HEIGHT


program_title = "Newtonian Orbital Simulation of the Inner Planets"
background = pygame.image.load("stars.jpg").convert()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# GRAY = (128, 128, 128)
# DARK_GRAY = (80, 80, 80)
# YELLOW = (255, 255, 0)


CLOCK = pygame.time.Clock()


# create FONTS
FONT_LST_16 = pygame.font.SysFont("Lucida Sans Typewriter", 16)
FONT_LST_18 = pygame.font.SysFont("Lucida Sans Typewriter", 18)
FONT_LST_20 = pygame.font.SysFont("Lucida Sans Typewriter", 20)
FONT_LST_22 = pygame.font.SysFont("Lucida Sans Typewriter", 22)
FONT_LST_28 = pygame.font.SysFont("Lucida Sans Typewriter", 28)
FONT_CS_36 = pygame.font.SysFont("comicsans", 36)

# create TEXT for visible SCREEN output
title_text = FONT_CS_36.render(program_title, True, Planet.WHITE)
abigail_text = FONT_CS_36.render("By: Abigail M. Lightle", True, Planet.WHITE)
text_stats = FONT_LST_20.render("Distance from the Sun", True, Planet.BLACK)
text_action = FONT_LST_20.render("Action Shortcuts", True, Planet.BLACK)
text_action_up = FONT_LST_16.render(
    "Up Arrow   - FPS up 5", True, Planet.BLACK)
text_action_down = FONT_LST_16.render(
    "Down Arrow - FPS down 5", True, Planet.BLACK)
text_pause = FONT_LST_16.render(
    "p          - Pause Toggle", True, Planet.BLACK)
text_delete_sun = FONT_LST_16.render(
    "s          - Remove Sun", True, Planet.BLACK)
text_earth_delete = FONT_LST_16.render(
    "e          - Remove Earth", True, Planet. BLACK)
text_restart = FONT_LST_16.render(
    "r          - Reset Orbits", True, Planet.BLACK)
text_scaled = FONT_LST_18.render(
    "All variables scaled accurately except visual size of the Sun and Planets ...",
    True, Planet.YELLOW)

# create images for visible SCREEN output
img_background = pygame.image.load("stars.jpg").convert()
img_newton = pygame.image.load("Newtons_Gravity_Law.png").convert_alpha()


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
        planet.draw(SCREEN)

    planet_rev = 0
    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)
        

    pygame.display.flip()


#################  END GAME LOOP ###############
pygame.quit()
