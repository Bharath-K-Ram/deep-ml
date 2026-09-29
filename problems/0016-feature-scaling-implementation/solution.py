import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	temp = data.T
	standardized_data, normalized_data = [],[]
	for i in temp:
		mean = np.mean(i)
		std = np.std(i)
		standardized_data.append(list(np.round((i-mean)/std,4)))
		x_sort = sorted(i)
		x_min,x_max = x_sort[0] , x_sort[-1]
		diff = x_max - x_min
		normalized_data.append(list(np.round((i-x_min)/(diff),4)))

	return list(np.array(standardized_data).T), list(np.array(normalized_data).T)