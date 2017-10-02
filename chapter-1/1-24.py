def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for i in range(len(string)):
        if string[i] in vowels:
            counter += 1
    return counter

print count_vowels("Target")