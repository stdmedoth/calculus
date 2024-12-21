import matplotlib.pyplot as plt
import numpy as np
import math

n = 1000

x = range(1,n)
y = [1/i for i in range(1,n)]
plt.step(x,y, label='Sequence')

x_continuous = np.linspace(1, n-1, 500)
y_continuous = [1/i for i in x_continuous]

plt.plot(x_continuous, y_continuous, label='Continuous')

plt.show()


