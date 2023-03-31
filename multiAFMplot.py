import sys
import numpy as np
import matplotlib.pyplot as plt

mean_data = []
total_data = []

for file in sys.argv[1:]:
	data = np.loadtxt(file, delimiter=',')

	total_data.append(data)
	mean_data.append(np.mean(data,axis=0))

	plt.plot(np.mean(data,axis=0),alpha=0.3,color='blue')

total_data = np.array(total_data)
mean_data = np.array(mean_data)

plt.plot(np.mean(mean_data,axis=0),color='blue')
plt.title('Surface Compare')
plt.show()
plt.savefig('surface_compare.png')

plt.imshow(np.mean(total_data,axis=0))
plt.title('Overall Average Surface')
plt.show()
plt.savefig('mean_surface.png')
