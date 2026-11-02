import pygame
import constants
from logger import log_event
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        self.new_direction = random.uniform(20,50)
        self.vel1 = pygame.math.Vector2.rotate(self.velocity, self.new_direction)
        self.vel2 = pygame.math.Vector2.rotate(self.velocity, self.new_direction + 180)
        self.new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], self.new_radius)
        asteroid1.velocity = self.vel1 * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], self.new_radius)
        asteroid2.velocity = self.vel2 * 1.2
