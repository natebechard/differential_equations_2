import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# solving the initial value problem
# y' = 3 + 9t + y/2, y(0) = -40

def slope(t, y):
    sl = 3 + 9*t + y/2
    return(sl)

# Setting up the grid
t0 = 0
y0 = -40
tf = 16
ts = (t0, tf)
n = 1000
dt = (tf-t0)/n

T = np.linspace(t0, tf, n+1)

# Array to store of the y-values
ey = np.zeros(n+1)
ey[0] = y0

# Improved Euler's iteration
for i in range(n):
    pt1y = ey[i] + dt*slope(t0 + i*dt, ey[i])
    pt2y = pt1y + dt*slope((t0+i+1)*dt, pt1y)
    ey[i+1] = ey[i] + (pt2y-ey[i])/2 
    print(pt1y, pt2y, ey[i+1], slope(t0 + i*dt, ey[i]), slope((t0+i+1)*dt, pt1y))

eu = np.zeros(n+1)
eu[0] = y0

# Euler's iteration
for i in range(n):
    eu[i+1] = eu[i] + slope(t0 + i*dt, eu[i])*dt

# now the RK45 solver
sol = solve_ivp(slope, ts, (y0,), t_eval=T, method = 'DOP853')

# setting up the theoretical solution
Y = -42 - 18*T + 2*np.exp(T/2)

plt.plot(T, ey, 'r', T, Y, 'g', T, sol.y[0], 'b', T, eu, 'y')
plt.xlabel('t')
plt.ylabel('y')
plt.suptitle('Improved Euler numerical solution (red) versus Analytical solution (green) versus RK (blue), Vs Euler (yellow)')
plt.show()

# Lets also plot the discrepancies
plt.plot(T, Y-ey, 'b')
plt.xlabel('t')
plt.ylabel('Y-Ey')
plt.suptitle('Difference between the Analytical and the Improved Euler numerical solutions')
plt.show()

# Lets also plot the discrepancies
plt.plot(T, Y-sol.y[0], 'b')
plt.xlabel('t')
plt.ylabel('Y-RKy')
plt.suptitle('Difference between the Analytical and the RK-8 numerical solutions')
plt.show()