# https://www.youtube.com/watch?v=WTLPmUHTPqo
# https://www.youtube.com/watch?v=zEQadiUjICY
# https://www.youtube.com/watch?v=4ycpvtIio-o
# https://www.youtube.com/watch?v=7rZgC_I9RNA
# https://www.youtube.com/watch?v=EhDtJxX0sCA

# obtained IMPORTS
import pygame
import math
# from milky_way_helper import *
import time

import os
os.system('cls')

# initial pygame and all it's components
pygame.init()

# define visual output SCREEN
WIDTH, HEIGHT = 1300, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# text for caption and SCREEN title
program_title = "Newtonian Orbital Simulation of the Inner Planets"

# create COLORS
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GRAY = (128, 128, 128)
DARK_GRAY = (80, 78, 81)
BLACK = (0, 0, 0)

# create FONTS
FONT_LST_16 = pygame.font.SysFont("Lucida Sans Typewriter", 16)
FONT_LST_18 = pygame.font.SysFont("Lucida Sans Typewriter", 18)
FONT_LST_20 = pygame.font.SysFont("Lucida Sans Typewriter", 20)
FONT_LST_22 = pygame.font.SysFont("Lucida Sans Typewriter", 22)
FONT_LST_28 = pygame.font.SysFont("Lucida Sans Typewriter", 28)
FONT_CS_36 = pygame.font.SysFont("comicsans", 36)

# create TEXT for visible SCREEN output
text_stats = FONT_LST_20.render("Distance from the Sun", True, BLACK)
text_action = FONT_LST_20.render("Action Shortcuts", True, BLACK)
text_action_up = FONT_LST_16.render("Up Arrow   - FPS up 5", True, BLACK)
text_action_down = FONT_LST_16.render("Down Arrow - FPS down 5", True, BLACK)
text_pause = FONT_LST_16.render("p          - Pause Toggle", True, BLACK)
text_delete_sun = FONT_LST_16.render("s          - Remove Sun", True, BLACK)
text_earth_delete = FONT_LST_16.render(
    "e          - Remove Earth", True, BLACK)
text_restart = FONT_LST_16.render("r          - Reset Orbits", True, BLACK)
text_scaled = FONT_LST_18.render(
    "All variables scaled accurately except visual size of the Sun and Planets ...",
    True, YELLOW)
text_abigail = FONT_CS_36.render("by Abigail Lightle", True, WHITE)
text_gravity = FONT_LST_20.render("Law of Gravitation", True, BLACK)

# create images for visible SCREEN output
img_background = pygame.image.load("stars.jpg").convert()
img_newton = pygame.image.load("Newtons_Gravity_Law.png").convert_alpha()

fps = 60
pygame.display.set_caption(
    f"{program_title} - Science Fair 2023-24 by Abigail M. Lightle")


# create Planet class
class Planet:
    AU = 149.5978707E9    # meters
    G = 6.6743E-11
    SIZE_SCALE = 250 / AU  # 250 Pixels per AU
    TIMESTEP = 3600*24  # 1 day in seconds
    CENTER_OFFSET_X = 175
    CENTER_OFFSET_Y = 0
    STOP_AFTER = 1000  # trial and error
    EARTH_SIZE = 20
    EARTH_VELOCITY = 29783

    def __init__(self, name, x, y, relative_radius, color, mass, y_vel):
        self.name = name
        self.x = x * Planet.AU
        self.y = y * Planet.AU

        self.radius = relative_radius * Planet.EARTH_SIZE
        self.color = color

        self.mass = mass

        self.orbit = []
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel

        # if self.name != "sun":
        #     self.time_per_revolution = abs(1/(self.x/Planet.AU/self.y_vel*Planet.EARTH_VELOCITY))
        #     print(self.name, self.time_per_revolution)

    def earth_years_per_revolution(self):
        if self.name != "sun":
            self.time_per_revolution = abs(
                1/(self.x/Planet.AU/self.y_vel*Planet.EARTH_VELOCITY))
            return self.name, self.time_per_revolution

    def draw(self, win):
        # draw orbits (stop after STOP_AFTER points)
        if len(self.orbit) > 1:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = (x * self.SIZE_SCALE + WIDTH / 2) + Planet.CENTER_OFFSET_X
                y = (y * self.SIZE_SCALE + HEIGHT / 2) + Planet.CENTER_OFFSET_Y

                if len(updated_points) < Planet.STOP_AFTER:
                    updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # draw Planets
        x = self.x * self.SIZE_SCALE + WIDTH / 2 + Planet.CENTER_OFFSET_X
        y = self.y * self.SIZE_SCALE + HEIGHT / 2 + Planet.CENTER_OFFSET_Y
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # Place names on Planets & Sun
        planet_text = FONT_LST_16.render(self.name, True, WHITE)
        below = 1.25 if self.name == "sun" else 2.0
        win.blit(planet_text, (x - planet_text.get_width()/2,
                               y - planet_text.get_height()/2 + below*self.radius))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.name == "sun":
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # (stop after STOP_AFTER points)
        if len(self.orbit) < Planet.STOP_AFTER:
            self.orbit.append((self.x, self.y))


