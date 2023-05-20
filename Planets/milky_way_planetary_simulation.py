# https://www.youtube.com/watch?v=WTLPmUHTPqo

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1300, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

program_title = "Planetary Simulation of the Inner Planets"
pygame.display.set_caption(program_title)

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT_distance_to_sun_text = pygame.font.SysFont("comicsans", 16)
FONT_title_text = pygame.font.SysFont("comicsans", 28)

FPS = 60

title_text = FONT_title_text.render(f"{program_title} - {FPS} fps", True, WHITE)
print(title_text.get_rect()[2])


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SIZE_SCALE = 250 / AU  # 1AU = 100 pixels if 250
    TIMESTEP = 3600*24  # 1 day in seconds
    CENTER_OFFSET = 200
    STOP_AFTER = 900  # trial and error

    def __init__(self, name, x, y, radius, color, mass, y_vel, y_vel_change=1):
        self.name = name
        self.x = x * Planet.AU
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel * y_vel_change

    def draw(self, win):
        # draw orbits (stop after STOP_AFTER points)
        if len(self.orbit) > 1:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SIZE_SCALE + WIDTH / 2 + Planet.CENTER_OFFSET
                y = y * self.SIZE_SCALE + HEIGHT / 2

                if len(updated_points) < Planet.STOP_AFTER:
                    updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # draw Planets
        x = self.x * self.SIZE_SCALE + WIDTH / 2 + Planet.CENTER_OFFSET
        y = self.y * self.SIZE_SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # Place names and distance to sun on Planets
        if self.name != "sun":
            distance_text = FONT_distance_to_sun_text.render(
                f"{math.floor(self.distance_to_sun/1000)}km", 1, WHITE)

            win.blit(distance_text, (x - distance_text.get_width()/2,
                                     y - distance_text.get_height()/2 - 2*self.radius - 5))

            planet_text = FONT_distance_to_sun_text.render(self.name, 1, WHITE)
            win.blit(planet_text, (x - planet_text.get_width()/2,
                                   y - planet_text.get_height()/2 + 2*self.radius))

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


def main():
    run = True
    clock = pygame.time.Clock()

    # def __init__(self, name, x, y, radius, color, mass, y_vel, y_vel_change=1):

    sun = Planet("sun", 0, 0, 30, YELLOW, 1.98892 * 10**30, 0)

    mercury_y_vel_ratio = 1
    mercury = Planet("mercury", 0.387, 0, 8, DARK_GREY,
                     mercury_y_vel_ratio * 3.30 * 10**23, -47.4 * 1000, mercury_y_vel_ratio)

    venus_y_vel_ratio = 1
    venus = Planet("venus", 0.723, 0, 14, WHITE,
                   venus_y_vel_ratio*4.8685 * 10**24, -35.02 * 1000, venus_y_vel_ratio)

    earth_y_vel_ratio = 1
    earth = Planet("earth", -1, 0, 16, BLUE,
                   5.9742 * 10**24, 29.783 * 1000, earth_y_vel_ratio)

    mars_y_vel_ratio = 1
    mars = Planet("mars", -1.524, 0, 12, RED,
                  6.39 * 10**23, 24.077 * 1000, mars_y_vel_ratio)

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(FPS)
        SCREEN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(SCREEN)

        SCREEN.blit(title_text, (5, 5))
        pygame.display.flip()

    pygame.quit()


main()
