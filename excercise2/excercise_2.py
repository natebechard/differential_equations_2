
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


N = 101
T = np.linspace(0, 8, N)

#make an array full of zeros:
YofT = np.zeros(N)
for i in range(N):

    def integrand(s):
        return(np.exp(((s**2)/-4)) + np.exp(((s**2)/-4)*(1/2)*np.sin(2*s)))
    YofT[i] = (integrate.quad(integrand, 0, T[i]))[0]  #*np.exp((T[i]**2)/4)

initial_conditions = np.array([-2, -1, 0, 1, 2])

for y0 in initial_conditions:
    Y = (np.exp(T**2/4))*(YofT + y0) #may have to fix this part
    plt.plot(T, Y)


plt.grid(True)
plt.show()