import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

block_size = 40

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player_x, player_y = 1, 1

finish_x, finish_y = 14, 9

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if maze[player_y][player_x - 1] == 0:
            player_x -= 1
    if keys[pygame.K_RIGHT]:
        if maze[player_y][player_x + 1] == 0:
            player_x += 1
    if keys[pygame.K_UP]:
        if maze[player_y - 1][player_x] == 0:
            player_y -= 1
    if keys[pygame.K_DOWN]:
        if maze[player_y + 1][player_x] == 0:
            player_y += 1

    if player_x == finish_x and player_y == finish_y:
        print("Победа!")
        running = False

    win.fill(WHITE)

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(win, color, (col * block_size, row * block_size, block_size, block_size))

    pygame.draw.rect(win, RED, (player_x * block_size, player_y * block_size, block_size, block_size))

    pygame.draw.rect(win, GREEN, (finish_x * block_size, finish_y * block_size, block_size, block_size))

    pygame.display.update()

    pygame.time.Clock().tick(10)
