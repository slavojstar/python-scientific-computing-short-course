from scipy import io as spio
import numpy as np 
a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a})
data = spio.loadmat('file.mat')
print(data['a'])