
my_list = []
my_data = 38728

try:
    my_list[7] = my_data
except IndexError:
    print("Don't try buffer overflow attacks in Python!")