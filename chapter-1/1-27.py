

def factors(n):
    k = 1
    factors_list = []
    while k * k < n:
        if n % k == 0:
            yield k
            factors_list.insert(0, n//k)
        k += 1
    if k * k == n:
        yield k
    for factor in factors_list:
        yield factor