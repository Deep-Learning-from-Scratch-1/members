import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
#AND 함수 구현
print("---------- AND 함수 ---------- ")
print("0 0 |", AND(0, 0))
print("0 1 |", AND(0, 1))
print("1 0 |", AND(1, 0))
print("1 1 |", AND(1, 1))
print()

#가중치와 편향 도입
print("---------- 가중치와 편향 ---------- ")
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print("x * w:")
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x)+b)