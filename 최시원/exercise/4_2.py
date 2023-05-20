import sys, os
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
from dataset.mnist import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False, normalize=False)
max=np.max(x_train[0][0].flatten())
img=max-x_train[0][0]
plt.imshow(img,cmap=plt.cm.binary)
plt.show()

plt.imshow(img.T,cmap=plt.cm.binary)
plt.show()