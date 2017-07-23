def sum_odd_squares(n):
    sum = 0
    for num in range(n-1, 0, -1):
        if num % 2 == 1:
            sum += num * num
    return sum



# test with 8 - should print 84
print sum_odd_squares(8)