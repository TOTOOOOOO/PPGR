import numpy as np


def osmoteme(points):
    for i in range(len(points)):
        points[i] = np.append(points[i], 1)

    # points = [p1, p2, p3, p5, p6, p7, p8]
            #   0   1   2   3   4   5   6
    xb1 = np.cross(np.cross(points[3], points[4]), np.cross(points[3], points[6]))
    xb2 = np.cross(np.cross(points[3], points[4]), np.cross(points[0], points[1]))
    xb3 = np.cross(np.cross(points[0], points[1]), np.cross(points[5], points[6]))
    
    yb1 = np.cross(np.cross(points[4], points[5]), np.cross(points[5], points[6]))
    yb2 = np.cross(np.cross(points[4], points[5]), np.cross(points[1], points[2]))
    yb3 = np.cross(np.cross(points[1], points[2]), np.cross(points[5], points[6]))

    zb1 = np.cross(np.cross(points[1], points[4]), np.cross(points[2], points[5]))
    zb2 = np.cross(np.cross(points[1], points[4]), np.cross(points[0], points[3]))
    zb3 = np.cross(np.cross(points[2], points[5]), np.cross(points[0], points[3]))


    xb = (xb1 + xb2 + xb3) / 3
    yb = (yb1 + yb2 + yb3) / 3
    zb = (zb1 + zb2 + zb3) / 3


    p41 = np.cross(np.cross(xb, points[2]), np.cross(yb, points[0]))
    p42 = np.cross(np.cross(xb, points[2]), np.cross(zb, points[6]))
    p43 = np.cross(np.cross(yb, points[0]), np.cross(zb, points[6]))


    p4 = (p41 + p42 + p43) / 3

    p4 = p4 / p4[2]
    res = np.array([round(p4[0]), round(p4[1]), 1])  

    return res

p1 = np.array([104,361])
p2 = np.array([93,113])
p3 = np.array([502,66])
p5 = np.array([568,706])
p6 = np.array([570,291])
p7 = np.array([1045,160])
p8 = np.array([1019,432])
points = [p1, p2, p3, p5, p6, p7, p8]

p4 = osmoteme(points)
print(p4)
