import pygame


class Enemy:
    def __init__(self, pos):
        self.color = 'red'
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.image = pygame.image.load("enemy.jpg")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect.center = pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_hit(self, ball):
        return self.rect.colliderect(ball.rect)
