
'''
1.
WaferDiameter:300
DieSize:30x30
DieShiftVector:(0,0)
ReferenceDie:(15,15)


2.
WaferDiameter:200
DieSize:10x10
DieShiftVector:(10,10)
ReferenceDie:(25,25)

3.
WaferDiameter:300
DieSize:24x70
DieShiftVector:(5,38)
ReferenceDie:(-7,3)

4.
WaferDiameter:300
DieSize:2x2
DieShiftVector:(15,15)
ReferenceDie:(-44,-66)
'''

import numpy as np
import matplotlib.pyplot as plt

# Input : 
with open('Testcase1.txt') as file :
    data = file.readlines()


d = int(data[0].strip().split(':')[1])
dx, dy = data[1].strip().split(':')[1].split('x')[0], data[1].strip().split(':')[1].split('x')[1]
sx, sy = data[2].strip().split(':(')[1].split(',')[0], data[2].strip().split(':(')[1].split(',')[1][ : -1]
rx, ry = data[3].strip().split(':(')[1].split(',')[0], data[3].strip().split(':(')[1].split(',')[1][ : -1]

dx, dy = int(dx), int(dy)
sx, sy = int(sx), int(sy)
rx, ry = int(rx), int(ry)

r = d // 2

print('dia', d)
print('size', dx, dy)
print('shift', sx, sy)
print('ref', rx, ry)


def points_on_circle(r, num_points = 100):
    theta_values = np.linspace(0, 2 * np.pi, num_points)
    x_values = r * np.cos(theta_values)
    y_values = r * np.sin(theta_values)
    return x_values, y_values

num_points = 50

x, y = points_on_circle(r, num_points)
x, y = points_on_circle(r)

'''
fig, ax = plt.subplots()

ax.plot(x, y)  # 'bo' stands for blue color, circle markers
ax.plot(x, [0 for i in range(100)], 'red')
ax.plot([0 for i in range(100)], y, 'red')

ax.axis('equal')  # Equal scaling ensures the circle looks like a circle

ax.plot()
plt.xticks(np.arange(-d, d, step = dx))
plt.yticks(np.arange(-d, d, step = dy))
plt.title(f'Points on a Circle with radius {r}')
plt.xlabel('x')
plt.ylabel('y')
ax.grid(which = 'major', linewidth = 1)
ax.grid(which = 'minor', linewidth = 1)

#ax.minorticks_on()

plt.show()'''


def isSafe(x, y, cx, cy, r) :

    if ((x - cx) * (x - cx) + (y - cy) * (y - cy) < r * r) :
        #print('val', (x - cx) * (x - cx) + (y - cy) * (y - cy))
        return True
    
    return False


ans = []


# Quadrant 1 :
xndx = 0
yndx = 0

for j in range(0, r + 1, dy) :
    xndx = 0
    for i in range(0, r + 1, dx) :

        if isSafe(i, j, 0, 0, r) :
            ans += [[[xndx, yndx], [i, j]]]
        
        xndx += 1
    
    print('j', j)
    
    yndx += 1

print('len', len(ans))


# Quadrant 2 :
xndx = 0
yndx = 0

for j in range(0, r + 1, dy) :

    xndx = 0
    for i in range(0, -(r + 1), -dx) :

        if isSafe(i, j, 0, 0, r) :

            #if [[xndx, yndx], [i, j]] not in ans :
            ans += [[[-1 + xndx, yndx], [-dx + i, j]]]

        xndx -= 1
    
    yndx += 1

print('len', len(ans))

# Quadrant 3 :
xndx = 0
yndx = 0

for j in range(0, -(r + 1), -dy) :
    xndx = 0
    for i in range(0, -(r + 1), -dx) :
        
        if isSafe(i, j, 0, 0, r) :
            #if [[xndx, yndx], [i, j]] not in ans :
            ans += [[[-1 + xndx, -1 + yndx], [-dx + i, -dy + j]]]

        xndx -= 1

    yndx -= 1

print('len', len(ans))

# Quadrant 4 :
xndx = 0
yndx = 0

for j in range(0, -(r + 1), -dy) :

    xndx = 0
    for i in range(0, r + 1, dx) :
        if isSafe(i, j, 0, 0, r) :
            #if [[xndx, yndx], [i, j]] not in ans :
            ans += [[[xndx, -1 + yndx], [i, -dy + j]]]
        
        xndx += 1
    
    yndx -= 1

print('ans', ans, len(ans))


with open('M21.txt', 'w') as file :

    for row in ans :

        file.write('(' + str(row[0][0]) + ',' + str(row[0][1]) + '):(' + str(row[1][0]) + ',' + str(row[1][1]) + ')\n')
