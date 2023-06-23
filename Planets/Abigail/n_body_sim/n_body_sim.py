# https://youtu.be/7rZgC_I9RNA

import random
import itertools
import math
import pygame
import sys
import os
os.system('cls')

G = 0.25
# random.seed(10)

pygame.init()
WINDOWS_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOWS_SIZE)
CLOCK = pygame.time.Clock()

BACKGROUND = pygame.Surface(WINDOWS_SIZE)
BACKGROUND.fill("Black")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(500, 500))

fps = 60
BODY_COUNT = 50
radius_mult = 2
sun_mass = 20


class Body(pygame.sprite.Sprite):
    def __init__(self, mass, radius, start_position, color, x_vel, y_vel):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((2*radius, 2*radius))
        # self.image = pygame.Surface(radius*2, radius*2)
        self.image.fill("Black")
        self.rect = self.image.get_rect(center=start_position)

        self.mass = mass
        self.radius = radius
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]
        self.color = color

        self.x_vel = x_vel
        self.x_acc = 0
        self.y_vel = y_vel
        self.y_acc = 0
        
        pygame.draw.circle(self.image, color, (radius, radius), radius)

    def set_x_vel(self, vel):
        self.x_vel = vel

    def set_y_vel(self, vel):
        self.y_vel = vel

    def set_x_acc(self, acc):
        self.x_acc = acc

    def set_y_acc(self, acc):
        self.y_acc = acc

    def change_x_pos(self, value):
        self.x_pos += value

    def change_y_pos(self, value):
        self.y_pos += value

    def change_x_vel(self, value):
        self.x_vel += value

    def change_y_vel(self, value):
        self.y_vel += value

    def update_pos(self):
        self.rect.center = (round(self.x_pos), round(self.y_pos))

    def animate(self):
        
        if self.color != "Yellow":
            self.change_x_vel(self.x_acc)
            self.change_y_vel(self.y_acc)

            self.change_x_pos(self.x_vel)
            self.change_y_pos(self.y_vel)

            self.update_pos()

    def gravitate(self, otherbody):
        dx = abs(self.x_pos - otherbody.x_pos)
        dy = abs(self.y_pos - otherbody.y_pos)
        
        if dx<self.radius*radius_mult and dy<self.radius*radius_mult:
            pass
        else:
            try:
                r = math.sqrt(dx**2 + dy**2)
                a = G * otherbody.mass/r**2
                theta = math.asin(dy/r)
                         
                if self.x_pos > otherbody.x_pos:
                    self.set_x_acc(-math.sin(theta)*a)
                else:
                    self.set_x_acc(math.sin(theta)*a)

                if self.y_pos > otherbody.y_pos:
                    self.set_y_acc(-math.cos(theta)*a)
                else:
                    self.set_y_acc(math.cos(theta)*a)
            except ZeroDivisionError:
                pass
        


body_group = pygame.sprite.Group()

# body_group.add(Body(1,3,(300,300), "White", 0,0))
# body_group.add(Body(1,3,(700,300), "White", 0,0))
# body_group.add(Body(1,3,(300,700), "White", 0,0))
# body_group.add(Body(1,3,(700,700), "White", 0,0))


body_group.add(Body(sun_mass,10,(500,500), "Yellow", 0, 0))  # SUN
for n in range(BODY_COUNT):
    # def __init__(self, mass, radius, start_position, color, x_vel, y_vel):
    body_group.add(Body(1,3,(random.randrange(100,900),random.randrange(100,900)),"White", 0,0))
    
body_list = list(body_group)
body_pairs = list(itertools.combinations(body_list,2))


while True:
    CLOCK.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(BACKGROUND, BACKGROUND_RECT)
    
    body_group.draw(screen)
    
    for body, otherbody in body_pairs:
        body.gravitate(otherbody)
        otherbody.gravitate(body)
        body.animate()
        otherbody.animate()
        
        

    pygame.display.flip()
