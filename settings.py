class settings():
    """ A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Bullet settings
        self.bullet_speed_factor =1 
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60, 60, 60

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 1.5
        