def display_planet_stats(planet, x, y):
    planet_text = FONT_LST_16.render(planet.name, True, BLACK)
    SCREEN.blit(planet_text, (x + 60, 80 + y))
    pygame.draw.circle(SCREEN, planet.color, (10 + 50, 88 + y), planet.radius)

    space = " " if planet.name == "mercury" else ""
    distance_text = FONT_LST_16.render(
        f"{space}{math.floor(planet.distance_to_sun/1000)} km", True, BLACK)
    SCREEN.blit(distance_text, (x + 150, 83 + y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False


def restart():

    def average_distance(planet):
        sum = 0
        max = 0
        min = 999999999999
        for orbit in planet.orbit:
            d = math.sqrt(orbit[0]**2 + orbit[1]**2)
            max = d if d >= max else max
            min = d if d <= min else min
            sum += d
        average = sum/len(planet.orbit)
        return max, min, average

    print()
    print("="*60)

    print(
        f"Mercury: {average_distance(mercury)[1]} - {average_distance(mercury)[2]} - {average_distance(mercury)[0]}")
    print(
        f"Venus: {average_distance(venus)[1]} - {average_distance(venus)[2]} - {average_distance(venus)[0]}")
    print(
        f"Earth: {average_distance(earth)[1]} - {average_distance(earth)[2]} - {average_distance(earth)[0]}")
    print(
        f"Mars: {average_distance(mars)[1]} - {average_distance(mars)[2]} - {average_distance(mars)[0]}")

    mercury.orbit = []
    venus.orbit = []
    earth.orbit = []
    mars.orbit = []

#################################################################################
# main program start
# def __init__(self, name, x, y, relative_radius, color, mass, y_vel):


# create Plaent instances of Sun and Planets
sun = Planet("sun", 0, 0, 2.5, YELLOW, 1.98892 * 10**30, 0)

mercury = Planet("mercury", -0.387, 0, 0.376, DARK_GRAY,
                 3.30 * 10**23, 47.4 * 1000)

venus = Planet("venus", -0.723, 0, 0.949, WHITE,
               4.87 * 10**24, 35.02 * 1000)

earth = Planet("earth", -1, 0, 1.0, BLUE,
               5.97 * 10**24, 29.783 * 1000)

mars = Planet("mars", -1.524, 0, 0.533, RED,
              6.42 * 10**23, 24.077 * 1000)

planets = [sun, mercury, venus, earth, mars]


def data():
    clock.tick(fps)
    show_data = True
    while show_data:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    show_data = False

        SCREEN.fill('Red')

        text_title = FONT_CS_36.render(
            f"{program_title}\n\n           Revolutions per Earth Years", True, BLACK)

        SCREEN.blit(text_title, (200, 5))
        SCREEN.blit(text_abigail, (1000, 845))

        planet_rev = mercury.earth_years_per_revolution()
        planet_rec_text = FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, BLACK)
        SCREEN.blit(planet_rec_text, (200, 250))

        planet_rev = venus.earth_years_per_revolution()
        planet_rec_text = FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, BLACK)
        SCREEN.blit(planet_rec_text, (200, 350))

        planet_rev = earth.earth_years_per_revolution()
        planet_rec_text = FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, BLACK)
        SCREEN.blit(planet_rec_text, (200, 450))

        planet_rev = mars.earth_years_per_revolution()
        planet_rec_text = FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, BLACK)
        SCREEN.blit(planet_rec_text, (200, 550))

        pygame.display.flip()


ticks = 0
clock = pygame.time.Clock()
run = True

while run:  # START OF GAME LOOP   ################
    clock.tick(fps)
    ticks += 1

    SCREEN.blit(img_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                fps = (fps-5) if fps > 5 else fps
                pygame.display.set_caption(
                    f"{program_title} - Science Fair 2023-24 by Abigail M. Lightle")
            if event.key == pygame.K_UP:
                fps += 5
                pygame.display.set_caption(
                    f"{program_title} - Science Fair 2023-24 by Abigail M. Lightle")
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_s:
                planets.remove(sun)
                sun = None
            if event.key == pygame.K_e:
                planets.remove(earth)
                earth = None
            if event.key == pygame.K_r:
                restart()
            if event.key == pygame.K_d:
                data()

    planet_rev = 0
    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)
        # if ticks % 360 == 0:
        #     planet_rev = planet.years_per_revolution()
        #     if planet_rev != None and planet_rev[0] == 'earth':
        #         print(planet_rev[1]*(365/fps))

    text_title = FONT_CS_36.render(
        f"{program_title} ({365/fps:.3} sim-secs/year)", True, WHITE)

    SCREEN.blit(text_title, (45, 5))
    SCREEN.blit(text_abigail, (1000, 845))

    # RECTANGLE: distance from the sun
    pygame.draw.rect(SCREEN, GRAY, (30, 120, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 120, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_stats, (50, 130))
    display_planet_stats(mercury, 30, 95)
    display_planet_stats(venus, 30, 138)
    if isinstance(earth, Planet):
        display_planet_stats(earth, 30, 181)
    display_planet_stats(mars, 30, 223)

    # RECTANGLE: actions shortcuts
    pygame.draw.rect(SCREEN, GRAY, (30, 380, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 380, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_action, (85, 390))
    SCREEN.blit(text_action_up, (40, 430))
    SCREEN.blit(text_action_down, (40, 458))
    SCREEN.blit(text_pause, (40, 486))
    SCREEN.blit(text_delete_sun, (40, 514))
    SCREEN.blit(text_earth_delete, (40, 542))
    SCREEN.blit(text_restart, (40, 570))

    # RECTANGLE: law of gavitation
    pygame.draw.rect(SCREEN, GRAY, (30, 640, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 640, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(text_gravity, (65, 655))
    SCREEN.blit(img_newton, (35, 685))
    SCREEN.blit(text_scaled, (55, 872))

    # sim-earth years
    text_earth_years = FONT_LST_22.render(
        f"sim-earth years: {ticks/365:.2f}", True, YELLOW)
    SCREEN.blit(text_earth_years, (40, 55))

    # fps
    text_fps = FONT_LST_28.render(f"fps - {fps}", True, YELLOW)
    SCREEN.blit(text_fps, (105, 80))

    pygame.display.flip()

#####################   END OF GAME LOOP   #####################

pygame.quit()
