import numpy as np
import matplotlib.pylab as plt

#3.2 활성화 함수 : 계단 함수
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
    
# def step_function(x):
#     y = x > 0
#     return y.astype(np.int)

# x = np.array([-1.0, 1.0, 2.0])
# print("x =", x)

# y = x > 0
# print("y =", y)

# y = y.astype(np.int)
# print("y =", y)
# print()

# #그래프
# def step_function(x):
#     return np.array(x > 0, dtype=np.int)

# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)

# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)  #y축의 범위 지정
# plt.show()


#3.2 활성화 함수 : 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print("sigmoid(x) =", sigmoid(x))
print()

t = np.array([1.0, 2.0, 3.0])
print("1.0 + t =", 1.0+t)
print("1.0 / t =", 1.0/t)
print()

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

#3.2 활성화 함수 : ReLU 함수
def relu(x):
    return np.maximum(0, x)