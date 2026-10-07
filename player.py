import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN, PLAYER_SPEED, PLAYER_TURN_SPEED,PLAYER_SHOOT_SPEED

class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0  # in degrees
        self.cooldown = 0.0  # time until next shot can be fired


    def triangle(self) -> list[pygame.Vector2]: 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, LINE_WIDTH)

    def rotate(self,dt:float)-> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN  

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED