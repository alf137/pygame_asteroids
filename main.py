import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initialize pygame
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #set screen
    clock = pygame.time.Clock() # add a clock  for time consitency
    dt = 0
    
    # make groups for readability
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()    
    #set containers
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    #creating player and Asteroids
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)  
    asteroidfield = AsteroidField()
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        for a in asteroids:
            if player.collision(a):
                sys.exit("Game Over")
        
        for a in asteroids:    
            for b in shots:
                if a.collision(b):
                    a.split()
            
            
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip() 
        dt = clock.tick(60)/1000
    
if __name__ == "__main__":
    main()