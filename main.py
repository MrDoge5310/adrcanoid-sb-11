import pygame
from platform import Platform
from ball import Ball
from enemy import Enemy
from tkinter import messagebox

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

message = ""

platform = Platform((640, 650))
ball = Ball((640, 600))

enemies = []
for y in range(60, (60+60) * 3, 100):
    for x in range(60, screen.get_width()-60, 60):
        enemies.append(Enemy((x, y)))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    platform.update(screen)
    ball.update(screen, platform)
    for enemy in enemies:
        enemy.draw(screen)
        if enemy.check_hit(ball):
            enemies.remove(enemy)
            ball.reflect()
            break

    if ball.rect.y > screen.get_height():
        message = "You Loose!"
        running = False
    elif len(enemies) == 0:
        message = "You Win"
        running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

messagebox.showinfo('GameOver', message)
pygame.quit()
