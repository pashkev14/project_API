import os
import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=76.590577,60.945467&z=17&l=map&pt=76.590577,60.945467,ya_ru"
# это Яндекс.Лицей
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
