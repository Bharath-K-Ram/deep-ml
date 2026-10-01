import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	matrix = np.array(a)
	init_shape = matrix.shape
	N = init_shape[0] * init_shape[1]

	M = new_shape[0] * new_shape[1]
	reshaped_matrix = []
	n = new_shape[1]
	if N == M:
		flat = matrix.flatten().tolist()
		for i in range(new_shape[0]):
			n = new_shape[1]
			temp = []
			for j in range(new_shape[1]):
				idx = i * n + j
				temp.append(flat[idx])
			reshaped_matrix.append(temp)
	return reshaped_matrix

