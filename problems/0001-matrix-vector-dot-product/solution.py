def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a[0]) != len(b):
        return -1
    a_len = len(a)
    b_len = len(b)
    final_result = []
    for i in range(a_len):
        temp = 0
        for j in range(b_len):
            temp +=  (a[i][j] * b[j])
        final_result.append(temp)
    return final_result
	pass