from scipy import *
from matplotlib.pyplot import *

x = linspace(-2 * pi, 2 * pi, 200)
plot(x, sin(x))

samples = x[::4]
plot(samples, sin(samples), 'b*', markersize = 10)

title("sin(x)")
grid()
savefig("sin.pdf")

matplotlib.pyplot.show()

input()