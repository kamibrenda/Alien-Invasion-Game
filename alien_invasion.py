import sys 

import pygame

from settings import settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullets import Bullet



def run_game():
    #initialize pygame, settings and a screen object.
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets
    bullets = Group()
    
     #set the background color
    bg_color = (230, 230, 230)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_bullets(bullets)
        ship.update()
        
        bullets.update()
        

        #get rid of bullets that have disappeared 
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    

        gf.update_screen(ai_settings, screen, ship, bullets)

        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
           
        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

# Check if the window is open by getting the surface
if pygame.display.get_surface() is None:
    print("The Pygame window is not open.")
else:
    print("The Pygame window is open.")

    pygame.display.update()

