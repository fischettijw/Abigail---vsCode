import pygame


class Planet():
    AU = 149.5978707E9   # meters
    G = 6.6743E-11
    SIZE_SCALE = 250/AU     # 250 pixels per AU
    TIMESTEP = 60*60*24    # 1 day in secs
    CENTER_OFFSET_X = 175
    CENTER_OFFSET_Y = 0 
    EARTH_SIZE = 20    # Relative Radius
    EARTH_VELOCITY = 29783
    WIDTH = None
    HEIGHT = None 

    def __init__(self, name, x, y, relative_radius, color, mass, y_vel):
        self.name = name
        self.x = x * Planet.AU
        self.y = y * Planet.AU

        self.radius = relative_radius * Planet.EARTH_SIZE
        self.color = color

        self.mass = mass
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel

    def draw(self, win):

        x = (self.x * Planet.SIZE_SCALE) + Planet.WIDTH/2 + Planet.CENTER_OFFSET_X
        y = (self.y * Planet.SIZE_SCALE) + Planet.HEIGHT/2 + Planet.CENTER_OFFSET_Y
        pygame.draw.circle(win, self.color, (x, y), self.radius)