from scipy import *
from matplotlib.pyplot import *

def mandelbrot(h, w, maxit = 20):
'''Returns image of Mandelbrot fractal of size (h, w)'''
x = linspace(-2, 0.8, w)
y = linspace(-1.4, 1.4, h)
X, Y = meshgrid(x, y)
c = X + Y * 1j
z = c
divtime = maxit + zeros(z.shape, dtype = int)
  for iteration in xrange(maxit):
    z = z ** 2 + c
    diverge = z * conj(z) > 2 ** 2
    div_now = diverge & (divtime == maxit)
    divtime[div_now] = iteration
    z[diverge] = 2
  return divtime