def odd_product(sequence):
    count = 0
    for i in sequence:
        if i % 2 == 1:
            count += 1
    return count == 2


testSequence = [2, 3, 4, 6, 8, 9, 10, 12]
testSequence2 = [2, 3, 4, 6, 8, 10, 12]
testSequence3 = [2, 3, 4, 6, 8, 9, 10, 12, 13]

# should print true, false, false
print(odd_product(testSequence))
print(odd_product(testSequence2))
print(odd_product(testSequence3))
