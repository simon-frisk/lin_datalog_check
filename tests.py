import unittest
from matrix import Matrix
from semiring import SR


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


class TestSemiRing(unittest.TestCase):
    def test_add(self):
        v1 = SR(2,2)
        v1.set(0, 1)
        v2 = SR(2, 2)
        v2.set(1, 1)
        v3 = SR(2, 2)
        v3.set(0, 1)
        v3.set(1, 1)
        self.assertEqual(v1+v2, v3)
        self.assertEqual(v3+v3,v3)

    def test_mul(self):
        v1 = SR(2, 1)
        v1.set(0, 1)
        v2 = SR(2, 1)
        v2.set(1, 1)
        v3 = SR(2, 1)
        v3.set(0, 1)
        v3.set(1, 1)
        self.assertEqual(v1 * v2, v3)
        self.assertEqual(v3 * v3, v3)

    def test_0(self):
        zero = SR(2, 1)
        v1 = SR(2, 1)
        v1.set(0, 1)
        self.assertEqual(v1 * zero, zero)
        self.assertEqual(v1 + zero, v1)

    def test_1(self):
        one = SR(2, 1)
        one.set_to_one()
        v1 = SR(2, 1)
        v1.set(0, 1)
        self.assertEqual(v1 * one, v1)

if __name__ == '__main__':
    unittest.main()
