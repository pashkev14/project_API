import os
import pygame
import requests


def draw_map(coords, mc):
    response = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={mc},{mc}&size=450,450&l=map")
    with open(map_file, "wb") as file:
        file.write(response.content)


coords = [37.677751, 55.757718]
mc = 2.0

map_file = "map.png"

draw_map(coords, mc)

pygame.init()
pygame.display.set_caption("Карта")
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT):
            x = 0
            y = 0
            if event.key == pygame.K_UP:
                y = mc
            if event.key == pygame.K_DOWN:
                y = -mc
            if event.key == pygame.K_LEFT:
                x = -mc
            if event.key == pygame.K_RIGHT:
                x = mc
            coords[0] += x
            coords[1] += y
            draw_map(coords, mc)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


pygame.quit()
os.remove(map_file)