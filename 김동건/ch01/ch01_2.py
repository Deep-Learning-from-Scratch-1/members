#numpy library를 이용하기

#1.5.1 넘파이 가져오기
import numpy as np

#1.5.2 numpy 배열 생성
print("---------- 배열 생성 ---------- ")
x = np.array([1.0, 2.0, 3.0])
print("x       =", x)
print("type(x) =", type(x))
print()

#1.5.3 numpy 산술 연산
print("---------- 산술 연산 ---------- ")
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x + y   =", x+y)
print("x - y   =", x-y)
print("x * y   =", x*y)
print("x / y   =", x/y)
print("x / 2.0 =", x/2.0)
print()

#1.5.4 numpy N차원 배열
print("---------- N차원 배열 ---------- ")
A = np.array([[1, 2], [3, 4]])

print("A :")
print(A)
print("행렬 형상 =", A.shape)
print("원소 타입 =", A.dtype)
print()

B = np.array([[3, 0], [0, 6]])

print("A + B :")
print(A+B)
print()

print("A * B :")
print(A*B)
print()

print("A * 10 :")
print(A*10)
print()

#1.5.5 numpy broadcast
print("---------- Broadcast ---------- ")
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])

print("A * B :")
print(A*B)
print()

#1.5.6 원소 접근
print("---------- 원소 접근 ---------- ")
X = np.array([[51, 55], [14, 19], [0, 4]])

print("X :")
print(X)
print()

print("X[0] =", X[0])
print("X[0][1] =", X[0][1])
print()

print("X :")
for row in X:
    print(row)
print()

X = X.flatten() #평탄화 : X를 1차원 배열로 변화
print("평탄화하고 나서의 X의 원소 =", X)
print("X의 0, 2, 4 인덱스의 원소  =", X[np.array([0, 2, 4])])
print()

print("X > 15  = ", X>15)
print("X[X>15] = ", X[X>15])