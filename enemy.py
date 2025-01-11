import pygame


class Enemy:
    def __init__(self, pos):
        self.color = 'red'
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_hit(self, ball):
        return self.rect.colliderect(ball.rect)
