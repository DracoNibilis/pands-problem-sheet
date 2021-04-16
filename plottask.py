# Program  that displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4] on the one set of axes.
# Author: Magdalena Malik

import numpy as np 
import matplotlib.pyplot as plt # importing modules that we gonna use

xpoints = np.array(range(0,5)) 
ypoints = xpoints * xpoints
zpoints = xpoints * xpoints * xpoints

plt.title("plot of functions: f(x)=x, g(x)=x**2 and h(x)=x**3") # plot title
plt.plot(xpoints,linestyle="dashed", color="red", label="f(x)=x") # plot of f(x)=x
plt.plot(ypoints,linestyle="dotted", color="yellow", label="g(x)=x**2") #plot of g(x)=x**2
plt.plot(zpoints,linestyle="solid", color="green", label="h(x)=x**3") # plot of h(x)=x**3
plt.legend()
plt.show()