def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = []
    for  i in matrix:
        temp = []
        for j in i:
            temp.append(scalar * j)
        result.append(temp)
	return result