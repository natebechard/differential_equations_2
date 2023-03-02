import numpy as np
import matplotlib.pyplot as plt

# solving the initial value problem
# y' = 3 + 9t + y/2, y(0) = -40

def slope(y, t):
    sl = (t**2 + 3*(y**2))/(2*t*y)
    return(sl)

# Setting up the grid
t_init = 1
y_init = 1
tf = 10
n = 100
dt = (tf-t_init)/n

T = np.linspace(t_init, tf, n+1)

# Array to store of the y-values
y = np.zeros(n+1) #euler Y values
y[0] = y_init

# Euler's iteration
for i in range(n):
    y[i+1] = y[i] + slope(y[i], t_init + i*dt)*dt

# setting up the theoretical solution
Y = T*np.sqrt(2*T - 1)

plt.plot(T, y, 'r', T, Y, 'g')
plt.xlabel('t')
plt.ylabel('y')
plt.suptitle('Euler numerical solution (red) versus Analytical solution (green)')
plt.show()

# Lets also plot the discrepancies
plt.plot(T, Y-y, 'b')
plt.xlabel('t')
plt.ylabel('Y-y')
plt.suptitle('Difference between the Analytical and the Euler numerical solutions')
plt.show()
