
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

fig, ax = plt.subplots()
def animate(i):
	angle = (i/180.0)*(math.pi)
	ax.clear()
	plt.xlabel("X",fontsize='13')	#adds a label in the x axis
	plt.ylabel("Y",fontsize='13')	#adds a label in the y axis
	plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
	circle1 = plt.Circle((0, 0), 1, color='r', fill=False)
	ax.add_patch(circle1)
	plt.arrow(0,0,math.cos(angle),math.sin(angle))
	plt.arrow(0,0,math.cos(angle),0, color='g')
	plt.arrow(math.cos(angle),0,0,math.sin(angle), color='b')
	
ani = FuncAnimation(fig, animate, interval=100)
plt.plot(-1.2,-1.2)
plt.plot(1.2,1.2)
plt.show()