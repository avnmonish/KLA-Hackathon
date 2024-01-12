

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


with open('Testcase2.txt') as file :
    data = file.readlines()

d = float(data[0].strip().split(':')[1])
n = int(data[1].strip().split(':')[1])
angle = float(data[2].strip().split(':')[1])


import math
import sympy as sp
import numpy as np

x1 = -1
y1 = -1
x2 = -1
y2 = -1

'''

Finding n equally spaced points in the diameter of a circle of radius r where the diameter is at an angle of theta from x-axis


'''


if angle == 0 :
    x1, y1 = -d / 2, 0
    x2, y2 = d / 2, 0

    ans = []
    result = np.vstack([np.linspace(x1, x2, n), np.linspace(y1, y2, n)]).T


    with open('M11.txt', 'w') as file :

        for co in result :
            file.write('(' + str(co[0]) + ',' + str(co[1]) + ')\n')
    


elif angle == 90 :
    pass

elif angle == 180 :
    pass

elif angle == 360 :
    pass

else :

    

    # Degrees to radians :
    degToRad = float( '{num:.10f}'.format( num = (math.radians(angle) ) ))

    # Finding slope :
    slope = math.tan(degToRad)

    x, y = sp.symbols('x, y')

    # Generating an equation :
    eq = sp.Eq(y - slope*x, 0)


    print('eq', eq)

    print('slope', slope)

    lx = - d / 2
    rx = d / 2

    X = sp.solve(eq, x)  # Sub y to get x.
    Y = sp.solve(eq, y)  # Sub x to get y.

    print('x, y', X, Y)

    #print(X[0].subs(y, 150), Y[0].subs(x, -150))

    


    a = np.array([float(lx), float(Y[0].subs(x, lx)) ])
    b = np.array([float(rx), float(Y[0].subs(x, rx)) ])

    print('a,b', a, b)


    print('n', n)

    result = np.vstack([np.linspace(a[0], b[0], n), np.linspace(a[1], b[1], n)]).T

    print('fina', result, len(result))

    with open('M12.txt', 'w') as file :
        
        for co in result :
            file.write('(' + str(co[0]) + ',' + str(co[1]) + ')\n')
    
