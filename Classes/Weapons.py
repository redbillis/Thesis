import pygame

class Projectile(object):       # Create a projectile class.
    def __init__(self, x, y, radius, color, face):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.face = face
        self.vel = 8 * face

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
