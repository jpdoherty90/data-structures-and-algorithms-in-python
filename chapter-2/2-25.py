class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other [j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other [j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other [j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __mul__(self, multiplier):
        if type(multiplier) is Vector:
            result = 0
            for j in range(len(self)):
                result += self[j] * multiplier[j]
            return result
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * multiplier
            return result

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'




v = Vector(5)
v[1] = 23
v[-1] = 45
u = v + [5, 3, 10, -2, 1]
# Testing new multiplication
print(u * 4)
print(u * v)