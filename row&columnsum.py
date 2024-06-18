import numpy as np

matrix = np.array([
    [2, 4, 6, 8],
    [10, 12, 14, 16],
    [18, 20, 22, 24]
])

sum_rows = np.sum(matrix, axis=1)
sum_columns = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("Sum of rows:", sum_rows)
print("Sum of columns:", sum_columns)
