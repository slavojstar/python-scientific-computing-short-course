import scipy.sparse as sp
import scipy.sparse.linalg as la
import numpy as np

N = 1000; h = 1.0 / (N+1)
K = sp.diags(diagonals=[2, -1, -1], offsets=[0, -1, 1],\
	shape=(N, N), format="lil")

rhs = 2 * np.ones(N) * h**2
print(K.toarray())
print(rhs)

K[+0,:] = 0.0
K[-1,:] = 0.0
rhs[+0] = 0.0
print(K.toarray())
print(rhs)

K[+0, +0] = 1.0
K[-1, -1] = 1.0
rhs[-1]   = 0.0
print(K.toarray())
print(rhs)

K = K.tocsr()

u = la.spsolve(K, rhs)
print(u)