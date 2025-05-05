import random
from circleshape import *
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width =2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_Radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_Radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_Radius)
            asteroid_1.velocity = pygame.Vector2(vector_1) * 1.2
            asteroid_2.velocity = pygame.Vector2(vector_2) * 1.2