def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    rows = len(matrix) if matrix else 1
    cols = len(matrix[0]) if matrix else 1
    N = cols if mode=="row" else rows
    if mode == "column":
        if rows < cols:
            sub = cols - rows
            for i in range(sub):
                matrix.append([0] * cols)
        rows = len(matrix) if matrix else 1
        cols = len(matrix[0]) if matrix else 1
    i,j = 0,0
    while i < rows:
        average_ = 0
        j = 0
        while j < cols:
            if mode == "column" :
                average_ += matrix[j][i]
            if mode == "row":
                average_ += matrix[i][j]
            j+=1
        i+=1
        means.append(average_ / N)


	return means