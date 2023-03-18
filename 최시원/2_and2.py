import numpy as np
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1
    
def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1
    
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

print("AND")
print("x1 x2  y")
print(" 0  0  "+str(AND(0,0)))
print(" 0  1  "+str(AND(0,1)))
print(" 1  0  "+str(AND(1,0)))
print(" 1  1  "+str(AND(1,1)))

print("NAND")
print("x1 x2  y")
print(" 0  0  "+str(NAND(0,0)))
print(" 0  1  "+str(NAND(0,1)))
print(" 1  0  "+str(NAND(1,0)))
print(" 1  1  "+str(NAND(1,1)))

print("OR")
print("x1 x2  y")
print(" 0  0  "+str(OR(0,0)))
print(" 0  1  "+str(OR(0,1)))
print(" 1  0  "+str(OR(1,0)))
print(" 1  1  "+str(OR(1,1)))

print("XOR")
print("x1 x2  y")
print(" 0  0  "+str(XOR(0,0)))
print(" 0  1  "+str(XOR(0,1)))
print(" 1  0  "+str(XOR(1,0)))
print(" 1  1  "+str(XOR(1,1)))