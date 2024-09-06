import pygame
import sys

pygame.init()

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = win.get_size()
pygame.display.set_caption("Лабиринит")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

block_size = 100

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


background = pygame.image.load(r'C:\Users\kitaez\Desktop\sdfsd\фон.png')
wall_image = pygame.image.load(r'C:\Users\kitaez\Desktop\sdfsd\стенка4.jpg')
play_image = pygame.image.load(r'C:\Users\kitaez\Desktop\sdfsd\игрок2.png')
главное_меню = pygame.image.load(r'C:\Users\kitaez\Desktop\sdfsd\стенка.png')

def start_menu():
    while True:
        win.blit(главное_меню, (0, 0))
        font = pygame.font.SysFont(None, 55)
        title_text = font.render("лабиринт", True, RED)
        start_text = font.render("бей по Enter", True, RED)
        
        win.blit(title_text, (WIDTH // 4, HEIGHT // 4))
        win.blit(start_text, (WIDTH // 6, HEIGHT // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

start_menu()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 0:
        player_x += 1
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 0:
        player_y += 1

    if player_x == finish_x and player_y == finish_y:
        print("Победа!")
        running = False

    win.blit(background, (0, 0))

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                win.blit(wall_image, (col * block_size, row * block_size))
                win.blit(play_image, (player_x * block_size, player_y * block_size, block_size, block_size))
                

    
    pygame.draw.rect(win, GREEN, (finish_x * block_size, finish_y * block_size, block_size, block_size))

    pygame.display.update()
    pygame.time.Clock().tick(10)
