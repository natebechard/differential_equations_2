import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Lets setup the grid
N = 101 # The number of grid points
T = np.linspace(0, 8, N)

# This evaluates the definite integral for all t in T
# Gotta start with an array which will hold the results of the integrations
INT = np.zeros(N)

for i in range(N):
    INT[i] = integrate.quad(lambda s:(np.exp(s**2/-4) + 0.5*np.sin(2*s)*np.exp(s**2/-4)) , 0, T[i])[0]

ini_cond = np.linspace(-2, 2, 5)


for y0 in ini_cond:
    Y = np.exp(T**2/4)*(INT + y0)
    plt.plot(T, Y)

plt.grid(True)
plt.show()

