import math

#scale function 'x,y' points and 's' scale
def scale(x, y ,s):
    x = x * s
    y= y * s


    return [x, y]

#rotation function that applies the multiplication of the points by the angle
def rotation(x,y,rot):
    x1 = x * math.cos(math.radians(rot)) - y * math.sin(math.radians(rot))
    y1 = x*math.sin(math.radians(rot)) + y*math.cos(math.radians(rot))
    return [x1 , y1]
#translate function
def traslate(x , y, new_x, new_y):
    new_x = x + new_x
    new_y = y + new_y

    return [new_x, new_y]