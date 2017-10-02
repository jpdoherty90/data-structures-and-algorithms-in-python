import random

def shuffle(data):
    index = random.randint(0, len(data) - 1)
    return data[index]

print shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])

