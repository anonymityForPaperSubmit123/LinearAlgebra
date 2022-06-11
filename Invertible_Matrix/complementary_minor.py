import numpy as np
import copy
from numpy.linalg import inv
from numpy.linalg import det


def cof(M,index):
    result = np.zeros((M.shape[0]-1,M.shape[1]-1))
    for i in range(M.shape[0]):
        temp = copy.deepcopy(M[i])
        if i==index[0]-1:
            continue
        if i >= index[0]:
            Ri = i-1
        else:
            Ri = i
        result[Ri] = np.append(temp[:index[1]-1],temp[index[1]:])
    res = det(result)
    return res

def alcof(M,index):
    res = pow(-1,index[0]+index[1])*cof(M,index)
    return res

M = np.array([[3,-1,0],[-2,1,1],[2,1,4]])
for i in range(1,4):
    for j in range(1,4):
        print("complementary minor", i, j, alcof(M, (i, j)))
