

class SR:
    """
    semiring
    elements are vectors of length k.
    + : addition is elementwise max.
    * : multiplication is elementwise addition, bounded by p.
    0 : additive identity is a special element, here None.
    1 : multiplicative identity is the zero vector.
    """

    def __init__(self, k, p):
        """
        Initialize the semiring value to the zero element.
        """
        self.k = k
        self.p = p
        self.value = None

    def copy(self):
        c = SR(self.k, self.p)
        c.value = None if self.value is None else self.value.copy()
        return c

    def set_to_one(self):
        self.value = [0 for i in range(self.k)]

    def set(self, index, val):
        if self.value is None:
            self.set_to_one()
        self.value[index] = val

    def __add__(self, other):
        result = SR(self.k, self.p)
        if self.value is None:
            return other.copy()
        elif other.value is None:
            return self.copy()
        result.set_to_one()

        for i in range(self.k):
            result.set(i, max(self.value[i], other.value[i]))
        return result

    def __mul__(self, other):
        result = SR(self.k, self.p)
        if self.value is None or other.value is None:
            return result
        result.set_to_one()

        for i in range(self.k):
            result.set(i, min(self.value[i] + other.value[i], self.p))
        return result

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return self.value.__repr__()