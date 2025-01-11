import pygame
import random


class Ball:
    def __init__(self, pos):
        self.color = "red"
        self.size = 35
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.speeds = [-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]
        self.dx = random.choice(self.speeds)
        self.dy = -2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size / 2)

    def reflect(self):
        self.dx = random.choice(self.speeds)
        self.dy *= -1

    def move(self, screen, platform):
        x, y = self.rect.center
        x += self.dx
        y += self.dy
        self.rect.center = x, y

        scr_width, scr_height = screen.get_size()
        if self.rect.right >= scr_width:
            self.dx = -abs(self.dx)
        elif self.rect.x <= 0:
            self.dx = abs(self.dx)
        if self.rect.y <= 0:
            self.dy = abs(self.dy)

        if self.rect.colliderect(platform.rect):
            self.dx = random.choice(self.speeds)
            self.dy = -2

    def update(self, screen, platform):
        self.draw(screen)
        self.move(screen, platform)

