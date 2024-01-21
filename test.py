import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from airplane_simulation.first_airplane import airplane_lrh

Air = airplane_lrh()

AA = np.arange(0, 20, 1)

y = 2 * AA + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(AA, y) 
plt.show()

print("Hello class")
