import matplotlib.pyplot as plt
import numpy as np

#fig1 = plt.imread("taiwan.jpg")
#fig2 = plt.imread("fangao.jpg")
#fig1 = plt.imread("taiwan3.jpg")
#fig2 = plt.imread("shan.jpg")
#fig1 = plt.imread("taiwan42.jpg")
#fig2 = plt.imread("view1.jpg")
fig1 = plt.imread("taiwan5.jpg")
fig2 = plt.imread("view21.jpg")

def random_inverseable_metrix(matrixSize):
    A = np.random.rand(matrixSize,matrixSize)
    B = np.dot(A,A.transpose())
    C = B+B.T # makesure symmetric
# test whether C is definite
    D = np.linalg.cholesky(C) # if there is no error, C is definite
    E = np.linalg.inv(D)
    original = D
    reverse = E
    return original, reverse
#print("D:", D)
#print("E:", E)

def merge_and_print(fig1, fig2, original, factor, print_mark):
    print(fig1.shape)
#while True:
#        p = np.random.randint(1,3,(1000,1000))
#        try:
#            pp = np.linalg.inv(p)
#        except:
#            continue
#    print("pp:", pp)

    fig1_1 = fig1 * (1 - factor)
    fig1_2 = fig1_1.reshape(1000, -1)
    fig1_3 = np.matmul(original, fig1_2)
    fig1_4 = fig1_3.reshape(1000, 872, 3)
    plt.imsave("fig1_with_factor" + str(print_mark) + ".jpg", np.array(np.trunc(fig1_4), dtype=np.uint8), format="jpg")
    fig12 = np.trunc(fig1_4 + fig2 * factor)
    fig12 = np.array(fig12, dtype=np.uint8)
    plt.imsave("mergedr0814" + str(print_mark) + ".jpg", fig12, format="jpg")

original, reverse = random_inverseable_metrix(1000)
print(original)
print(reverse)

merge_and_print(fig1, fig2, original, 0.9, 0.9)
merge_and_print(fig1, fig2, original, 0.95, 0.95)
merge_and_print(fig1, fig2, original, 0.99, 0.99)
merge_and_print(fig1, fig2, original, 0.995, 0.995)
merge_and_print(fig1, fig2, original, 0.999, 0.999)
merge_and_print(fig1, fig2, original, 0.99999, 0.99999)
merge_and_print(fig1, fig2, original, 0.7, 0.7)
merge_and_print(fig1, fig2, original, 0.5, 0.5)
merge_and_print(fig1, fig2, original, 0.1, 0.1)
merge_and_print(fig1, fig2, original, 0.2, 0.2)
merge_and_print(fig1, fig2, original, 0.3, 0.3)
merge_and_print(fig1, fig2, original, 0.4, 0.4)

#plt.imshow(fig1)
#print("fig1:", fig1)
#fig12 = np.trunc((fig1 + fig2) / 2)
#fig12 = np.array(fig12, dtype=np.uint8)
#fig12.astype(np.int)

#print(fig12)
#plt.imsave("merged2.jpg", fig12, format="jpg")
#plt.imsave("merged21.jpg", fig1 * 2 + fig2, format="jpg")
#plt.imsave("merged22.jpg", fig1 * 4 + fig2, format="jpg")
#plt.imsave("merged23.jpg", fig1 * 6 + fig2, format="jpg")
#plt.imsave("merged24.jpg", fig1 * 8 + fig2, format="jpg")
#plt.imshow(fig12)
