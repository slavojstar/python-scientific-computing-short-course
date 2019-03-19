import random

class Polynomial(object):
	def __init__(self, coeffs):
		for coeff in coeffs:
			if not isinstance(coeff, (int, float, complex)):
				print('Cannot initialise a polynomial with non-numeric coefficients:\
					 {0}'.format(coeffs))
				return

		# Polynomial(k) should return the same as Polynomial([k])
		if isinstance(coeffs, (int, float, complex)):
			coeffs = [coeffs]

		# Any zeros at the tail end of the coeffs array don't make
		# a difference, so chop them off
		while coeffs[-1] == 0:
			del coeffs[-1]

		self.coeffs = coeffs
		self.degree = len(coeffs) - 1

	def __add__(self, p):
		pCoeffs = p.coeffs
		coeffs = self.coeffs

		# Extend the shorter list of coefficients in preparation to add
		# them together
		diff = len(coeffs) - len(pCoeffs)
		if diff > 0:
			pCoeffs.extend([0] * diff)
		else:
			coeffs.extend([0] * (-diff))

		newCoeffs = [m + n for (m, n) in zip(pCoeffs, coeffs)]

		return Polynomial(newCoeffs)

	def eval(self, x):
		''' Returns p evaluated at x '''
		if not isinstance(x, (int, float)):
			print("Error with eval({0}): Polynomial must be evaluated at a \
				real number.".format(x))

		return sum(coeff * (x ** i) for (coeff, i) in zip(self.coeffs, range(len(self.coeffs))))

	def differentiate(self):
		''' Returns the polynomial which is the differential of the original '''
		newCoeffs = [coeff * i for (coeff, i) in zip(self.coeffs, range(len(self.coeffs)))]
		del newCoeffs[0]

		return Polynomial(newCoeffs)

	def integrate(self):
		''' Returns the polynomial which is the integral of the original '''
		newCoeffs = [float(coeff) / (i + 1) for (coeff, i) in zip (self.coeffs, range(len(self.coeffs)))]
		newCoeffs.insert(0, 0)

		return Polynomial(newCoeffs)

	def roots(self, tol):
		''' Returns the roots of the polynomial to within a distance of tol 
		using the Aberth method '''
		# Create an array of approximations to the roots
		approx = []

		while len(approx) < self.degree:
			newRoot = random.randint(-self.degree, self.degree)
			if newRoot in approx:
				continue
			else:
				approx.append(newRoot)

		offsets = [self.degree + 1] * len(approx)

		while max(offsets) > tol:
			for i in range(len(approx)):
				root = approx[i]

				# Make a list without the root so you can calculate the sum of the
				# inverses of the differences without dividing by zero
				approxWithoutRoot = approx[:i] + approx[i + 1:]
				sumDiff = sum(1 / (root - x) for x in approxWithoutRoot)

				# Get the (pseudo) Newton step
				p = self.eval(root)
				pDashed = self.differentiate().eval(root)
				newton = p / pDashed

				offset = newton / (1 - newton * sumDiff)
				offsets[i] = offset

				approx = root - offset

		return approx
				
	def multiply(self, q):
		''' Returns p x q '''

		coeffs = self.coeffs
		qCoeffs = q.coeffs
		newCoeffs = [0] * (self.degree + q.degree) 

		for k in range(len(coeffs) + len(qCoeffs) - 1):
			for i in range(len(coeffs)):
				for j in range(len(qCoeffs)):
					if i + j == k:
						newCoeffs[k] += coeffs[i] * qCoeffs[j]

		return Polynomial(newCoeffs)

p = Polynomial([4, 4, 1])
print(p.roots(0.01))














