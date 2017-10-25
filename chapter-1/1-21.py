
def read_input():
    input_list = []
    while True:
        try:
            input_list.append(raw_input("Enter your input: "))
        except EOFError as e:
            for i in range(len(input_list) - 1, -1, -1):
                print(input_list[i])
            break
        
read_input()