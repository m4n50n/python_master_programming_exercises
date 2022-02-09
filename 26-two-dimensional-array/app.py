def matrix(x, y):
    matrix = []

    for rows in range (0, x):
        row = []
        for cell in range(0, y):
            row.append(rows * cell)

        matrix.append(row)

    return matrix

print(matrix(3, 5))