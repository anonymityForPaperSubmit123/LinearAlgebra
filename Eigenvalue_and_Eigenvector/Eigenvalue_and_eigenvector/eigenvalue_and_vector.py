import numpy as np

def eigenvalue_and_vector(A):
    print('Matrix: \n{}'.format(A))
    a, b = np.linalg.eig(A)
    print('Eigenvalue: \n{}'.format(a))
    print('Eigenvector: \n{}'.format(b))
    print("\n\n")

A = np.array([[-1,1,0],[-4,3,0],[1,0,2]])
eigenvalue_and_vector(A)
