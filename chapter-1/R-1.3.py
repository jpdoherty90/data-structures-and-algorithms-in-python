def minmax(data):
    small = data[0]
    large = data[0]
    for num in data:
        if num < small:
            small = num
        elif num > large:
            large = num
    results = (small, large)
    return results









# test
test_data = [2, 4, 6, 8, 10, 12]
print minmax(test_data)