import pygame
from asteroidfield import AsteroidField
from asteroids import Asteroids
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
import shot


def main():
    MAX_FPS = 60
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for object in updatable:
            object.update(dt)
            for asteroid in asteroids:
                if asteroid.isColliding(player):
                    print("Game over!")
                    exit()

                for bullet in shots:
                    if asteroid.isColliding(bullet):
                        asteroid.split()
                        bullet.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limits framerate to MAX_FPS
        dt = clock.tick(MAX_FPS) / 1000  # converts from milliseconds to seconds


if __name__ == "__main__":
    main()
