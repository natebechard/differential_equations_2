import numpy as np
import matplotlib.pyplot as plt

# solving the initial value problem
# y' = 3 + 9t + y/2, y(0) = -40

def slope(y, t):
    sl = 3 +9*t + y/2
    return(sl)

# Setting up the grid
t0 = 0
y0 = -40
tf = 100
n = 1000
dt = (tf-t0)/n

T = np.linspace(t0, tf, n+1)

# Array to store of the y-values
y = np.zeros(n+1)
y[0] = y0

# Euler's iteration
for i in range(n):
    y[i+1] = y[i] + slope(y[i], t0 + i*dt)*dt

 # setting up the theoretical solution
Y = -42 - 18*T + 2*np.exp(T/2)

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

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)