import os
import pygame
import requests


def get_response():
    global map_request, map_params, map_file
    response = requests.get(map_request, params=map_params)
    with open(map_file, "wb") as file:
        file.write(response.content)


map_request = "https://static-maps.yandex.ru/1.x/"
map_params = {"ll": '76.590577,60.945467',
              "z": 17,
              "l": "map",
              "pt": "76.590577,60.945467,pm2rdl"}
response = requests.get(map_request, params=map_params)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
pygame.display.set_caption("Карта")
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                map_params['z'] -= 1
                if map_params['z'] < 0:
                    map_params['z'] = 0
                get_response()
            if event.key == pygame.K_PAGEUP:
                map_params['z'] += 1
                if map_params['z'] > 17:
                    map_params['z'] = 17
                get_response()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
pygame.quit()
os.remove(map_file)