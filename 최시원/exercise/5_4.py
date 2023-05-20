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
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
ans90=[]
ans50=[]
err90=[]
err90_P=[]
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if y[p]>=0.9:
        if p==t[i]:
            ans90.append(i)
        else:
            err90.append(i)
            err90_P.append(p)
    elif y[p]<50 and p==t[i]:
        ans50.append(i)

print(len(ans90)/len(x)*100)
print(len(ans50)/len(x)*100)
print(len(err90)/len(x)*100)

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x[ans90[i]].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(t[ans90[i]])
plt.show()
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x[ans50[i]].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(t[ans50[i]])
plt.show()
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x[err90[i]].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(str(t[err90[i]])+' '+str(err90_P[i]))
plt.show()