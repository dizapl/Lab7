from numpy import *
import matplotlib.pyplot as plt

x = linspace(0, 7, 50)
y = 5*sin(10*x)*sin((3*x)/(x**(1/2)))
plt.plot(x, y, label =' 5*sin(10*x)*sin(3*x)/(x**(1/2))')

plt.axis([0, 7, -7, 7])
plt.xlabel('x')
plt.ylabel('y')
plt.title('My first graph')
plt.legend()

plt.show()