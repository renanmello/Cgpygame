import sys
import time
from typing import Any
import Fill
import pygame
from pygame import gfxdraw
import Conversion
import numpy as np

import Painel
#class to draw on the screen and covert lists of objects

def ask_coord_xy():

    print("Enter x-1:")
    x1 = int(input())
    print("Enter y-1:")
    y1 = int(input())
    print("Enter x-2:")
    x2 = int(input())
    print("Enter y-2:")
    y2 = int(input())

    return x1,y1,x2,y2

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
   Input coordinates should be integers.
   The result will contain both the start and the end point.
   """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy, D
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy

#function that draw the list returned in bresenham() calculation
def Draw_bre(list):

    screen=Painel.make_screen()
    color=Painel.black
    Painel.coord_lines(screen)

    list2: list[Any] = []
    for x in list:
        list2.append(x)

    xlist=[]
    ylist=[]
    for x in range(len(list2)):
        pixels = list2[x]
        xlist.append(pixels[0])
        ylist.append(pixels[1])


    for x in range(len(xlist)):
        xlist[x],ylist[x]=Conversion.convert(xlist[x],ylist[x])
        gfxdraw.pixel(screen, xlist[x],  ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x] , ylist[x], 5, 5])
        pygame.display.flip()

        pygame.display.flip()

    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()



#class to draw a circle
def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    screen = Painel.make_screen()
    color = Painel.black
    Painel.coord_lines(screen)

    # Printing the initial point the
    # axes after translation
    print("(", x + x_centre, ", ",
          y + y_centre, ")",
          sep="", end="")
    gfxdraw.pixel(screen,x + x_centre,y + y_centre, color)
    # When radius is zero only a single
    # point be printed
    if (r > 0):
        print("(", x + x_centre, ", ",
              -y + y_centre, ")",
              sep="", end="")
        gfxdraw.pixel(screen, x + x_centre,-y + y_centre, color)
        print("(", y + x_centre, ", ",
              x + y_centre, ")",
              sep="", end="")
        gfxdraw.pixel(screen, y + x_centre, y + x_centre, color)
        print("(", -y + x_centre, ", ",
              x + y_centre, ")", sep="")
        gfxdraw.pixel(screen,-y + x_centre, -y + x_centre, color)

    # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if (x < y):
            break

        # Printing the generated point its reflection
        # in the other octants after translation
        print("(", x + x_centre, ", ", y + y_centre,
              ")", sep="", end="")
        gfxdraw.pixel(screen, x + x_centre, y + y_centre, color)
        pygame.draw.rect(screen, color, (x + x_centre, y + y_centre, 5, 5))
        print("(", -x + x_centre, ", ", y + y_centre,
              ")", sep="", end="")
        gfxdraw.pixel(screen, -x + x_centre, y + y_centre, color)
        pygame.draw.rect(screen, color,( -x + x_centre, y + y_centre, 5, 5))
        print("(", x + x_centre, ", ", -y + y_centre,
              ")", sep="", end="")
        gfxdraw.pixel(screen, x + x_centre, -y + y_centre, color)
        pygame.draw.rect(screen, color, (x + x_centre, -y + y_centre, 5, 5))
        print("(", -x + x_centre, ", ", -y + y_centre,
              ")", sep="")
        gfxdraw.pixel(screen, -x + x_centre, -y + y_centre, color)
        pygame.draw.rect(screen, color, (-x + x_centre, -y + y_centre, 5, 5))

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            print("(", y + x_centre, ", ", x + y_centre,
                  ")", sep="", end="")
            gfxdraw.pixel(screen, y + x_centre, x + y_centre, color)
            pygame.draw.rect(screen, color, (y + x_centre,x + y_centre, 5, 5))
            print("(", -y + x_centre, ", ", x + y_centre,
                  ")", sep="", end="")
            gfxdraw.pixel(screen, -y + x_centre, x + y_centre, color)
            pygame.draw.rect(screen, color, ( -y + x_centre,x + y_centre, 5, 5))
            print("(", y + x_centre, ", ", -x + y_centre,
                  ")", sep="", end="")
            gfxdraw.pixel(screen, y + x_centre, -x + y_centre, color)
            pygame.draw.rect(screen,color,(y + x_centre, -x + y_centre, 5,5))
            print("(", -y + x_centre, ", ", -x + y_centre,
                  ")", sep="")
            gfxdraw.pixel(screen, -y + x_centre, -x + y_centre,color)
            pygame.draw.rect(screen,color,(-y + x_centre, -x + y_centre, 5,5))
            pygame.display.flip()
        for event in pygame.event.get():
            time.sleep(1)
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
#bezier function calculator
def bezier(p0,p1,p2,t):

    screen = Painel.make_screen()
    color = Painel.black
    Painel.coord_lines(screen)
    for i in np.arange(0, 1, 0.01):

        px = p0[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p1[0] + p2[0] * t ** 2
        py = p0[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p1[1] + p2[1] * t ** 2
        t = t + 0.01
        px,py=Conversion.convert(px,py)
        pygame.draw.rect(screen, color, (px, py, 5, 5))
    pygame.display.flip()
    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()

#function to draw polylines on the screen
def draw_polylines(points):
    screen = Painel.make_screen()
    color = Painel.black
    Painel.coord_lines(screen)
    pygame.draw.lines(screen,color,False,points,5)
    pygame.display.flip()
    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()

#function to draw polylines using bresenham calculation
def polylines(points):
    for x in range(len(points)):
        if (x == len(points)-1):
            break
        list=bresenham(points[x][0],points[x][1],points[x+1][0],points[x+1][1])
        Draw_bre(list)
#function to fill a polygon
def polygon_fill(points):
    screen = Painel.make_screen()
    color = Painel.black
    coord = pygame.surfarray.pixels2d(screen)
    p1 = pygame.draw.polygon(screen, color, points, 2)
    Fill.flood_fill(screen,(p1.centerx, p1.centery),color)
    pygame.display.flip()
#function to draw poligon on the screen
def draw_polygon(points):
    screen = Painel.make_screen()
    color = Painel.black
    Painel.coord_lines(screen)
    #pygame.draw.polygon(screen, color, points, 5)
    polygon(points,color,screen)
    pygame.display.flip()
    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()
#function that draw a polygon on the screen and return a object polygon
def polygon(points,color,screen):

    p1=pygame.draw.polygon(screen, color, points,5)
    pygame.display.flip()
    return p1

#function to convert object list to int list
def convert_list(list):
    list2: list[Any] = []
    for x in list:
        list2.append(x)

    return list2
#function to draw the 3D polygon 'matrixp'
#the lists are the vertex's
def draw_bre2(list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12):
    screen = Painel.make_screen()
    color = Painel.black
    Painel.coord_lines(screen)
    xlist = []
    ylist = []
    for x in range(len(list1)):
        pixels = list1[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x],ylist[x]=Conversion.convert(xlist[x],ylist[x])
        gfxdraw.pixel(screen, xlist[x],  ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list2)):
        pixels = list2[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list3)):
        pixels = list3[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list4)):
        pixels = list4[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list5)):
        pixels = list5[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list6)):
        pixels = list6[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list7)):
        pixels = list7[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list8)):
        pixels = list8[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list9)):
        pixels = list9[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list10)):
        pixels = list10[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list11)):
        pixels = list11[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    xlist = []
    ylist = []
    for x in range(len(list12)):
        pixels = list12[x]
        # pixels = conversaol(pixels)
        xlist.append(pixels[0])
        ylist.append(pixels[1])
    for x in range(len(xlist)):
        xlist[x], ylist[x] = Conversion.convert(xlist[x], ylist[x])
        gfxdraw.pixel(screen, xlist[x], ylist[x], color)
        pygame.draw.rect(screen, color, [xlist[x], ylist[x], 5, 5])
    pygame.display.flip()
    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()


