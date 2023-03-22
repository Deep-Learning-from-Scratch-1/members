#3.5 출력층 설계
import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)
print("exp_a =", exp_a)

sum_exp_a = np.sum(exp_a)
print("sum_exp_a =", sum_exp_a)

y = exp_a / sum_exp_a
print("y =", y)
print("y =", softmax(a))
print()

#softmax함수 개선
a = np.array([1010, 1000, 990])
#print(softmax(a)) #값이 너무 커서 overflow
c = np.max(a)
a -= c
print(np.exp(a)/np.sum(np.exp(a)))
print(softmax(a))
print()

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print("y =", y)
print("sum(y) =", np.sum(y))