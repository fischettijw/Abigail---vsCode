# https://www.youtube.com/watch?v=WTLPmUHTPqo
# https://www.youtube.com/watch?v=zEQadiUjICY
# https://www.youtube.com/watch?v=4ycpvtIio-o

import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 1300, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

program_title = "Newtonian Orbital Simulation of the Inner Planets"


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GRAY = (128, 128, 128)
DARK_GRAY = (80, 78, 81)
BLACK = (0, 0, 0)

FONT_distance_to_sun_text = pygame.font.SysFont("Lucida Sans Typewriter", 16)
FONT_scaled_text = pygame.font.SysFont("Lucida Sans Typewriter", 18)
FONT_title_text = pygame.font.SysFont("comicsans", 36)

FONT_distance_to_sun_text_stat = pygame.font.SysFont(
    "Lucida Sans Typewriter", 20)
stats_title = "Distance from the Sun"
title_text_stat = FONT_distance_to_sun_text_stat.render(stats_title, 1, BLACK)

action_title = "Action Shortcuts"
action_text = FONT_distance_to_sun_text_stat.render(action_title, 1, BLACK)
action_up = "Up Arrow   - FPS up 5"
action_up_text = FONT_distance_to_sun_text.render(action_up, 1, BLACK)
action_down = "Down Arrow - FPS down 5"
action_down_text = FONT_distance_to_sun_text.render(action_down, 1, BLACK)
pause = "p          - Pause Toggle"
pause_text = FONT_distance_to_sun_text.render(pause, 1, BLACK)
delete_sun = "s          - Remove Sun"
delete_sun_text = FONT_distance_to_sun_text.render(delete_sun, 1, BLACK)
delete_earth = "e          - Remove Earth"
delete_earth_text = FONT_distance_to_sun_text.render(delete_earth, 1, BLACK)
restart = "r          - Reset Orbits"
restart_text = FONT_distance_to_sun_text.render(restart, 1, BLACK)
scaled = "All variables scaled accurately except visual size of the Sun and Planets ..."
scaled_text = FONT_scaled_text.render(scaled, 1, YELLOW)

abigail = "by Abigail Lightle"
abigail_text = FONT_title_text.render(abigail, 1, WHITE)

law_of_gravity = "Law of Gravitation"
gravity_text = FONT_distance_to_sun_text_stat.render(
    law_of_gravity, 1, BLACK)

background = pygame.image.load("stars.jpg").convert()
newton = pygame.image.load("Newtons_Gravity_Law.png").convert_alpha()


fps = 60
pygame.display.set_caption(f"{program_title} - {fps} fps")


class Planet:
    AU = 149.6e6 * 1000    # meters
    G = 6.67428e-11
    SIZE_SCALE = 250 / AU  # 250 Pixels per AU
    TIMESTEP = 3600*24  # 1 day in seconds
    CENTER_OFFSET = 175
    STOP_AFTER = 1000  # trial and error

    def __init__(self, name, x, y, radius, color, mass, y_vel, y_vel_change=1):
        self.name = name
        self.x = x * Planet.AU
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.xx = []
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel * y_vel_change

    def draw(self, win):
        # draw orbits (stop after STOP_AFTER points)
        if len(self.orbit) > 1:
            updated_points = []
            self.xx = []
            for point in self.orbit:
                x, y = point
                x = (x * self.SIZE_SCALE + WIDTH / 2) + Planet.CENTER_OFFSET
                y = (y * self.SIZE_SCALE + HEIGHT / 2)

                if len(updated_points) < Planet.STOP_AFTER:
                    updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # draw Planets
        x = self.x * self.SIZE_SCALE + WIDTH / 2 + Planet.CENTER_OFFSET
        # if self.name == "earth":
        #     print(x)
        y = self.y * self.SIZE_SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # Place names on sun and Planets

        planet_text = FONT_distance_to_sun_text.render(self.name, 1, WHITE)
        win.blit(planet_text, (x - planet_text.get_width()/2,
                               y - planet_text.get_height()/2 + 2*self.radius))

        # if self.name != "sun":
        #     planet_text = FONT_distance_to_sun_text.render(self.name, 1, WHITE)
        #     win.blit(planet_text, (x - planet_text.get_width()/2,
        #                            y - planet_text.get_height()/2 + 2*self.radius))

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
    planet_text = FONT_distance_to_sun_text.render(planet.name, 1, BLACK)
    SCREEN.blit(planet_text, (x + 60, 80 + y))
    pygame.draw.circle(SCREEN, planet.color, (10 + 50, 88 + y), planet.radius)

    space = " " if planet.name == "mercury" else ""
    distance_text = FONT_distance_to_sun_text.render(
        f"{space}{math.floor(planet.distance_to_sun/1000)} km", 1, BLACK)
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

    def average_distance(plant):
        sum = 0
        max = 0
        min = 999999999999
        for orbit in plant.orbit:
            d = math.sqrt(orbit[0]**2 + orbit[1]**2)
            max = d if d >= max else max
            min = d if d <= min else min
            sum += d
        average = sum/len(plant.orbit)
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


