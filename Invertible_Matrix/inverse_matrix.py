import numpy as np
import copy
from numpy.linalg import inv

M = np.array([[3,-1,0],[-2,1,1],[2,1,4]])
print("inverse_matrix:", inv(M))
