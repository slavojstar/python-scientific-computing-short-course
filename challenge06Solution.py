import numpy as np 
import sys
import json

def GameOfLife(M):
	''' Takes a (0, 1)-matrix and produces iterations of Conway's Game Of Life
	on it '''

	# Check whether the input is a matrix
	if not type(M) is np.ndarray:
		print("Warning: Can only take matrices as input, {0} is not a matrix.".format(inputMatrix))
		return

	# Check whether the input is a (0, 1)-matrix
	for row in M:
		for element in row:
			if not element == 0 and not element == 1:
				print("Warning: Input must be a (0, 1) matrix. {0}".format(element))
				return

	# Check if input matrix is square
	if M.shape[0] != M.shape[1]:
		print("Warning: Input must be a square matrix.")
		return




	M = np.insert(M, 0, 0, axis=1)
	M = np.insert(M, 0, 0, axis=1)
	M = np.insert(M, M.shape[1], 0, axis=1)
	M = np.insert(M, M.shape[1], 0, axis=1)

	zeros = np.zeros((1, M.shape[1]), dtype=int)

	M = np.concatenate((zeros, zeros, M))
	M = np.concatenate((M, zeros, zeros))

	print(M)

inputMatrix = np.array(json.loads(sys.argv[1]))


GameOfLife(inputMatrix)