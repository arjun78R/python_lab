inp = input("Enter the string: ")
input_list = list(inp)

first_char = input_list[0]
print("First character:", first_char)

first_found = False

for i in input_list:
    if i == first_char:
        if not first_found:
            print(i)
            first_found = True
        else:
            print("$")
    else:
        print(i)
