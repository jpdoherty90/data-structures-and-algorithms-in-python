import collections

class Vector:
    
    # new constructor function
    def __init__(self, d):
        if isinstance(d, collections.Iterable):
            self._coords = [0] * len(d) 
            for i in range(len(d)):
                self._coords[i] = d[i]
        else:
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
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * multiplier
        return result


    def __rmul__(self, multiplier):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * multiplier
        return result


    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'




v = Vector(5)
print(v)
# testing new constructor
u = Vector([1, 2, 3, 4, 5])
print(u)