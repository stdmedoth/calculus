""" 0.(9) = 1 """

import matplotlib.pyplot as plt
n = 100

x = [i for i in range(1,n)]
y = [sum([9/10**i2 for i2 in range(1,i)]) for i in range(1,n)]
y2 = [1 for i in range(1,n)]


plt.step(x,y)
# plt.plot(x,y2)


plt.show()


