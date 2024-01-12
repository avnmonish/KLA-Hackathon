

'''
1.
WaferDiameter:300
NumberOfPoints:30
Angle:0

2.
WaferDiameter:300
NumberOfPoints:10
Angle:45

3.
WaferDiameter:200
NumberOfPoints:25
Angle:250

4.
WaferDiameter:200
NumberOfPoints:31
Angle:150
'''


with open('Testcase1.txt') as file :
    data = file.readlines()

d = int(data[0].strip().split(':')[1])
n = int(data[1].strip().split(':')[1])
angle = float(data[2].strip().split(':')[1])


import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x1 = -1
y1 = -1
x2 = -1
y2 = -1


if angle == 0 :
    x1, y1 = -d / 2, 0
    x2, y2 = d / 2, 0

    ans = []
    result = np.vstack([np.linspace(x1, x2, n), np.linspace(y1, y2, n)]).T


    with open('M11.txt', 'w') as file :

        for co in result :
            file.write('(' + str(co[0]) + ',' + str(co[1]) + ')\n')
    

else :

    # Degrees to radians :
    degToRad = float( '{num:.10f}'.format( num = (math.radians(angle) ) ))

    # Finding slope :
    slope = math.tan(degToRad)

    x, y = sp.symbols('x, y')

    # Generating an equation :
    eq = sp.Eq(y - slope*x, 0)

    def intersection_points_with_circle(m, r):
    
        x_positive = r / np.sqrt(1 + m**2)
        x_negative = -r / np.sqrt(1 + m**2)


        y_positive = m * x_positive
        y_negative = m * x_negative

        # Return intersection points as tuples
        point_positive = (x_positive, y_positive)
        point_negative = (x_negative, y_negative)

        return point_positive, point_negative

    # Example usage
    m_slope = slope  # Replace with your desired slope
    radius = d // 2     # Replace with your desired radius

    intersection_points = intersection_points_with_circle(m_slope, radius)

    print(f"Intersection Point 1: {intersection_points[0]}")
    print(f"Intersection Point 2: {intersection_points[1]}")


    print('eq', eq)

    print('slope', slope)

    lx = - d / 2
    rx = d / 2

    X = sp.solve(eq, x)  # Sub y to get x.
    Y = sp.solve(eq, y)  # Sub x to get y.

    print('x, y', X, Y)

    #print(X[0].subs(y, 150), Y[0].subs(x, -150))

    
    #a = np.array([float(lx), float(Y[0].subs(x, lx)) ])
    #b = np.array([float(rx), float(Y[0].subs(x, rx)) ])

    #a = np.array([106.06601717798212, 106.06601717798212])
    #b = np.array([-106.06601717798212, -106.06601717798212])

    a = np.array([intersection_points[0][0], intersection_points[0][1]])
    b = np.array([intersection_points[1][0], intersection_points[1][1]])

    print('a,b', a, b)

    print('n', n)

    result = np.vstack([np.linspace(a[0], b[0], n), np.linspace(a[1], b[1], n)]).T

    print('fina', result, len(result))

    with open('M14.txt', 'w') as file :
        
        for co in result :
            file.write('(' + str(co[0]) + ',' + str(co[1]) + ')\n')
