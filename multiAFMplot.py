import sys
import numpy as np
import matplotlib.pyplot as plt

total_data = []

for file in sys.argv[1:]:
	data = np.loadtxt(file, delimiter=',')

	total_data.append(np.mean(data,axis=0))

total_data = np.array(total_data)

plt.plot(np.mean(total_data,axis=0))
plt.title('Overall Mean Surface')
plt.show()
plt.savefig('mean_surface.png')
