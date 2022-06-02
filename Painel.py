# colors to set screen and lines
import sys

import pygame
from pygame import gfxdraw
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

#Function to create a screen
def make_screen():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill(white)


    return screen

#function to draw coordinates lines
def coord_lines(screen):
    # grade central
    gfxdraw.line(screen, 300, 0, 300, 600, red)
    gfxdraw.line(screen, 0, 300, 600, 300, red)
    # criando linhas
    gx = 0
    while (gx < 600):
        if (gx == 300):
            gx = gx + 5
            continue
        else:
            gfxdraw.line(screen, gx, 0, gx, 600, blue)
            gfxdraw.line(screen, 0, gx, 600, gx, blue)
            gx = gx + 5
    pygame.display.flip()
#function that draw a cut area on screen
def cut_area(color,screen):
    gfxdraw.line(screen, 300, 0, 300, 600, red)
    gfxdraw.line(screen, 0, 300, 600, 300, red)
    pygame.draw.rect(screen,blue,(200,200,200,200),1)