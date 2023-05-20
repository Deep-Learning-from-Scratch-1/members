import numpy as np

def softmax(x):
    c=np.max(x)
    x1=np.exp(x-c)
    return x1/np.sum(x1)

def relu(x):
    return np.maximum(0,x)

x=np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]])
w1=np.array([[0,0,0,0,1],\
             [-1,0,0,0,0],\
             [0,-1,0,0,0],\
             [0,0,-1,0,0],\
             [0,0,0,-1,0]])
b1=np.array([5,4,3,2,1])
w2=np.array([[0,1,0,0,0],\
             [0,0,1,0,0],\
             [0,0,0,1,0],\
             [0,0,0,0,1],\
             [1,0,0,0,0]])
b2=np.array([-1,-2,0,0,0])

a1=np.dot(x,w1)+b1
z1=relu(a1)
a2=np.dot(a1,w2)+b2
y=softmax(a2)

print(y)