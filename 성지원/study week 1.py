# 밑바닥부터 시작하는 딥러닝 1주차

print(type(10),'\n')
print(type(2.718),'\n')
print(type("Hello"),'\n')

x = 10
y = 3.14
print(type(x*y),'\n')

a = [1,2,3,4,5]
print(a,'\n')
print(len(a),'\n')

print(a[0],'\n')
a[4]=10
print(a)

print(a[0:2],'\n')

class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()

x0 = np.arange(0,6,0.1)
y1 = np.sin(x0)
y2 = np.cos(x0)

plt.plot(x0, y1, label="sin")
plt.plot(x0,y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

from matplotlib.image import imread

img = imread('C:/Users/성지원/OneDrive/바탕 화면/수치해석 과제/121212.png')

plt.imshow(img)
plt.show()