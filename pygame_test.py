import pygame
import math
import random 

pygame.init()
WEIGHT = 1280.0
HEIGHT = 720.0
screen = pygame.display.set_mode((WEIGHT, HEIGHT))
clock = pygame.time.Clock()
running = True


px = WEIGHT / 2
py = HEIGHT / 2

speed = 240.0
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("Black")

    mx, my = pygame.mouse.get_pos()

    dx = mx - player_pos.x
    dy = my - player_pos.y

    angle_rad = math.atan2(dy, dx)

    pygame.draw.line(screen, "red", (player_pos.x, player_pos.y), (mx, my), 2)

    pygame.draw.circle(screen, "green", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt




    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000.0

pygame.quit()