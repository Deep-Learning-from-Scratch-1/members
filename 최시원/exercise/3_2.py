import numpy as np

def softmax(x):
    c=np.max(x)
    x1=np.exp(x-c)
    return x1/np.sum(x1)

w1=np.array([[1,2,3],[-4,-5,-6]])
b1=np.array([0,0,0])
w2=np.array([[5,0],[0,-3],[4,0]])
b2=np.array([0,0])
x=np.log(np.array([4,2]))

a1=np.dot(x,w1)+b1
a2=np.dot(a1,w2)+b2
y=softmax(x)
print(y)
