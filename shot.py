import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255),
                    (int(self.position.x), int(self.position.y)), int(self.radius), 0)

    def update(self, dt: float) -> None:
        # Update position based on velocity
        self.position += self.velocity * dt