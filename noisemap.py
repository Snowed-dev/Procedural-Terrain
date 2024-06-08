from PIL import Image
import numpy as np
from perlin_noise import PerlinNoise
import random
import pygame

pygame.init()

noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))
xpix, ypix = 500, 500
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

screen = pygame.display.set_mode ((500, 500), pygame.RESIZABLE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    def noisegen(mountaincap,thickforest,forest,plains,heavyswamp,lightswamp,ocean):
        for i, row in enumerate(pic):
            for j, column in enumerate(row):
                if column>=0.6:
                    pygame.draw.rect(screen, (500, 5000, 500), pygame.Rect(j, i, 1, 1))
                elif column>=mountaincap:
                    pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(j, i, 1, 1))                 
                elif column>=thickforest:
                    pygame.draw.rect(screen, (30, 90, 30), pygame.Rect(j, i, 1, 1))
                elif column >=forest:
                    pygame.draw.rect(screen, (10, 100, 10), pygame.Rect(j, i, 1, 1))
                elif column >=plains:
                    pygame.draw.rect(screen, (100, 150, 0), pygame.Rect(j, i, 1, 1))
                elif column >=-heavyswamp:
                    pygame.draw.rect(screen, (30, 190, 0), pygame.Rect(j, i, 1, 1))
                elif column >=-lightswamp:
                    pygame.draw.rect(screen, (40, 200, 0), pygame.Rect(j, i, 1, 1))
                
                elif column >=-ocean:
                    pygame.draw.rect(screen, (0, 0, 200), pygame.Rect(j, i, 1, 1))
    noisegen(0.2,0.09,0.009,0.002,0.06,0.02,0.1)
    pygame.display.update()

pygame.quit()
quit()
