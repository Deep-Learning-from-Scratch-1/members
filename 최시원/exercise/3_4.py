import numpy as np

def softmax(x):
    c=np.max(x)
    x1=np.exp(x-c)
    return x1/np.sum(x1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

w1=np.random.normal(size=[784,50])
b1=np.zeros(50)
w2=np.random.normal(size=[50,100])
b2=np.zeros(100)
w3=np.random.normal(size=[100,10])
b3=np.zeros(10)

x=np.random.rand(784)
a1=np.dot(x,w1)+b1
z1=sigmoid(a1)
a2=np.dot(z1,w2)+b2
z2=sigmoid(a2)
a3=np.dot(z2,w3)+b3
y=softmax(a3)

print(y)