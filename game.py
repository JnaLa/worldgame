import pygame
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pygame_textinput

# Initialize pygame
pygame.init()


# Get the current screen resolution
info = pygame.display.Info()
dock_height = 50
screen_width = info.current_w
screen_height = info.current_h - dock_height
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)  # Use RESIZABLE for maxing

# Game settings
pygame.display.set_caption("Guess the country")
clock = pygame.time.Clock()
textinput = pygame_textinput.TextInputVisualizer()
textinput.value = ''

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
highlighted = (255, 0, 0)

# Loading the shapefile
file_path = "maps/ne_10m_admin_0_countries.shp"
data = gpd.read_file(file_path)


def draw_map_with_highlighted():
    random_index = np.random.choice(data.index)
    random_country = data.loc[[random_index]]
    print(random_country['NAME'])

    # Create fig for base map and the highlighted country
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    data.plot(ax=ax, color='lightgray')  # Plot the base map in light gray
    random_country.plot(ax=ax, color='red')  # Highlight the selected country

    # Hiding ticks 
    ax.tick_params(axis='both', which='both', left=False, right=False, top=False, bottom=False, labelbottom=False, labelleft=False)

    # Save the highlighted country plot to an image
    image_path = "worldmap.png"
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0, dpi=100)
    plt.close(fig)

    # Load and scale image for Pygame
    world_img = pygame.image.load(image_path)
    world_map_with_highlighted = pygame.transform.scale(world_img, (screen_width, screen_height))

    return world_map_with_highlighted

def main_game_loop():
    running = True
    
    while running:
        screen.fill(white)

        events = pygame.event.get()
        
        # Feeding the input every frame
        textinput.update(events)

        # Draw everything
        screen.blit(map_with_hl, (0, 0))
        screen.blit(textinput.surface, (10, 10))

        # Poll for events
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("input so far:  {textinput.value}")


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Load the base map and highlighted country images
map_with_hl = draw_map_with_highlighted()

main_game_loop()
