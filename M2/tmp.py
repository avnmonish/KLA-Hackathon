import numpy as np
import matplotlib.pyplot as plt

def points_on_circle(r, num_points = 100):
    theta_values = np.linspace(0, 2 * np.pi, num_points)
    x_values = r * np.cos(theta_values)
    y_values = r * np.sin(theta_values)
    return x_values, y_values

r = 150
num_points = 50

x, y = points_on_circle(r, num_points)

print(x, y)


plt.plot(x, y)  # 'bo' stands for blue color, circle markers
plt.axis('equal')  # Equal scaling ensures the circle looks like a circle
plt.title(f'Points on a Circle with radius {r}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
