#3.3 다차원 배열의 계산
import numpy as np

A = np.array([1, 2, 3, 4])
print("A =", A)
print("np.ndim(A) =", np.ndim(A)) #몇 차원인지 알려줌
print("A.shape    =", A.shape)
print("A.shape[0] =", A.shape[0])
print()

B = np.array([[1, 2], [3, 4], [5, 6]])
print("B :")
print(B)
print("np.ndim(B) =", np.ndim(B))
print("B.shape    =", B.shape)
print()

#3.3.2 행렬의 곱
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A.shape =", A.shape)
print("B.shape =", B.shape)
print("np.dot(A,B) :")
print(np.dot(A, B))
print()

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
C = np.array([[1, 2], [3, 4]])

print("A.shape =", A.shape)
print("B.shape =", B.shape)
print("C.shape =", C.shape)

print("np.dot(A, B) :")
print(np.dot(A, B))
print()
#print("np.dot(A, C) :")
#print(np.dot(A, C))        #형상이 안 맞아서 오류

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])

print("A.shape =", A.shape)
print("B.shape =", B.shape)
print("np.dot(A, B) :", np.dot(A, B))
print()

X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print("X.shape =", X.shape)
print("W.shape =", W.shape)
print("W :")
print(W)
print("Y :", Y)