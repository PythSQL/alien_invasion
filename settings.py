class Settings:
    """A class containing the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 10

        # Bullet settings
        self.bullet_speed = 20
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Game stats settings
        self.ship_limit = 3
        self.speedup_scale = 1.2

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale