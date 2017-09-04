def are_different(sequence):
    for i in range(len(sequence)): 
        count = 0
        for j in range(len(sequence)):
            if sequence[i] == sequence[j]:
                count += 1
                if count > 1:
                    return False
    return True


distinctList = [1, 2, 3,  4, 5, 6, 7]
notDistinctList = [1, 2, 3, 2, 4, 5, 6]

# testing - should print true, false
print(are_different(distinctList))
print(are_different(notDistinctList))