import math

# (a)
def ab3(f, u0, t0, tT, N):
	''' Returns a list containing N approximations to the soln.
	of a differential equation du/dt = f(u) with u(0) =  u0[0]
	in the interval t0 to tT '''
	approx = [u0[0], u0[1], u0[2]]
	h = (tT - t0) / N

	for n in range(N - 3):
		newU = approx[n + 2] + h * ((23 / 12) * f(approx[n + 2]) - (16 / 12) * \
			f(approx[n + 1]) + (5 / 12) * f(approx[n]))
		approx.append(newU)

	return approx

# (b)

def GCDEuclid(a, b):
	''' Returns the GCD of integers a and b using Euclid's algorithm. '''

	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {0} is not an integer".format(a, b))
		return

	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {1} is not an integer".format(a, b))
		return

	while b != 0:
		t = b
		b = a % b
		a = t

def gcd(a, b):
	''' Returns the GCD of integers a and b '''
	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {0} is not an integer".format(a, b))
		return

	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {1} is not an integer".format(a, b))
		return

	if b == 0:
		return a
	else:
		return gcd(b, a % b)

