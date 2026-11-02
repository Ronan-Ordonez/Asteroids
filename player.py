import constants
import pygame
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.radius = constants.PLAYER_RADIUS
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)
        return
    def rotate (self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt  
        
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            #print("A")

        if keys[pygame.K_d]:
            self.rotate(dt)
            #print("D")
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        self.shoot_timer -= dt

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.math.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
