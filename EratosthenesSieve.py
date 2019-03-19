import numpy as np

def primes(N):
	is_prime = np.ones(N, dtype = bool)
	is_prime[:2] = False # 0, 1 not prime
	N_sqrt = int(np.sqrt(N))

	for j in range(2, N_sqrt):
		is_prime[2*j::j] = False

	return np.nonzero(is_prime)[0]


if __name__ == "__main__":
import sys
N = int(sys.argv[1]) # read in from command-line
print(primes(N))