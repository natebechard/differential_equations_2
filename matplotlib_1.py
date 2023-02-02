import matplotlib.pyplot as plt
fig = plt.figure(1)	#identifies the figure 
plt.title("Y vs X", fontsize='16')	#title


for a in range(0, 10):
    for b in range(0, 10):
        plt.arrow(a, b, 0.2*a, (0.1*a)*(0.1*a))
plt.plot(10,10)
plt.plot(0,0)


plt.xlabel("X",fontsize='13')	#adds a label in the x axis
plt.ylabel("Y",fontsize='13')	#adds a label in the y axis
plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
#plt.savefig('Y_X.png')	#saves the figure in the present directory
plt.grid()	#shows a grid under the plot#
plt.show()