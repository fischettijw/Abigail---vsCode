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
text_abigail = FONT_CS_36.render("by Abigail Lightle", True, Planet.WHITE)
text_gravity = FONT_LST_20.render("Law of Gravitation", True, Planet.BLACK)

# create images for visible SCREEN output
img_background = pygame.image.load("stars.jpg").convert()
img_newton = pygame.image.load("Newtons_Gravity_Law.png").convert_alpha()



def display_planet_stats(planet, x, y):
    planet_text = FONT_LST_16.render(planet.name, 1, Planet.BLACK)
    SCREEN.blit(planet_text, (x + 60, 80 + y))
    pygame.draw.circle(SCREEN, planet.color, (10 + 50, 88 + y), planet.radius)

    space = " " if planet.name == "mercury" else ""
    distance_text = FONT_LST_16.render(
        f"{space}{math.floor(planet.distance_to_sun/1000)} km", 1, Planet.BLACK)
    SCREEN.blit(distance_text, (x + 150, 83 + y))




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
        
    # BLIT Text to Screen
    text_title = FONT_CS_36.render(
        f"{program_title} ({365/fps:.3} sim-secs/year)", True, Planet.WHITE)

    SCREEN.blit(text_title, (45, 5))
    SCREEN.blit(text_abigail, (1000, 845))

    
    # RECTANGLE: distance from the sun
    pygame.draw.rect(SCREEN, Planet.GRAY, (30, 120, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30, 120, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_stats, (50, 130))
    display_planet_stats(mercury, 30, 95)
    display_planet_stats(venus, 30, 138)
    if isinstance(earth, Planet):
        display_planet_stats(earth, 30, 181)
    display_planet_stats(mars, 30, 223)
    
    
    # RECTANGLE: actions shortcuts
    pygame.draw.rect(SCREEN, Planet.GRAY, (30, 380, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30, 380, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_action, (85, 390))
    SCREEN.blit(text_action_up, (40, 430))
    SCREEN.blit(text_action_down, (40, 458))
    SCREEN.blit(text_pause, (40, 486))
    SCREEN.blit(text_delete_sun, (40, 514))
    SCREEN.blit(text_earth_delete, (40, 542))
    SCREEN.blit(text_restart, (40, 570))


    # RECTANGLE: law of gavitation
    pygame.draw.rect(SCREEN, Planet.GRAY, (30, 640, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30, 640, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_gravity, (65, 655))
    SCREEN.blit(img_newton, (35, 685))
    SCREEN.blit(text_scaled, (55, 872))


    pygame.display.flip()


#################  END GAME LOOP ###############
pygame.quit()
