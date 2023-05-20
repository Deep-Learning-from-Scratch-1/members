import numpy as np
import matplotlib.pyplot as plt

#arr=np.arange(25).reshape([5,5]).T
#arr=np.arange(25).reshape([5,5])
#arr=np.flipud(np.fliplr(arr))
arr=np.zeros([5,5])
arr+=np.array([[0,0,1,0,0]])
arr+=np.array([[0,0,1,0,0]]).T
plt.imshow(arr,cmap=plt.cm.gray)
plt.show()