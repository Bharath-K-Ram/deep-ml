import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    row = len(a)
    col = len(a[0])
    b = np.zeros((col, row))
    for iidx , i_value in enumerate(a):
        for jidx, j_value in enumerate(i_value):
            b[jidx][iidx] = j_value
	return b