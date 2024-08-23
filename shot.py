import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, SHOT_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt