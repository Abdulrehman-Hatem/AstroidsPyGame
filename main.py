import pygame,sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0.0
    updatable =pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable,asteroids)
    Shot.containers = (updatable, drawable,shots)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        
        screen.fill((0, 0, 0))  # Clear the screen with black
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return


        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_hit")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip() # Update the display
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds

if __name__ == "__main__":
    main()
