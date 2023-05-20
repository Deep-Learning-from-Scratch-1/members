# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
import pickle
from dataset.mnist import load_mnist

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
x_1=x+np.random.normal(scale=0.1,size=np.shape(x))
x_2=x+np.random.normal(scale=0.2,size=np.shape(x))
x_5=x+np.random.normal(scale=0.5,size=np.shape(x))
network = init_network()
error=0
for i in range(len(x)):
    y = predict(network, x_5[i])
    p= np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p != t[i]:
        error+=1
        
print(error/len(x)*100)
