import pygame


class Planet():
    # AU = 149.5978707E9   # meters
    # G = 6.6743E-11
    # EARTH_SIZE = 20    # Relative Radius
    # EARTH_VELOCITY = 29783
    
    
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
        self.y = y

        self.radius = relative_radius * Planet.EARTH_SIZE
        self.color = color

        self.mass = mass

        self.orbit = []
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel        
        
        
        
        
        
        # self.name = name
        # self.x = x*Planet.AU
        # self.y = y

        # self.radius = relative_radius * Planet.EARTH_SIZE
        # self.color = color

        # self.mass = mass
        # self.distance_to_sun = 0

        # self.x_vel = 0
        # self.y_vel = y_vel

    def draw(self, win):

        # x = self.x + 650
        # y = self.y + 450
        # pygame.draw.circle(win, self.color, (x, y), self.radius)
        x = self.x * Planet.SIZE_SCALE + 1300 / 2 + Planet.CENTER_OFFSET_X
        y = self.y * Planet.SIZE_SCALE + 900 / 2 + Planet.CENTER_OFFSET_Y
        pygame.draw.circle(win, self.color, (x, y), self.radius)
