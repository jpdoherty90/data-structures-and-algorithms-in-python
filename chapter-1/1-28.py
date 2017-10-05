import math

def norm(v, p=2):
    sum = 0
    for val in v:
        x = pow(val, p)
        sum += x
        print "SUM: ", sum
    norm = pow(sum, 1. / p)
    return norm


print norm((4,3))