import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X, dtype=float)
	y = np.array(y,dtype=float).reshape(-1,1)

	theta = np.linalg.inv(X.T @ X) @ X.T @ y

	theta = list (np.round(theta.flatten() , 4))
	# Your code here, make sure to round
	return theta