# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    #print(f'Screen width: {SCREEN_WIDTH}')
    #print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group() #all the objects that can be updated
    drawable = pygame.sprite.Group() #all the objects that can be drawn
    asteroids = pygame.sprite.Group() #all the asteroid objects


    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    enemy_asteroids = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obs in updateable:
            obs.update(dt)

        for ass in asteroids:
            if ass.collision(my_player) == True:
                sys.exit("Game over!")
       
        screen.fill("black")
        
        for obs in drawable:
            obs.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = game_clock.tick(60)/1000
        

if __name__ == "__main__":
    main()