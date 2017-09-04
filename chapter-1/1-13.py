def rev(lst):
    newLst = []
    for i in range(len(lst)):
        newLst.append(lst[len(lst) - 1 - i])
    return newLst


# testing - should return [5, 4, 3, 2, 1]
sampleList = [1, 2, 3, 4, 5]
print(rev(sampleList))