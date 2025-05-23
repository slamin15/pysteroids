import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        updateable.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)



        pygame.display.flip()

        dt = clock.tick(60)
        

if __name__ == "__main__":
    main()