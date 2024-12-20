import unittest
from matrix import Matrix


def create_test_matrices():
    m1 = Matrix(2, 2, 0)
    m1.set(0, 0, 1)
    m1.set(1, 0, 2)
    m1.set(0, 1, 3)
    m1.set(1, 1, 4)

    m2 = Matrix(2, 2, 0)
    m2.set(0, 0, 1)
    m2.set(1, 0, 2)
    m2.set(0, 1, 3)
    m2.set(1, 1, 4)

    m3 = Matrix(2, 2, 0)
    m3.set(0, 0, 2)
    m3.set(1, 0, 4)
    m3.set(0, 1, 6)
    m3.set(1, 1, 8)

    m4 = Matrix(2, 2, 0)
    m4.set(0, 0, 7)
    m4.set(1, 0, 10)
    m4.set(0, 1, 15)
    m4.set(1, 1, 22)

    return m1, m2, m3, m4


class TestMatrix(unittest.TestCase):
    def test_add(self):
        m1, m2, m3, m4 = create_test_matrices()
        self.assertEqual(m1 + m2, m3)

    def test_multiply(self):
        m1, m2, m3, m4 = create_test_matrices()
        self.assertEqual(m1 * m2, m4)


if __name__ == '__main__':
    unittest.main()
