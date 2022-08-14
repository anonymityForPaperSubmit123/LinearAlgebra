import numpy as np
from numpy.linalg import inv

def eigenvalue_and_vector(A):
    print('Matrix A: \n{}'.format(np.round(A+0.000001, 3))) 
    a, b = np.linalg.eig(A)
    print('\nEigenvalue \lambda: \n{}'.format(np.round(a+0.000001, 3)))
    print('\nEigenvector P: \n{}'.format(np.round(b+0.000001, 3)))
    print("\n")
    return a, b

def verify(eigenvalue, eigenvector, ori):
    inv_ev = inv(eigenvector)
    a1 = np.matmul(inv_ev, ori)
    a2 = np.matmul(a1, eigenvector)
    eigenvalue += 0.000001
    a3 = a2 + 0.000001

    print("P^{-1} A P: \n", np.round(a3, 3))
    


A = np.array([[0,0,0,0,0.5],[0.25,0,1.0/3,0,0.5],[0.25,1,0,1,0],[0.25,0,1.0/3,0,0],[0.25,0,1.0/3,0,0]])
eigenvalue, eigenvector = eigenvalue_and_vector(A)
verify(eigenvalue, eigenvector, A)







C = np.array([[-1,1,0],[-4,3,0],[1,0,2]])
B = np.array([[-1,2,0],[-5,3,0],[10,0,2]])
D = np.array([[0,0.5,0,0.5,0.5],[0.25,0,1.0/3,0,0.5],[0.25,0.5,0,0.5,0],[0.25,0,1.0/3,0,0],[0.25,0,1.0/3,0,0]])
#D = np.array([[0,0.5,0.333333,0.5,0.5],[0.25,0,0.33333333,0,0.5],[0.25,0.5,0,0.5,0],[0.25,0,0,0,0],[0.25,0,0.3333333,0,0]])
E = np.array([[0,0.5,0.333333,0.5,0.5],[0.25,0,0.33333333,0,0.5],[0.25,0.5,0,0.5,0],[0.25,0,0,0,0],[0.25,0,0.3333333,0,0]])
F = np.array([[0,0.5,0,0.5,0.5],[0.25,0,1.0/3,0,0.5],[0.25,0.5,0,0.5,0],[0.25,0,1.0/3,0,0],[0.25,0,1.0/3,0,0]])
G = np.array([[0,0.5,0,0,0.5],[0.25,0,1.0/3,0,0.5],[0.25,0.5,0,1,0],[0.25,0,1.0/3,0,0],[0.25,0,1.0/3,0,0]])
H = np.array([[0,0,0,0.5,0.5],[0.25,0,1.0/3,0,0.5],[0.25,1.0,0,0.5,0],[0.25,0,1.0/3,0,0],[0.25,0,1.0/3,0,0]])
I = np.array([[0,0,0,0.5,0.5],[0.25,0,0,0,0.5],[0.25,1.0,0,0.5,0],[0.25,0,0.5,0,0],[0.25,0,0.5,0,0]])

"""eigenvalue_and_vector(B)
eigenvalue_and_vector(C)
eigenvalue_and_vector(D)
eigenvalue_and_vector(F)
eigenvalue_and_vector(G)
eigenvalue_and_vector(H)
eigenvalue_and_vector(I)"""
