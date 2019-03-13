import math

h = 1 / 1000
a = - 1 / 2

approx = [1, math.exp(h * a), math.exp(2 * h * a)]
exact = approx[:]

for n in range(997):
	newU = approx[n + 2] + h * a * ((23 / 12) * approx[n + 2] - (4 / 2) * approx[n + 1]\
		+ (5 / 12) * approx[n])
	approx.append(newU)
	exact.append(math.exp(a * (n + 3) * h))

error = []

for (e, a) in zip(exact, approx):
	error.append(e - a)


