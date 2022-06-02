#In pygame x=0 and y=0 start at the top left of the main screen. To center the coordinates in the midle of the screen
# it is necessary convert the x and y coordinates

#function that convert coordinates x,y
def convert(x,y):

    if(x>0):
        x=x+300
    if(x<0):
        x=300+x
    if (x == 0):
        x = 300


    if(y>0):
        y=300-y
    if(y<0):
        y=300+(y*-1)
    if (y == 0):
        y = 300
    return x,y

#function that convert a list of coordinates (x,y)
def convert_l(points):
    new_points=[]
    for x in range(len(points)):
        new_points.append(points[x])


    for x in range(len(new_points)):
        if(new_points[x][0]>0):
            new_points[x][0]=new_points[x][0]+300
        if (new_points[x][1] > 0):
            new_points[x][1] = 300-new_points[x][1]
        if (new_points[x][0] < 0):
            new_points[x][0] = 300+new_points[x][0]
        if (new_points[x][1] < 0):
            new_points[x][1] = 300 + (new_points[x][1]*-1)
        if (new_points[x][0] == 0):
            new_points[x][0] = 300
        if (new_points[x][1] == 0):
            new_points[x][1] = 300
    return new_points