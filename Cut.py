import time
from typing import Any

import pygame
from pygame import gfxdraw
import Painel
import Conversion

# the logical is the same of draw_bre function but modified to not draw outside the clipping area
def draw_cut(listt):
    screen = Painel.make_screen()
    color = Painel.black
    Painel.cut_area(color,screen)

    list2: list[Any] = []
    for x in listt:
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
        if(xlist[x]>200 and xlist[x]<400):
            if(ylist[x]>200 and ylist[x]<400):
                pygame.draw.rect(screen, color, [xlist[x] , ylist[x], 5, 5])
    pygame.display.flip()
    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()
#is the same 'draw_cut' fuction but receive five parameters(Polygon)
def draw_cut_polygon(list1, list2, list3, list4, list5):
    screen = Painel.make_screen()
    color = Painel.black
    Painel.cut_area(color, screen)
    listt1: list[Any] = []
    listt2: list[Any] = []
    listt3: list[Any] = []
    listt4: list[Any] = []
    listt5: list[Any] = []
    for x in list1:
        listt1.append(x)
    for x in list2:
        listt2.append(x)
    for x in list3:
        listt3.append(x)
    for x in list4:
        listt4.append(x)
    for x in list5:
        listt5.append(x)

    xlist1 = []
    ylist1 = []
    for x in range(len(listt1)):
        pixels = listt1[x]
        xlist1.append(pixels[0])
        ylist1.append(pixels[1])
    xlist2 = []
    ylist2 = []
    for x in range(len(listt2)):
        pixels = listt2[x]
        xlist2.append(pixels[0])
        ylist2.append(pixels[1])
    xlist3 = []
    ylist3 = []
    for x in range(len(listt3)):
        pixels = listt3[x]
        xlist3.append(pixels[0])
        ylist3.append(pixels[1])
    xlist4 = []
    ylist4 = []
    for x in range(len(listt4)):
        pixels = listt4[x]
        xlist4.append(pixels[0])
        ylist4.append(pixels[1])
    xlist5 = []
    ylist5 = []
    for x in range(len(listt5)):
        pixels = listt5[x]
        xlist5.append(pixels[0])
        ylist5.append(pixels[1])

    for x in range(len(xlist1)):
        xlist1[x],ylist1[x]=Conversion.convert(xlist1[x],ylist1[x])
        gfxdraw.pixel(screen, xlist1[x],  ylist1[x], color)
        if(xlist1[x]>200 and xlist1[x]<400):
            if(ylist1[x]>200 and ylist1[x]<400):
                pygame.draw.rect(screen, color, [xlist1[x] , ylist1[x], 5, 5])
    for x in range(len(xlist2)):
        xlist2[x],ylist2[x]=Conversion.convert(xlist2[x],ylist2[x])
        gfxdraw.pixel(screen, xlist2[x],  ylist2[x], color)
        if(xlist2[x]>200 and xlist2[x]<400):
            if(ylist2[x]>200 and ylist2[x]<400):
                pygame.draw.rect(screen, color, [xlist2[x] , ylist2[x], 5, 5])
    for x in range(len(xlist3)):
        xlist3[x],ylist3[x]=Conversion.convert(xlist3[x],ylist3[x])
        gfxdraw.pixel(screen, xlist3[x],  ylist3[x], color)
        if(xlist3[x]>200 and xlist3[x]<400):
            if(ylist3[x]>200 and ylist3[x]<400):
                pygame.draw.rect(screen, color, [xlist3[x] , ylist3[x], 5, 5])
    for x in range(len(xlist4)):
        xlist4[x],ylist4[x]=Conversion.convert(xlist4[x],ylist4[x])
        gfxdraw.pixel(screen, xlist4[x],  ylist4[x], color)
        if(xlist4[x]>200 and xlist4[x]<400):
            if(ylist4[x]>200 and ylist4[x]<400):
                pygame.draw.rect(screen, color, [xlist4[x] , ylist4[x], 5, 5])
    for x in range(len(xlist5)):
        xlist5[x],ylist5[x]=Conversion.convert(xlist5[x],ylist5[x])
        gfxdraw.pixel(screen, xlist5[x],  ylist5[x], color)
        if(xlist5[x]>200 and xlist5[x]<400):
            if(ylist5[x]>200 and ylist5[x]<400):
                pygame.draw.rect(screen, color, [xlist5[x] , ylist5[x], 5, 5])

    pygame.display.flip()

    for event in pygame.event.get():
        time.sleep(1)
        if event.type == pygame.QUIT:
            pygame.quit()



