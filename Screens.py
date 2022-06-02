#class that will show the sub options screens
import sys


def opPrincipal():

    print("Choose a Option:")
    print("1-Draw in a Screen.")
    print("2-Fill.")
    print("3-Cut.")
    print("4-Geometric Transformations.")
    print("5-Projections.")
    print("0-Exit")

    op = int(input())

    if(op == 1):
        op1 = tDraw()
        if(op1 == 1):
            return 1
        if(op1 == 2):
            return 2
        if(op1 == 3):
            return 3
        if(op1 == 4):
            return 4
        if (op1 == 5):
            return 30
    if(op == 2):
        op2 = tFill()
        if(op2 == 1):
            return 5
        if(op2 == 2):
            return 6
        if (op2 == 3):
            return 30
    if(op == 3):
        op3 = tCut()
        if(op3 == 1):
            return 7
        if(op3 == 2):
            return 8
        if (op3 == 3):
            return 30
    if(op == 4):
        op4 = tTransform()
        if(op4==1):
            return 9
        if(op4==2):
            return 10
        if(op4==3):
            return 11
        if (op4 == 4):
            return 30
    if(op == 5):
        op5 = tProjection()
        if(op5 == 1):
            return 12
        if(op5 == 2):
            return 13
        if (op5 == 3):
            return 14
        if (op5 == 4):
            return 15
        if (op5 == 5):
            return 16
        if (op5 == 6):
            return 30
    if(op == 0):
        sys.exit()

def tDraw():
    print("1-Draw Line(Bresenham).")
    print("2-Draw Circle .")
    print("3-Draw Curve.")
    print("4-Polylines.")
    print("5-Return")
    op=int(input())
    return op
def tFill():
    print("1-Flood Fill Algorithm.")
    print("2-ScanLine Algorithm.")
    print("3-Return")
    op = int(input())
    return op
def tCut():
    print("1-Cut Line.")
    print("2-Cut Polygon.")
    print("3-Return")
    op = int(input())
    return op
def tTransform():
    print("1-Scale Polygon.")
    print("2-Rotation Polygon")
    print("3-Translate Polygon.")
    print("4-Return")
    op = int(input())
    return op
def tProjection():
    print("1-Front Ortogonal Projection(Plan View)")
    print("2-Side Ortogonal Projection")
    print("3-Back Ortogonal Projection")
    print("4-Top Ortogonal Projection")
    print("5-Isometric Axometric Projection")
    print("6-Return")
    op = int(input())
    return op
