import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        x = self.position[0]
        y = self.position[1]
        self.position = (x + dt, y + dt)