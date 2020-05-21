import pygame
import os

pygame.init()

WIDTH = 690
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite!")

current_path = os.path.dirname('Sprite!.py')
image_path = os.path.join(current_path, 'images')

raccoon = pygame.image.load(os.path.join(image_path, 'raccoon.png'))
door = pygame.image.load(os.path.join(image_path, 'door.png'))


run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, (0,128,128), (0, 0, 700, 100))
    pygame.draw.rect(screen, (0, 128, 0), (0, 100, 700, 450))
    pygame.draw.rect(screen, (0,128,128), (0, 550, 700, 100))
    screen.blit(raccoon, (300, 300))
    i = 10
    x = 200
    y = 200
    for x in range(5, 15):
        screen.blit(door, (x * 30, 210))
        screen.blit(door, (x * 30, 410))
    for y in range(21, 42):
        screen.blit(door, (150, y * 10))
        screen.blit(door, (450, y * 10))
            

    pygame.display.update()

pygame.quit()

