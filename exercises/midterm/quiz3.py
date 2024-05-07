import numpy as np
import matplotlib.pyplot as plt

p = np.arange(0,1100, 100)

R = 20* p - 0.02 * p**2
plt.plot(p,R)
plt.plot('p')
plt.plot('R')
plt.show()