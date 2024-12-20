from matrix import Matrix
from semiring import SR


def identity_matrix(n, p):
    """
    Create the identity matrix for the semiring for the instance with n nodes, over a p stable semiring
    """
    assert(n % 3 == 0)

    vector_length = n ** 2 // 9

    matrix = Matrix(n, n, SR(vector_length, p))
    one = SR(vector_length,p)
    one.set_to_one()

    for i in range(n):
        matrix.set(i,i,one.copy())

    return matrix


def create_program_matrix(n, p):
    """
    Construct the matrix describing the datalog program
    :param n: the number of nodes in the graph. Needs to be a multiple of 3
    :param p: the p for which the semiring is p-stable
    :return: the matrix describing the program
    """
    assert(n % 3 == 0)

    vector_length = n**2 // 9

    matrix = Matrix(n, n, SR(vector_length, p))

    one = SR(vector_length,p)
    one.set_to_one()

    for i in range(0, n // 3):
        matrix.set(i, (n // 3), one.copy())
    for i in range(n // 3, 2 * n // 3):
        matrix.set(i, i + 1, one.copy())
    for i in range(2 * n // 3, n):
        matrix.set(2 * n // 3 - 1, i, one.copy())

        for j in range(0, n//3):
            el = SR(vector_length, p)
            el.set_to_one()
            el.set((i - 2 * n // 3) * n // 3 + j, 1)
            matrix.set(i, j, el)

    return matrix


def iterate(matrix, identity):
    """
    For matrix A, let A^(i)=1+A+A^2+...+A^i. Return the lowest i such that A^(i)=A^(i+1).
    """
    i = 0
    current = identity
    while True:
        prev = current
        current = current * matrix + identity
        #print(current)
        if current == prev:
            break
        else:
            i += 1
    return i


def main():
    for p in [1, 2, 5]:
        for n in [6, 9, 30]:
            print("n=", n, ", p=", p, end=": ", sep="")
            m = create_program_matrix(n, p)
            identity = identity_matrix(n, p)
            print(iterate(m, identity), "iterations")


if __name__ == "__main__":
    main()
