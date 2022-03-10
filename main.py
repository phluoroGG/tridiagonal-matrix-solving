def compress_tridiagonal_matrix(matrix):
    matrix_storage = [matrix[0][0], matrix[0][1],
                      matrix[len(matrix) - 1][len(matrix) - 2], matrix[len(matrix) - 1][len(matrix) - 1]]
    for row in range(1, len(matrix) - 1):
        for col in range(row - 1, row + 2):
            matrix_storage.insert(len(matrix_storage) - 2, matrix[row][col])
    return matrix_storage


def uncompress_into_tridiagonal_matrix(matrix_storage):
    size = (len(matrix_storage) + 2) // 3
    first_row = [matrix_storage[0], matrix_storage[1]]
    for i in range(size - 2):
        first_row.append(0)
    last_row = [matrix_storage[len(matrix_storage) - 2], matrix_storage[len(matrix_storage) - 1]]
    for i in range(size - 2):
        last_row.insert(0, 0)
    matrix = [first_row, last_row]
    for i in range(1, size - 1):
        row = []
        for j in range(i - 1):
            row.append(0)
        for j in range(3):
            row.append(matrix_storage[j + 3 * i - 1])
        for j in range(size - 2 - i):
            row.append(0)
        matrix.insert(len(matrix) - 1, row)
    return matrix


def solve_tridiagonal_matrix(matrix, values):
    size = len(values)
    if isinstance(matrix[0], list):
        matrix = compress_tridiagonal_matrix(matrix)
    v_values = [- matrix[1] / matrix[0]]
    u_values = [values[0] / matrix[0]]
    for i in range(1, size - 1):
        divider = matrix[3 * i - 1] * v_values[len(v_values) - 1] + matrix[3 * i]
        v_values.append(- matrix[3 * i + 1] / divider)
        u_values.append((values[i] - matrix[3 * i - 1] * u_values[len(u_values) - 1]) / divider)
    u_values.append((values[size - 1] - matrix[3 * size - 4] * u_values[len(u_values) - 1])
                    / (matrix[3 * size - 4] * v_values[len(v_values) - 1] + matrix[3 * size - 3]))
    result = [u_values[len(u_values) - 1]]
    for i in range(size - 1):
        result.insert(0, v_values[size - i - 2] * result[0] + u_values[size - i - 2])
    return result


if __name__ == '__main__':
    matrix_ = [[4, 2, 0, 0, 0, 0],
               [1, 3, 1, 0, 0, 0],
               [0, 4, 5, 2, 0, 0],
               [0, 0, 2, 9, 4, 0],
               [0, 0, 0, 6, 3, 3],
               [0, 0, 0, 0, 1, 2]]
    values_ = [1, 2, 3, 4, 5, 6]
    result_ = solve_tridiagonal_matrix(matrix_, values_)
    print(result_)
