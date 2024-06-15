# noisemap.py

import pygame
from perlin_noise import PerlinNoise
import random

# Define as a list or dictionary to allow global modification
terrain_parameters = {
    "mountaincap": 0.2,
    "thickforest": 0.3,
    "forest": 0.4,
    "lightforest": 0.5,
    "grassland": 0.6,
    "patchy_grassland": 0.34,
    "sand": 0.24,
    "ocean": 0
}

def noisegen(value):
    pygame.init()
    
    noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))
    xpix, ypix = 500, 500
    pic = [[noise([i/xpix, j/ypix]) + random.uniform(-0.0001, 0.0001) for j in range(xpix)] for i in range(ypix)]

    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    for i, row in enumerate(pic):
        for j, column in enumerate(row):
            if column >= 0.6:
                pygame.draw.rect(screen, (250, 250, 250), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["mountaincap"]:
                pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(j, i, 1, 1))                 
            elif column >= terrain_parameters["thickforest"]:
                pygame.draw.rect(screen, (30, 90, 30), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["forest"]:
                pygame.draw.rect(screen, (10, 100, 10), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["lightforest"]:
                pygame.draw.rect(screen, (100, 150, 0), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["grassland"]:
                pygame.draw.rect(screen, (30, 190, 0), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["patchy_grassland"]:
                pygame.draw.rect(screen, (40, 200, 0), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["sand"]:
                pygame.draw.rect(screen, (232, 232, 80), pygame.Rect(j, i, 1, 1))
            elif column >= terrain_parameters["ocean"]:
                pass

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    noisegen(0)
