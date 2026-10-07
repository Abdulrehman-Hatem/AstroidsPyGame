import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255),
                    (int(self.position.x), int(self.position.y)), int(self.radius), LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update position based on velocity
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < 2 * ASTEROID_MIN_RADIUS:
            return  # too small to split

        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        size = self.radius - ASTEROID_MIN_RADIUS

        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        asteroid1 = Asteroid(self.position.x, self.position.y, size)
        asteroid1.velocity = vel1*1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, size)
        asteroid2.velocity = vel2*1.2

