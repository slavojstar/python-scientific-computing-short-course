import numpy as np 
import sys
import json
import time

def GameOfLife(M):
	''' Takes a square (0, 1)-matrix and produces iterations of Conway's Game Of Life
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

	while True:
		newM = iterate(M)
		time.sleep(0.5)
		if np.array_equal(newM, M):
			print(newM)
			print("The game board has reached an equilibrium")
			return
		else:
			M = newM
			print(M)

def neighbours(M, pos):
	''' Takes a square (0, 1)-matrix and a position of an element within it
	and returns the number of neighbours to that position which contain 1 not
	0 '''

	# Check whether the input is a matrix
	if not type(M) is np.ndarray:
		print("Warning: Can only take matrices as input, {0} is not \
			a matrix.".format(inputMatrix))
		return

	# Check whether the position is a tuple
	if not type(pos) is tuple:
		print("Warning: Position must be a tuple. {0} is not \
			a tuple.".format(pos))
		return

	# Check whether the input is a (0, 1)-matrix
	for row in M:
		for element in row:
			if not element == 0 and not element == 1:
				print("Warning: Input must be a (0, 1) matrix. {0} is not \
					a (0, 1)-matrix".format(M))
				return

	# Check if input matrix is square
	if M.shape[0] != M.shape[1]:
		print("Warning: Input must be a square matrix.")
		return

	neighbourSum = 0

	row = pos[0]
	col = pos[1]

	# Check the row above (making sure the element is not
	# on the top row)
	if not row == 0:
		if not col == 0:
			if M[row - 1][col - 1] == 1:
				neighbourSum += 1
		if M[row - 1][col] == 1:
			neighbourSum += 1
		if not col == M.shape[1] - 1:
			if M[row - 1][col + 1] == 1:
				neighbourSum += 1

	# Check the row the element is on
	if not col == 0:
		if M[row][col - 1] == 1:
			neighbourSum += 1
	if not col == M.shape[1] - 1:
		if M[row][col + 1] == 1:
			neighbourSum += 1

	# Check the row below (making sure the element is not
	# on the bottom row)
	if not row == M.shape[0] - 1:
		if not col == 0:
			if M[row + 1][col - 1] == 1:
				neighbourSum += 1
		if M[row + 1][col] == 1:
			neighbourSum += 1
		if not col == M.shape[1] - 1:
			if M[row + 1][col + 1] == 1:
				neighbourSum += 1

	return neighbourSum

def iterate(M):
	''' Takes a square (0, 1)-matrix M and applies the rules from
	Conway's Game of Life to it '''
	# Matrix doesn't actually need to be square, but whatever

	# Check whether the input is a matrix
	if not type(M) is np.ndarray:
		print("Warning: Can only take matrices as input, {0} is not \
			a matrix.".format(inputMatrix))
		return

	# Check whether the input is a (0, 1)-matrix
	for row in M:
		for element in row:
			if not element == 0 and not element == 1:
				print("Warning: Input must be a (0, 1) matrix. {0} is not \
					a (0, 1)-matrix".format(M))
				return

	# Check if input matrix is square
	if M.shape[0] != M.shape[1]:
		print("Warning: Input must be a square matrix.")
		return

	res = np.zeros(M.shape, dtype=int)
	np.copyto(res, M)

	for i in range(M.shape[0]):
		for j in range(M.shape[1]):
			element = M[i][j]
			neighs = neighbours(M, (i, j))

			if neighs < 2:
				res[i][j] = 0
			elif neighs == 2:
				continue
			elif neighs == 3:
				if element == 1:
					continue
				else:
					res[i][j] = 1
			else:
				res[i][j] = 0

	return res

inputMatrix = np.array(json.loads(sys.argv[1]))

GameOfLife(inputMatrix)














