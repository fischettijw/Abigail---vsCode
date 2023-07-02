import pygame
from planet_class import Planet
import planet_global_variables
import collections
import math


pygame.init()


def data(screen, clock, planets):
    clock.tick(60)
    show_data = True
    while show_data:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    show_data = False

        screen.fill('Red')

        text_title = Planet.FONT_CS_36.render(
            f"Newtonian Orbital Simulation of the Inner Planets\n\n           Revolutions per Earth Year", True, Planet.BLACK)
        text_abigail = Planet.FONT_CS_36.render(
            "by Abigail Lightle", True, Planet.WHITE)

        screen.blit(text_title, (200, 5))
        screen.blit(text_abigail, (1000, 845))

        planet_rev = Planet.earth_years_per_revolution(planets[1])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 250))

        planet_rev = Planet.earth_years_per_revolution(planets[2])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 350))

        planet_rev = Planet.earth_years_per_revolution(planets[3])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 450))

        planet_rev = Planet.earth_years_per_revolution(planets[4])
        planet_rec_text = Planet.FONT_CS_36.render(
            planet_rev[0] + "  " + str(planet_rev[1]), True, Planet.BLACK)
        screen.blit(planet_rec_text, (200, 550))

        img_excel_chart_01 = pygame.image.load(
            "Excel_Chart_01.png").convert_alpha()
        screen.blit(img_excel_chart_01, (25, 700))

        pygame.display.flip()


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                paused = False


def print_dts_min_avg_max(planets):
    for planet in planets:
        if planet != planets[0]:                     # != stands for not equal
            print(planet.name, len(planet.orbit))
            # print(planet.name)
            print("min", planet.dts_min)
            print("avg", planet.dts_avg)
            print('max', planet.dts_max)
            print('='*15)
        else:
            print()
            print()


def text_rectangle(screen, planets):
    # BLIT Text Rectangle (DISTANCE FROM SUN & TEXT)

    pygame.draw.rect(screen, Planet.GRAY, (30, 120, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 120, 290, 220),
                     width=3, border_radius=20)

    if len(planets) > 4:
        planets[1].display_distance_to_sun(screen, 0, 95)
        planets[2].display_distance_to_sun(screen, 0, 138)
        planets[3].display_distance_to_sun(screen, 0, 181)
        planets[4].display_distance_to_sun(screen, 0, 223)


def text_shortcuts(screen):
    # BLIT Text Rectangle (SHORTCUTS & TEXT)
    pygame.draw.rect(screen, Planet.GRAY, (30, 380, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 380, 290, 220),
                     width=3, border_radius=20)

    screen.blit(planet_global_variables.text_arrow_up, (40, 430))
    screen.blit(planet_global_variables.text_arrow_down, (40, 458))
    screen.blit(planet_global_variables.text_pause, (40, 486))
    screen.blit(planet_global_variables.text_orbit, (40, 514))
    screen.blit(planet_global_variables.text_delete_sun, (40, 542))
    screen.blit(planet_global_variables.text_reset, (40, 570))


def blit_text_to_screen(screen):
    # BLIT Text to Screen
    screen.blit(planet_global_variables.title_text, (225, 5))
    screen.blit(planet_global_variables.abigail_text, (980, 840))
    screen.blit(planet_global_variables.text_stats, (58, 130))
    screen.blit(planet_global_variables.text_shortcuts, (65, 390))
    screen.blit(planet_global_variables.text_gravity, (78, 650))


def rectabgle_law_of_gravity(screen, img):
   # RECTANGLE (Law Of Gravitation)
    pygame.draw.rect(screen, Planet.GRAY, (30, 640, 290, 220),
                     width=0, border_radius=20)
    pygame.draw.rect(screen, Planet.WHITE, (30, 640, 290, 220),
                     width=3, border_radius=20)

    screen.blit(img, (35, 685))
    screen.blit(planet_global_variables.text_scaled, (55, 872))
