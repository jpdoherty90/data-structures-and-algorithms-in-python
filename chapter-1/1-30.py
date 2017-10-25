def get_to_two(num):
    count = 0
    while num >= 2:
        num = num / 2
        count += 1
    print(count)
    return count


# tests
get_to_two(5)
get_to_two(74)
get_to_two(8734)
