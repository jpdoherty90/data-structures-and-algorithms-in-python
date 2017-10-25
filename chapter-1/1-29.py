# Write a Python program that outputs all possible strings formed by using the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.

letters = ['c', 'a', 't', 'd', 'o', 'g']

def perms(arr, strings=[], i=0, next_string=""):
    if len(strings) == 726:
        return strings
    if len(next_string) == 6:
        strings.append(next_string)
    








perms(letters)