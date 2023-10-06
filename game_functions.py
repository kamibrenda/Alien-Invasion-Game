import sys
import pygame
from bullets import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to Keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 ship.moving_right = True
            #check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.K_LEFT:
            ship.moving_right = True
            #check_keyup_events(event, ship)

        elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)    

def check_keydown_events(event, ai_settings, screen, ship, bullets):
        """Respond to keypresses."""
            #if event.type == pygame.KEYDOWN:
            #check_keydown_events(event, ai_settings, screen, ship, bullets)
        if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                ship.moving_left = True

def check_keyup_events(event, ship):
        """Respond to key releases"""
        if event.key ==pygame.K_RIGHT:
            ship.moving_right = False   
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    """Update the images on the screen and flip to the new screen"""

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
         bullet.draw_bullet()