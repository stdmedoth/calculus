import matplotlib.pyplot as plt
import math
import numpy as np

n = 10000

x = 0.01
y = [ ((-1)**(i+1)*x**i)/math.factorial(i) for i in range(1,n) ]

print(sum(y)+x)