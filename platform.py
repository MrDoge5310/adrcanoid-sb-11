import pygame


class Platform:
    def __init__(self, pos):
        self.color = "green"
        self.width = 200
        self.rect = pygame.Rect(0, 0, self.width, 50)
        self.rect.center = pos

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0, 10)

    def update(self, screen):
        self.draw(screen)
        self.move(screen)

    def move(self, screen):
        win_width, win_height = screen.get_size()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5

        elif keys[pygame.K_RIGHT] and self.rect.right <= win_width:
            self.rect.x += 5

