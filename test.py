import unittest
import main
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_compress_method(self):
        matrix = [[1, 2, 0, 0],
                  [3, 4, 5, 0],
                  [0, 6, 7, 8],
                  [0, 0, 9, 10]]
        storage = main.compress_tridiagonal_matrix(matrix)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], storage)

    def test_uncompress_method(self):
        storage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        matrix = main.uncompress_into_tridiagonal_matrix(storage)
        self.assertEqual([[1, 2, 0, 0],
                          [3, 4, 5, 0],
                          [0, 6, 7, 8],
                          [0, 0, 9, 10]], matrix)

    def test_solve_algorithm_size_4(self):
        matrix = [[1, 2, 0, 0],
                  [3, 4, 5, 0],
                  [0, 6, 7, 8],
                  [0, 0, 9, 10]]
        values = [1, 1, 1, 1]
        result = main.solve_tridiagonal_matrix(matrix, values)
        usual_result = np.linalg.solve(matrix, values)
        for i in range(len(values)):
            self.assertTrue(usual_result[i] - result[i] < 1e-9)

    def test_solve_algorithm_size_5(self):
        matrix = [[2, -1, 0, 0, 0],
                  [-3, 8, -1, 0, 0],
                  [0, -5, 12, 2, 0],
                  [0, 0, -6, -18, -4],
                  [0, 0, 0, -5, 10]]
        values = [-25, 72, -69, -156, 20]
        result = main.solve_tridiagonal_matrix(matrix, values)
        usual_result = np.linalg.solve(matrix, values)
        for i in range(len(values)):
            self.assertTrue(usual_result[i] - result[i] < 1e-9)

    def test_solve_algorithm_size_6(self):
        matrix = [[4, 2, 0, 0, 0, 0],
                  [1, 3, 1, 0, 0, 0],
                  [0, 4, 5, 2, 0, 0],
                  [0, 0, 2, 9, 4, 0],
                  [0, 0, 0, 6, 3, 3],
                  [0, 0, 0, 0, 1, 2]]
        values = [1, 2, 3, 4, 5, 6]
        result = main.solve_tridiagonal_matrix(matrix, values)
        usual_result = np.linalg.solve(matrix, values)
        for i in range(len(values)):
            self.assertTrue(usual_result[i] - result[i] < 1e-9)


if __name__ == '__main__':
    unittest.main()
