from scipy import *
from matplotlib.pyplot import *

x = range(5)
y = [1, 2, 1, 3, 5]
p2 = polyfit(x, y, 2)
p4 = polyfit(x, y, 4)

xx = linspace(-1, 5, 200)
plot(xx, polyval(p2, xx), label="degree 2")
plot(xx, polyval(p4, xx), label="degree 4")
plot(x, y, 'b*', markersize=10)

axis([-1, 5, 0,6])
legend(loc='upper left')
title('Polynomial fitting')

matplotlib.pyplot.show()

input()