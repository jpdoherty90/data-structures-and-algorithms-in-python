def sum_odd_squares(n):
    return sum([k*k for k in range(n, 0, -1) if (k % 2 == 1)])



# test with 8 -> should print 84
print sum_odd_squares(8)