import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    det_mat = np.linalg.det(matrix)
    if det_mat == 0 :
        return None
    matrix_rev = [[matrix[1][1], - matrix[0][1]],[-matrix[1][0],  matrix[0][0]]]
    inv_matrix = np.dot((1/ det_mat ), matrix_rev)
    return inv_matrix
    pass