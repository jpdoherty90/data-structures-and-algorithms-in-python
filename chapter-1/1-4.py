def sum_of_squares(n):
    sum = 0
    for num in range(n-1, 0, -1):
        sum += num * num
    return sum



# test with 6 - answer should be 55
print sum_of_squares(6)