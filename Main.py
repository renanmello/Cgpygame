import random
import sys
import time
import numpy as np
import pygame
from pygame import gfxdraw
import Conversion
import Cut
import Fill
import Projections
import Draw
import Screens
import Transform
#Main Class
#Function to show Principal Options
import Transform

while(True):
    op = Screens.opPrincipal()
    if (op == 1):
        x1, y1, x2, y2 = Draw.ask_coord_xy()
        list = Draw.bresenham(x1, y1, x2, y2)
        Draw.Draw_bre(list)

    if (op == 2):
        xmd = int(input("Enter x."))
        ymd = int(input("Enter y."))
        r = int(input("Enter radius."))
        xmd, ymd = Conversion.convert(xmd, ymd)
        Draw.midPointCircleDraw(xmd, ymd, r)

    if (op == 3):
        x1, y1, x2, y2 = Draw.ask_coord_xy()
        p0= x1,y1
        p2 = x2, y2
        pc1=int(input("Control point 1"))
        pc2=int(input("Control point 2"))
        p1= pc1,pc2
        t = 0
        Draw.bezier(p0, p1, p2, t)

    if (op == 4):
        points=[]
        count=int(input("How many points? n>3"))
        for i in range(count):
            x=int(input("Enter x-"+str(i)+"."))
            y=int(input("Enter y-"+str(i)+"."))
            points.append([x,y])
        Draw.draw_polylines(Conversion.convert_l(points))

    if (op == 5):
        n = int(input("how many sides of the polygon? n>=3"))
        points = []
        for i in range(n):
            x = int(input("Enter x-" + str(i)))
            y = int(input("Enter y-" + str(i)))
            points.append([x, y])
        points = Conversion.convert_l(points)
        Draw.polygon_fill(points)

    if (op == 7):
        x1, y1, x2, y2 = Draw.ask_coord_xy()
        list = Draw.bresenham(x1, y1, x2, y2)
        Cut.draw_cut(list)

    if (op == 8):
        print("Polygon n=5")
        x1 = int(input("Enter x1."))
        y1 = int(input("Enter y1."))
        x2 = int(input("Enter x2."))
        y2 = int(input("Enter y2."))
        x3 = int(input("Enter x3."))
        y3 = int(input("Enter y3."))
        x4 = int(input("Enter x4."))
        y4 = int(input("Enter y4."))
        x5 = int(input("Enter x5."))
        y5 = int(input("Enter y5."))
        list1 = Draw.bresenham(x1, y1, x2, y2)
        list2 = Draw.bresenham(x2, y2, x3, y3)
        list3 = Draw.bresenham(x3, y3, x4, y4)
        list4 = Draw.bresenham(x4, y4, x5, y5)
        list5 = Draw.bresenham(x5, y5, x1, y1)
        Cut.draw_cut_polygon(list1, list2, list3, list4, list5)

    if (op == 9):

        n = int(input("how many sides of the polygon? n>=3" ))
        points = []
        points2 = []
        s = int(input("Type scale..(int) "))
        for i in range(n):
            x = int(input("Enter x-"+str(i)))
            y = int(input("Enter y-"+str(i)))
            points.append([x,y])
            points2.append(Transform.scale(x,y,s))
        Draw.draw_polygon(Conversion.convert_l(points))
        Draw.draw_polygon((Conversion.convert_l(points2)))

    if (op == 10):
        n = int(input("how many sides of the polygon? n>=3"))
        points = []
        points2 = []
        pivot_index=None
        rot = int(input("Enter Rotation angle in degrees."))

        for i in range(n):
            x = int(input("Enter x-" + str(i)))
            y = int(input("Enter y-" + str(i)))
            points.append([x, y])

            if(pivot_index==None):
                answer = int(input("Pivot point?? yes>>1 no>>2"))
                if(answer==1):
                    pivot_index=i
                    points2.append([x,y])
                    print("pivot agree")
            points2.append(Transform.rotation(x, y, rot))
        Draw.draw_polygon(Conversion.convert_l(points))
        Draw.draw_polygon(Conversion.convert_l(points2))

    if (op == 11):
        n = int(input("how many sides of the polygon? n>=3"))
        points = []
        points2 = []
        for i in range(n):
            x = int(input("Enter x-" + str(i)))
            y = int(input("Enter y-" + str(i)))
            points.append([x, y])
        new_x = int(input("Enter new x point"))
        new_y = int(input("Enter new y point"))
        for x in range(len(points)):
            points2.append(Transform.traslate(points[x][0],points[x][1],new_x,new_y))
        Draw.draw_polygon(Conversion.convert_l(points))
        Draw.draw_polygon(Conversion.convert_l(points2))

    if (op == 12):

        matrixp = [[0, 50, 50, 0, 0, 50, 50, 0],
                   [0, 0, 25, 25, 0, 0, 50, 50],
                   [50, 50, 50, 50, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]]
        print("Matrix Points ", matrixp)
        pointsx = []
        pointsy = []
        points = []

        for i in range(len(matrixp[0])):
            pointsx.append(matrixp[0][i])
        for i in range(len(matrixp[1])):
            pointsy.append(matrixp[1][i])
        for i in range(len(pointsx)):
            points.append([pointsx[i], pointsy[i]])
        Draw.draw_polygon(Conversion.convert_l(points))
    if (op == 13):

        matrixp = [[0, 50, 50, 0, 0, 50, 50, 0],
                   [0, 0, 25, 25, 0, 0, 50, 50],
                   [50, 50, 50, 50, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]]
        print("Matrix Points ", matrixp)
        pointsz = []
        pointsy = []
        points = []

        for i in range(len(matrixp[2])):
            pointsz.append(matrixp[2][i])
        for i in range(len(matrixp[1])):
            pointsy.append(matrixp[1][i])
        #for i in range(len(pointsz)):
        #    points.append([pointsz[i], pointsy[i]])
        points=[[pointsz[0],pointsy[0]], [pointsz[2],pointsy[2]],
                      [pointsz[6],pointsy[6]],[pointsz[4],pointsy[4]]]
        Draw.draw_polygon(Conversion.convert_l(points))
    if (op == 14):

        matrixp = [[0, 50, 50, 0, 0, 50, 50, 0],
                   [0, 0, 25, 25, 0, 0, 50, 50],
                   [50, 50, 50, 50, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]]
        print("Matrix Points ", matrixp)
        pointsx = []
        pointsy = []
        points = []

        for i in range(len(matrixp[0])):
            pointsx.append(matrixp[0][i])
        for i in range(len(matrixp[1])):
            pointsy.append(matrixp[1][i])
        points=[[pointsx[0],pointsy[0]],[pointsx[1],pointsy[1]],[pointsx[6],pointsy[6]],[pointsx[7],pointsy[7]]]

        Draw.draw_polygon(Conversion.convert_l(points))
    if (op == 15):

        matrixp = [[0, 50, 50, 0, 0, 50, 50, 0],
                   [0, 0, 25, 25, 0, 0, 50, 50],
                   [50, 50, 50, 50, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]]
        print("Matrix Points ", matrixp)
        pointsx = []
        pointsz = []
        points = []

        for i in range(len(matrixp[0])):
            pointsx.append(matrixp[0][i])
        for i in range(len(matrixp[2])):
            pointsz.append(matrixp[2][i])
        points=[[pointsx[7],pointsz[7]],[pointsx[3],pointsz[3]],[pointsx[6],pointsz[6]],[pointsx[7],pointsz[7]]]
        Draw.draw_polygon(Conversion.convert_l(points))

    if (op == 16):
        matrixp = [[0, 50, 50, 0, 0, 50, 50, 0],
                   [0, 0, 25, 25, 0, 0, 50, 50],
                   [50, 50, 50, 50, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]]
        print("polygon 3D matrix points:", matrixp)

        matrixrx = [[0.71, 0, 0.71, 0],
                    [0, 1, 0, 0],
                    [-0.71, 0, 0.71, 0],
                    [0, 0, 0, 1]]

        matrixry = [[1, 0, 0, 0],
                    [0, 0.82, -0.58, 0],
                    [0, 0.58, 0.82, 0],
                    [0, 0, 0, 1]]

        matrixrz = [[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 1]]
        pt = Projections.mult_m(matrixp, matrixrx, matrixry, matrixrz)

        # A-B vertex
        line1 = Draw.bresenham(int(pt[0][0]), int(pt[1][0]), int(pt[0][1]), int(pt[1][1]))
        n_line1=Draw.convert_list(line1)

        # B-C vertex
        line2 = Draw.bresenham(int(pt[0][1]), int(pt[1][1]), int(pt[0][2]), int(pt[1][2]))
        n_line2 = Draw.convert_list(line2)

        # C-D vertex
        line3 = Draw.bresenham(int(pt[0][2]), int(pt[1][2]), int(pt[0][3]), int(pt[1][3]))
        n_line3 = Draw.convert_list(line3)

        # D-A vertex
        line4 = Draw.bresenham(int(pt[0][3]), int(pt[1][3]), int(pt[0][0]), int(pt[1][0]))
        n_line4=Draw.convert_list(line4)
        # E-F vertex
        line5 = Draw.bresenham(int(pt[0][4]), int(pt[1][4]), int(pt[0][5]), int(pt[1][5]))
        n_line5=Draw.convert_list(line5)
        # F-G vertex
        line6 = Draw.bresenham(int(pt[0][5]), int(pt[1][5]), int(pt[0][6]), int(pt[1][6]))
        n_line6=Draw.convert_list(line6)
        # G-H vertex
        line7 = Draw.bresenham(int(pt[0][6]), int(pt[1][6]), int(pt[0][7]), int(pt[1][7]))
        n_line7=Draw.convert_list(line7)
        # H-E vertex
        line8 = Draw.bresenham(int(pt[0][7]), int(pt[1][7]), int(pt[0][4]), int(pt[1][4]))
        n_line8=Draw.convert_list(line8)
        # C-G vertex
        line9 = Draw.bresenham(int(pt[0][2]), int(pt[1][2]), int(pt[0][6]), int(pt[1][6]))
        n_line9=Draw.convert_list(line9)
        # B-F vertex
        line10 = Draw.bresenham(int(pt[0][1]), int(pt[1][1]), int(pt[0][5]), int(pt[1][5]))
        n_line10=Draw.convert_list(line10)
        # D-H vertex
        line11 = Draw.bresenham(int(pt[0][3]), int(pt[1][3]), int(pt[0][7]), int(pt[1][7]))
        n_line11 = Draw.convert_list(line11)
        # A-E vertex
        line12 = Draw.bresenham(int(pt[0][0]), int(pt[1][0]), int(pt[0][4]), int(pt[1][4]))
        n_line12=Draw.convert_list(line12)
        Draw.draw_bre2(n_line1 , n_line2,n_line3,n_line4,n_line5,n_line6,n_line7,n_line8,n_line9,
                       n_line10,n_line11,n_line12)
    if(op==30):
        op=Screens.opPrincipal()

    if(op==0):
        sys.exit()