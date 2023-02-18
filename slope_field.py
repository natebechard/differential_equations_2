import numpy as np
from matplotlib import pyplot as plt
import math


#def slope(t, y):
#    return  1 + (t * y)/2 + 0.5 * np.sin(2*t)
def slope(t, y):
    return (-t*y**2 -np.cos(t))/(np.exp(2*y)+y*t**2)

def linear(t1, y1, slope, domain):
    y_val = y1 + (slope)*(domain-t1)
    return y_val
T = np.linspace(-4, 4, 30)
Y = np.linspace(-4, 4, 30)
for j in T:
    for k in Y:
        length = 0.2
        local_slope = slope(j, k)
        dt = math.sqrt((length**2)/((local_slope**2) + 1))
        dy = math.sqrt((length**2)-(dt**2))
        current_domain = np.linspace(j-(dt/2), j+(dt/2), 2) #the end points of the small intervals on the t-axis
       # plt.plot(current_domain, linear(j, k, local_slope, current_domain), color='red')
        plt.plot((j-(dt/2)), (k + (dy/2)) , color='red')

       # plt.arrow(current_domain[0], linear(j, k, local_slope, current_domain)[0], dt, dy,
       # color='red', length_includes_head=True, head_length=.02, head_width=.01)
        plt.arrow((j-(dt/2)), (k-(dy/2)), dt, dy, color='red',length_includes_head=True, head_length=.02, head_width=.03)

plt.title("Directional Field")
plt.plot(0, 0)
plt.plot(5, 4)
plt.grid(True)
plt.show()
