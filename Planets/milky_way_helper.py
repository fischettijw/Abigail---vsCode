import pygame
import math

WIDTH, HEIGHT = 1300, 900


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

    def years_per_revolution(self):
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

        planet_text = Planet.FONT_LST_16.render(self.name, 1, WHITE)
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

#         # (stop after STOP_AFTER points)
        if len(self.orbit) < Planet.STOP_AFTER:
            self.orbit.append((self.x, self.y))