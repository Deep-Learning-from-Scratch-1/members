# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
import pickle
from dataset.mnist import load_mnist
import time

def softmax(x):
    c=np.max(x)
    x1=np.exp(x-c)
    return x1/np.sum(x1)

def sigmoid(x):
    return 1/(1+np.exp(-x))


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    #W1, W2, W3 = network['W1'], network['W2'], network['W3']
    #b1, b2, b3 = network['b1'], network['b2'], network['b3']
    W1=np.random.normal(size=[784,50])
    b1=np.zeros(50)
    W2=np.random.normal(size=[50,100])
    b2=np.zeros(100)
    W3=np.random.normal(size=[100,10])
    b3=np.zeros(10)
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
start=0
end=0
batchTime=[]
network = init_network()
for i in range(1,31):
    start=time.time()
    for j in range(0,len(x),i):
        y = predict(network, x[j:j+i])
    end=time.time()
    timeVal=end-start
    print(timeVal)
    batchTime.append(timeVal)

batchTimeX=np.arange(1,31)
plt.plot(batchTimeX,batchTime)
plt.show()