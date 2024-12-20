

class Matrix:

    def __init__(self, n, m, zero):
        self.n = n
        self.m = m
        self.zero = zero
        # n rows and m columns
        # store matrix as list of rows
        self.values = [[zero for i in range(m)] for j in range(n)]

    def get(self, i, j):
        return self.values[i][j]

    def set(self, i, j, val):
        self.values[i][j] = val

    def __mul__(self, other):
        assert(self.m == other.n)
        result = Matrix(self.n, self.m, self.zero)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    # Something like this, not sure
                    new_val = result.get(i, j) + self.get(i, k) * other.get(k, j)
                    result.set(i, j, new_val)
        return result

    def __add__(self, other):
        assert(self.n == other.n and self.m == other.m)

        result = Matrix(self.n, self.m, self.zero)
        for i in range(self.n):
            for j in range(self.m):
                result.set(i,j, self.get(i,j) + other.get(i,j))

        return result

    def __eq__(self, other):
        if not type(other) == Matrix:
            return False
        return self.values == other.values

    def __str__(self):
        string = "\n"
        for row in self.values:
            for v in row:
                string += f" {v}"
            string += "\n"
        return string

