import numpy as np
from scipy.linalg import fractional_matrix_power

def mat_X_vec(m, v):
    res = np.dot(m, v)
    return res

def mat_X_mat(m1, m2):
    res = np.matmul(m1, m2)
    return res

def mat_n_power(m, n):
    m2 = m.copy()
    for i in range(n):
        m3 = mat_X_mat(m2, m)
        m2 = m3.copy()
    return m3

def main():
#    a = np.array([[3.0/4, 1.0/36],[1.0/4, 35.0/36]])
    a = np.array([[11.0/12, 1.0/36],[1.0/12, 35.0/36]])
    x1 = np.array([5, 10])
    x2 = np.array([3, 6])

    a6 = mat_n_power(a, 3)
    a7 = mat_n_power(a, 5)
    a2 = mat_n_power(a, 10)
    a3 = mat_n_power(a, 100)
    a8 = mat_n_power(a, 100000)

    print("A^3*x_1:", mat_X_vec(a6, x1))
    print("A^5*x_1:", mat_X_vec(a7, x1))
    print("A^10*x_1:", mat_X_vec(a2, x1))
    print("A^100*x_1:", mat_X_vec(a3, x1))
    print("A^1000*x_1:", mat_X_vec(a8, x1))

    print("A^3*x_1:", mat_X_vec(a6, x2))
    print("A^5*x_1:", mat_X_vec(a7, x2))
    print("A^10*x_1:", mat_X_vec(a2, x2))
    print("A^100*x_1:", mat_X_vec(a3, x2))
    print("A^1000*x_1:", mat_X_vec(a8, x2))

def main2():
#    a = np.array([[3.0/4, 1.0/36],[1.0/4, 35.0/36]])
    a = np.array([[11.0/12, 1.0/36],[1.0/12, 35.0/36]])
    x1 = np.array([5, 10])
    x2 = np.array([3, 6])

    a5 = mat_n_power(a, 1)
    a6 = mat_n_power(a, 3)
    a7 = mat_n_power(a, 5)
    a2 = mat_n_power(a, 10)
    a3 = mat_n_power(a, 100)
    a4 = mat_n_power(a, 30)
    a8 = mat_n_power(a, 100000)

    print("A*x_1:", mat_X_vec(a, x1))
    print("A^2*x_1:", mat_X_vec(a5, x1))
    print("A^3*x_1:", mat_X_vec(a6, x1))
    print("A^5*x_1:", mat_X_vec(a7, x1))
    print("A^10*x_1:", mat_X_vec(a2, x1))
    print("A^30*x_1:", mat_X_vec(a4, x1))
    print("A^100*x_1:", mat_X_vec(a3, x1))
    print("A^1000*x_1:", mat_X_vec(a8, x1))

    print("A*x_1:", mat_X_vec(a, x2))
    print("A^2*x_1:", mat_X_vec(a5, x2))
    print("A^3*x_1:", mat_X_vec(a6, x2))
    print("A^5*x_1:", mat_X_vec(a7, x2))
    print("A^10*x_1:", mat_X_vec(a2, x2))
    print("A^30*x_1:", mat_X_vec(a4, x2))
    print("A^100*x_1:", mat_X_vec(a3, x2))
    print("A^1000*x_1:", mat_X_vec(a8, x2))

main()
