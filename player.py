import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS,PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    
    timer = 0
    
    def __init__(self,x , y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #change draw method
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), 2)
     
     # change rotations of player   
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # move the player in rotation direction
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer > 0:
            pass
        else:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
            

        
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        
        #rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # rotate right    
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # move up
        if keys[pygame.K_w]:
            self.move(dt)
        # move down
        if keys[pygame.K_s]:
            self.move(-dt)
        
        #shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        
            
            
    