import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]
data = np.loadtxt(filename, delimiter=',')

plt.imshow(data)
plt.title(filename[14:-4])
plt.show()
plt.savefig(filename[14:-4]+".png")
