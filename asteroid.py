import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_velocity = self.velocity.rotate(new_angle)
            second_velocity = self.velocity.rotate(-new_angle)

            baby_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            baby_asteroid_one.velocity = first_velocity * 1.2

            baby_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            baby_asteroid_two.velocity = second_velocity * 1.2
        else:
            return