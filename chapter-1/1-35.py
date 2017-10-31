# BIRTHDAY PARADOX
import random

def birthday_paradox(n):
    birthdays = []
    for i in range(n):
        new_birthday = random.randint(1, 365)
        if new_birthday in birthdays:
            return True
        birthdays.append(new_birthday)
    return False



# TESTS
print(birthday_paradox(3))
print(birthday_paradox(20))
print(birthday_paradox(23))
print(birthday_paradox(44))
print(birthday_paradox(255))
print(birthday_paradox(432))
