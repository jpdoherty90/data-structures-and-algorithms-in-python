def dot(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print dot(arr1, arr2)