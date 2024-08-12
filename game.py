import pygame
import geopandas as gpd
import random

# Initializing pygame
pygame.init()

# loading the map
world = gpd.read_file("maps/ne_10m_admin_0_countries.shp")

# pygame setup
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guess the country")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
highlighted = (255, 0, 0)

# Game variables
country_to_guess = None
timer = 15 # seconds




def main_game_loop():
    global timer
    running = True
    

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(white)

        # render the game 

        pygame.display.flip()

        clock.tick(60)

        pygame.draw.polygon()

    pygame.quit()




