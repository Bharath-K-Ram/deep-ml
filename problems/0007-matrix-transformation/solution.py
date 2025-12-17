import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    det_t = np.linalg.det(T)
    det_s = np.linalg.det(S)
    if det_t ==0 or  det_s == 0:
        return -1
    t_inv = np.linalg.inv(T)
    X = np.matmul(A, S)
    transformed_matrix = np.matmul(t_inv, X)

	return transformed_matrix