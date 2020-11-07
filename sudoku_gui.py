import pygame, sys
from pygame.locals import *

WIDTH = 400
HEIGHT = 300
pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku UU")

#main loop gmae
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
