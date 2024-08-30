import pygame
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Initializing pygame
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guess the country")
clock = pygame.time.Clock()

# loading the map
file_path = "maps/ne_10m_admin_0_countries.shp"
data = gpd.read_file(file_path)
fig, ax = plt.subplots(figsize=(12.8, 7.2))
data.plot(ax=ax)
plot_image_path = "plot_image.png"
plt.savefig(plot_image_path, bbox_inches='tight', pad_inches=0, dpi=100)
plt.close(fig)

world = pygame.image.load(plot_image_path)
world = pygame.transform.scale(world, (screen_width, screen_height))




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
        screen.blit(world, (0, 0))

        # render the game 
        pygame.display.flip()

        clock.tick(60)


        
    

    pygame.quit()

    os.remove(plot_image_path)

main_game_loop()



