# Input is a string of space-separated words

def word_counts(s):
    arr = s.split(" ")
    count_dict = {}
    for i in range(len(arr)):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
        else:
            count_dict[arr[i]] = 1
    return count_dict




#TESTS
print(word_counts("dog cat frog pig dog dog snake snake snake cat frog dog dog"))