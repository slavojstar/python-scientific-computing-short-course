def AitkensDelta(sequence):
	''' Returns the Aitken acceleration of sequence '''

	val1 = next(sequence)
	val2 = next(sequence)
	val3 = next(sequence)

	while True:
		newVal = val1 - ((val2 - val1) ** 2) / (val3 - 2 * val2 + val1)
		yield newVal

		val1 = val2
		val2 = val3
		val3 = next(sequence)

def TestSequence(N):
	i = 0
	sumVal = 0

	while i <= N:
		sumVal += ((-1) ** i) / (2 * i + 1)
		yield sumVal
		i += 1

testSeq = TestSequence(100)

for x in AitkensDelta(testSeq):
	print(x)