# main program start   ======================================================
run = True
clock = pygame.time.Clock()

# def __init__(self, name, x, y, radius, color, mass, y_vel, y_vel_change=1):

sun = Planet("sun", 0, 0, 50, YELLOW, 1.98892 * 10**30, 0)

mercury_y_vel_ratio = 1
mercury = Planet("mercury", -0.387, 0, 8, DARK_GRAY,
                 3.30 * 10**23, 47.4 * 1000, mercury_y_vel_ratio)

venus_y_vel_ratio = 1
venus = Planet("venus", -0.723, 0, 14, WHITE,
               4.87 * 10**24, 35.02 * 1000, venus_y_vel_ratio)

earth_y_vel_ratio = 1
earth = Planet("earth", -1, 0, 16, BLUE,
               5.97 * 10**24, 29.783 * 1000, earth_y_vel_ratio)

mars_y_vel_ratio = 1
mars = Planet("mars", -1.524, 0, 12, RED,
              6.42 * 10**23, 24.077 * 1000, mars_y_vel_ratio)

planets = [sun, mercury, venus, earth, mars]

ticks = 0
while run:
    clock.tick(fps)
    # SCREEN.fill((0, 0, 0))
    SCREEN.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                fps = (fps-5) if fps > 5 else fps
                pygame.display.set_caption(f"{program_title} - {fps} fps")
            if event.key == pygame.K_UP:
                fps += 5
                pygame.display.set_caption(f"{program_title} - {fps} fps")
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

    for planet in planets:
        planet.update_position(planets)
        planet.draw(SCREEN)

    title_text = FONT_title_text.render(
        f"{program_title} ({365/fps:.3} sim-sec/year)", True, WHITE)

    SCREEN.blit(title_text, (45, 5))

    pygame.draw.rect(SCREEN, GRAY, (30, 120, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 120, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(title_text_stat, (50, 130))
    display_planet_stats(mercury, 30, 100)
    display_planet_stats(venus, 30, 140)
    if isinstance(earth, Planet):
        display_planet_stats(earth, 30, 180)
    display_planet_stats(mars, 30, 220)

    pygame.draw.rect(SCREEN, GRAY, (30, 380, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 380, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(action_text, (85, 390))
    SCREEN.blit(action_up_text, (40, 430))
    SCREEN.blit(action_down_text, (40, 458))
    SCREEN.blit(pause_text, (40, 486))
    SCREEN.blit(delete_sun_text, (40, 514))
    SCREEN.blit(delete_earth_text, (40, 542))
    SCREEN.blit(restart_text, (40, 570))

    SCREEN.blit(abigail_text, (1000, 850))

    pygame.draw.rect(SCREEN, GRAY, (30, 640, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(SCREEN, WHITE, (30, 640, 290, 220),
                     width=3, border_radius=20)
    SCREEN.blit(gravity_text, (65, 655))
    SCREEN.blit(newton, (35, 685))
    SCREEN.blit(scaled_text, (55, 872))

    pygame.display.flip()

pygame.quit()


# main()
