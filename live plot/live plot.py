import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint
import time


data = [3, 6, 2, 1, 8]
fig, ax = plt.subplots()
def animate(i):
    data.append(randint(0, 10))
    ax.clear()
    ax.plot(data[-20:]) # plot the last 5 data points
# call the animation
ani = FuncAnimation(fig, animate, interval=10)

# show the plot
plt.show()
