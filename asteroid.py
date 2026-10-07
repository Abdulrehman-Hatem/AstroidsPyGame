import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255),
                    (int(self.position.x), int(self.position.y)), int(self.radius), LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update position based on velocity
        self.position += self.velocity * dt