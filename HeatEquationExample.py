import numpy as np 
import matplotlib.pyplot as plt 

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
lenX = lenY = 20
delta = 1

# BCs
Ttop = 100
Tbottom = 0
Tleft = 0
Tright = 0

# Initial guess
Tguess = 30

# Set colou interpolation and colour map.
colourInterpolation = 50
colourMap = plt.cm.jet # plt.cm.coolwarm

# Set meshgrid
X, Y, = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY)) # this only works with delta = 1

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set the BCs
T[(lenY - 1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX - 1):] = Tright
T[:, :1] = Tleft

# Iterate
print("wait")
for iteration in range(0, maxIter):
	for i in range(1, lenX - 1, delta):
		for j in range(1, lenY - 1, delta):
			T[i, j] = 0.25 * (T[i + 1][j] + T[i - 1][j] + T[i][j + 1] + T[i][j - 1])

print("Iteration finished")

# Configure the contour
plt.title("Temperature Contour")
plt.contourf(X, Y, T, colourInterpolation, cmap=colourMap)

# Set Colourbar
plt.colorbar()

# Show the result
plt.show()

input()






































