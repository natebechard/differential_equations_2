
import matplotlib.pyplot as plt
import numpy as np

length1 = 1
angle1 = (np.pi)/4   #all angles in radians
length2 = 0.75
angle2 = (np.pi)/6
length3 = 0.1
angle3 = (np.pi)/8

coord_0 = [0,0]
coord_1 = [length1*np.cos(angle1), length1*np.sin(angle1)]
coord_2 = [coord_1[0] + length2*np.cos(angle1), coord_1[1] + length2*np.sin(angle1)]

x_coords = np.array([coord_0[0], coord_1[0]])
y_coords = np.array([coord_0[1], coord_1[1]])
x_coords_2 = np.array([coord_1[0], coord_2[0]])
y_coords_2 = np.array([coord_1[1], coord_2[1]])

print(coord_0, coord_1)

plt.plot(x_coords, y_coords)
plt.plot(x_coords_2, y_coords_2)
#plt.plot(coord_1, coord_2)
plt.show()