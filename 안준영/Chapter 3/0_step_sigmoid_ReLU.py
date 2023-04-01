import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.intc)


def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = input("Function? : ")

match y:
    case "step":
        y = step_function(x)

    case "sigmoid":
        y = sigmoid_function(x)

    case "ReLU":
        y = ReLU(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
