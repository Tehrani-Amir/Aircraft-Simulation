import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from airplane_simulation.first_airplane import airplane_lrh

Air = airplane_lrh()

X = np.arange(0, 20, 1)

y = 2 * X + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(X, y) 
plt.show()

print("Hello class")
plt.savefig("my_plot.png")  # Save the plot to a file