def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    
    b = matrix [0][0] + matrix [1][1]
    c = matrix [0][1] + matrix [1][0]
    
    sq_rt =  ((b ** 2) - 4 * (b - c))**0.5
    lamb_1 = (b + sq_rt)/2
    lamb_2 = (b - sq_rt)/2
    eigenvalues = [round(lamb_1), round(lamb_2)]
	return eigenvalues