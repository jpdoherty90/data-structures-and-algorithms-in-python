def sum_squares(n):
    return sum([k * k for k in range(n-1, 0 , -1)])


# test with 6 - should be 55
print sum_squares(6)
