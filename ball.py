import pygame
import random


class Ball:
    def __init__(self, pos):
        self.color = "red"
        self.size = 35
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.speeds = [-1, -1.5, -1.25, 0, 1, 1.25, 1.5]
        print(self.speeds)
        self.dx = random.choice(self.speeds)
        self.dy = -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size / 2)

    # def move(self, screen):
    #     pass
    #
    # def update(self, screen):
    #     self.draw(screen)
    #     self.move(screen)

