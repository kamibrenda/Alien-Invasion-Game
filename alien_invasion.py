import sys 

import pygame

from settings import settings


def run_game():
    #initialize pygame, settings and a screen object.
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

     #set the background color
    bg_color = (230, 230, 230)

    #Start the main loop for the game.
    while True:

        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
       
        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

# Check if the window is open by getting the surface
if pygame.display.get_surface() is None:
    print("The Pygame window is not open.")
else:
    print("The Pygame window is open.")

    pygame.display.update()

