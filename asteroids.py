import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_INCREASE, ASTEROID_WIDTH


class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_direction_angle = random.uniform(20, 50)
        new_velocity_pos_angle = self.velocity.rotate(new_direction_angle)
        new_velocity_neg_angle = self.velocity.rotate(-new_direction_angle)

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        pos_angle_asteroid = Asteroids(self.position.x, self.position.y, smaller_radius)
        negative_angle_asteroid = Asteroids(
            self.position.x, self.position.y, smaller_radius
        )

        pos_angle_asteroid.velocity = new_velocity_pos_angle * ASTEROID_SPEED_INCREASE
        negative_angle_asteroid.velocity = (
            new_velocity_neg_angle * ASTEROID_SPEED_INCREASE
        )
