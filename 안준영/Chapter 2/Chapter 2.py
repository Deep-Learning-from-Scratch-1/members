import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # Weight, 가중치
    b = -0.7  # Bias, 편향
    return 1 if (np.sum(x * w) + b) > 0 else 0


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # Weight
    b = 0.7  # Bias, 편향
    return 1 if (np.sum(x * w) + b) > 0 else 0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # Weight
    b = -0.2  # Bias, 편향
    return 1 if (np.sum(x * w) + b) > 0 else 0


def NOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # Weight
    b = 0.2  # Bias, 편향
    return 1 if (np.sum(x * w) + b) > 0 else 0


def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))


def XNOR(x1, x2):
    return OR(NOR(x1, x2), AND(x1, x2))


logic = [AND, NAND, OR, NOR, XOR, XNOR]


def verification():
    arr = [[0, 0], [0, 1], [1, 0], [1, 1]]
    for gate in logic:
        print("{} Gate Truth Table\n".format(gate.__name__))
        print("| x1| x2| w |")

        for a in arr:
            print("| {} | {} | {} |".format(a[0], a[1], gate(a[0], a[1])))

        print("\n")


verification()
