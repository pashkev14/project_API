import os
import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=76.590577,60.945467&z=17&l=map&pt=76.590577,60.945467,pm2rdl"
# это Яндекс.Лицей
coords = input("Введите координаты точки в формате {долгота},{широта}: ")  # для вызова стандартной точки нажмите ENTER
if coords:
    map_request = "https://static-maps.yandex.ru/1.x/"
    map_params = {"ll": coords,
                  "z": 17,
                  "l": "map",
                  "pt": f"{coords},pm2rdl"}
    response = requests.get(map_request, params=map_params)
else:
    response = requests.get(map_request)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
pygame.display.set_caption("Карта")
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
